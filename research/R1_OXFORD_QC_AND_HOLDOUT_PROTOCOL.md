# R1 data qualification — Oxford structural audit and pre-registration
**Audit date:** 2026-11-27. Original source: uploaded Oxford_Battery_Degradation_Dataset_1.mat, ExampleDC_C1.mat, Readme.txt. This is *data QC*, not calibration, verification of sensor accuracy, or independent model validation.

## Reproducible scan
Run `python scripts/audit_oxford_structural.py /path/to/Oxford_Battery_Degradation_Dataset_1.mat --output output.csv`. Does not download or redistribute third-party data. The source field `t` is MATLAB datenum in days; conversion to elapsed seconds is `(t-t[0])*86400`. The smaller ExampleDC_C1.mat instead has elapsed-second integer timestamps and needs its own adapter.

### Counts
| Cell | Characterization checkpoints | Phase records |
|---|---:|---:|
| 1 | 78 | 312 |
| 2 | 73 | 292 |
| 3 | 76 | 304 |
| 4 | 47 | 188 |
| 5 | 46 | 184 |
| 6 | 46 | 184 |
| 7 | 77 | 308 |
| 8 | 76 | 304 |
| **Total** | **519** | **2076** |

Combined: **15,264,130 observations** over the `t,v,q,T` trajectories (not independent experiments). Four phases per checkpoint: C1ch, C1dc, OCVch, OCVdc. All 2076 trajectories had finite t,v,q,T and strictly increasing recorded timestamps in the scan.

### Critical QC findings
- **Cell1/cyc1600/all four phases:** temperature is approximately **0.519–0.522 °C**, inconsistent with the README's 40 °C chamber. Values are finite but almost certainly a channel/unit/sensor recording anomaly. QUARANTINE thermal records; other channels require independent assessment.
- **Cell1/cyc3200/OCVch and OCVdc:** one timestamp gap of about **545,688 s** and **545,840 s** respectively. Total durations ~661,666 and 661,861 s. Do not infer normal contiguous experiment or integrate current across the gap without verification.
- **Cell1/cyc4500/OCVch and OCVdc:** one timestamp gap of about **543,993 s** and **544,109 s** respectively. Total durations ~655,516 and 655,624 s. Quarantine time-dependent analysis.
- **All other records:** no nonfinite entries, nonincreasing timestamps or >600-second gaps identified under these specific tests. This is **not** a pass on physical plausibility, signal calibration, uniform sampling, or charge conservation.
- Some nominal 100-cycle checkpoints absent; do not impute missing ones or assume samples are independent.

**Minimum exclusions for thermal temporal training and holdouts:** all Cell1/cyc1600 phases; four Cell1/cyc3200 and cyc4500 OCV phase traces pending raw verification (8 records total). Do not remove records silently; preserve exclusion reason and immutable source reference.

### Example file
`ExampleDC_C1.mat` directly inspected: separate 840-sample `ch` and 3145-sample `dc`. Example charge q increment ~345.193 mAh, with nominal charge current ~1483 mA. This is a **partial segment**, not a full 0-to-100% 2C charge. Current sign convention differs between charge and discharge segments; verify against q derivative. Example timestamps are elapsed numerical seconds rather than serial day numbers.

## Pre-registered evaluation design (proposal, not yet executed)
1. **Time and units:** load raw Oxford files; convert main MAT datenum to elapsed seconds, example integer seconds as-is; check sample gaps and derivative of q vs imposed/derived I (convert mAh and s carefully).
2. **Physical QC before modeling:** check V range and outliers, temperature continuity, charge monotonicity by phase, duplicate traces, start SOC, cycle-to-cycle temperature drift and actual ambient sensor status; preserve all failures.
3. **Training:** use *Cell1, Cell2, Cell3, Cell4* early checkpoints (up to cyc3000, except quarantined records). Use only relevant compatible phases. These boundaries are proposed in advance and require a parameter-identifiability analysis.
4. **Within-cell temporal holdout:** later checkpoints from training cells, without fitting to them. Evaluates ageing extrapolation; label as such.
5. **Entire-cell holdout:** reserve *Cell5–Cell8* completely for final testing. All are in the same test rig at nominal 40 °C; this is cross-cell generalization, not cross-thermal-condition transfer.
6. **Baseline reporting:** measured V and surface T only; evaluate MAE, RMSE, max abs error, event-end errors and temporal residuals at sequence level; uncertainty intervals per held-out **cell**, avoiding sample-wise pseudo-replication.
7. **No XFC claim:** main 1C and example nominal 2C records, at one chamber setpoint, cannot support independent validation of XFC or cooling architecture superiority.
8. **Acceptance criteria:** specify quantitative thresholds *before fitting*, justified by sensor accuracy, sampling resolution, response scale and benchmark papers. No arbitrary error threshold chosen after results.
9. **Identifiability:** with only surface T, known chamber setpoint but no directly measured heat flux or core T, avoid jointly fitting unconstrained `R_int, C_core, C_surface, h, dUocv/dT`; freeze independently sourced parameters or report identifiable combinations only.

## Dataset source and licensing
Oxford readme: eight 740 mAh Kokam pouch cells in 40 °C chamber, ODbL 1.0 / DbCL 1.0; no copied raw dataset is committed. Original validation source is Birkl thesis and original archived dataset.

## Stanford raw-data blocker
Catenaro & Onori, *Data in Brief* 35 (2021) 106894, https://doi.org/10.1016/j.dib.2021.106894. Mendeley dataset DOI 10.17632/kxsbr4x3j2.2: https://data.mendeley.com/datasets/kxsbr4x3j2/2 (CC BY 4.0). Article documents six experimental steps and step-indexed raw XLSX layout; whether all charge steps are actually in the downloadable XLSX remains **unverified**. The Mendeley public landing page displays a Download All control but no file list in retrieved HTML; direct REST access failed due DNS/network restrictions in this environment. No files downloaded, no claim of inspected raw charging traces.

## Newly discovered candidate experimental sources (not full-paper audited)
- Chen et al. 2020 original cell-parameterisation validation data: https://doi.org/10.5281/zenodo.4032560 (LG M50, three cells, measured chamber/surface T and I/V, charge CC-CV, C/10–1.5C discharge); source metadata from OpenAIRE. This is a direct chemistry-and-thermal-boundary reference, but not XFC.
- *High-power lithium-ion battery characterization dataset for stochastic battery modeling*, Scientific Data (2025), https://doi.org/10.1038/s41597-025-05725-y. Abstract describes 12 high-power cells with surface temperatures; raw data and fast-charge profiles not yet audited.
- *Lithium-Ion Battery Pack Cycling Dataset with CC-CV Charging and WLTP/Constant Discharge Profiles*, Scientific Data (2025), https://doi.org/10.1038/s41597-025-06229-5. Article abstract describes multi-point temperatures up to 36 cells, closer to module thermal benchmarking; CC-CV protocol still must be checked for rates and thermal boundary.
These are **discovery candidates only**; no full-text/figure/equation or raw dataset qualification claimed.

## R1 exit gate
**Not passed**: full source-level experimental metadata, charge/current consistency, cell sensor calibration/thermal transfer identifiability, true high-rate *charge* thermal evidence and independent cooling-boundary measurements remain unresolved.
