"""Audit Oxford Battery Degradation Dataset 1. Requires numpy/scipy; no fitting."""
import argparse
import csv
import json
from pathlib import Path
import numpy as np
from scipy.io import loadmat

PHASES = ("C1ch", "C1dc", "OCVch", "OCVdc")
def audit(path):
    mat = loadmat(path, squeeze_me=True, struct_as_record=False)
    records = []
    for cell_name in sorted((k for k in mat if k.startswith("Cell")), key=lambda x: int(x[4:])):
        cell = mat[cell_name]
        for checkpoint in sorted(cell._fieldnames):
            if not checkpoint.startswith("cyc"):
                continue
            obj = getattr(cell, checkpoint)
            for phase in PHASES:
                if not hasattr(obj, phase):
                    raise ValueError(f"Missing phase: {cell_name}/{checkpoint}/{phase}")
                z = getattr(obj, phase)
                cols = {f: np.ravel(getattr(z, f)).astype(float) for f in ("t", "v", "q", "T")}
                sizes = {len(a) for a in cols.values()}
                if len(sizes) != 1:
                    raise ValueError(f"Unequal vector lengths: {cell_name}/{checkpoint}/{phase}")
                n = len(cols["t"])
                if n < 2:
                    raise ValueError(f"Fewer than 2 rows: {cell_name}/{checkpoint}/{phase}")
                dt_s = np.diff(cols["t"]) * 86400.0  # MATLAB datenum, in DAYS
                flags = []
                if not all(np.isfinite(a).all() for a in cols.values()):
                    flags.append("NONFINITE")
                if (dt_s <= 0).any():
                    flags.append("NONMONOTONIC_TIME")
                if np.nanmin(cols["T"]) < 20 or np.nanmax(cols["T"]) > 60:
                    flags.append("TEMPERATURE_REVIEW")
                if (dt_s > 600).any():
                    flags.append("TIME_GAP_OVER_600_S")
                records.append({
                    "cell": cell_name, "checkpoint": checkpoint, "phase": phase,
                    "samples": n, "elapsed_s": round(float((cols["t"][-1]-cols["t"][0])*86400), 3),
                    "max_step_s": round(float(np.nanmax(dt_s)), 3),
                    "charge_change_mAh": round(float(cols["q"][-1]-cols["q"][0]), 4),
                    "temperature_min_C": round(float(np.nanmin(cols["T"])), 4),
                    "temperature_max_C": round(float(np.nanmax(cols["T"])), 4),
                    "flags": ";".join(flags),
                })
    return records

def main():
    p = argparse.ArgumentParser()
    p.add_argument("mat_path", type=Path)
    p.add_argument("--output", type=Path, default=Path("oxford_qc_records.csv"))
    args = p.parse_args()
    records = audit(args.mat_path)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(records[0]))
        w.writeheader()
        w.writerows(records)
    flagged = [r for r in records if r["flags"]]
    print(json.dumps({"records": len(records), "flagged_records": len(flagged),
                      "sample_count": sum(r["samples"] for r in records),
                      "flagged_examples": flagged[:12]}, indent=2))

if __name__ == "__main__":
    main()
