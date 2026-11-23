# Existing software and open-data audit — 2026-11-23
**Scope:** source inspection only; no package installation, reproduction, or dataset-download validation performed. No external project is asserted to have experimentally validated XFC cooling.

## Software / repositories

### S01 — PyBaMM (strong reference baseline)
Repo: https://github.com/pybamm-team/PyBaMM
Docs: https://docs.pybamm.org/
**Source checked:** project README and actual base model implementation listing thermal and current-control options.
**Capabilities:** parameterized battery simulations including electrochemical models, thermal submodels, experiments/charging controls. It already supports lumped and spatial thermal options; using it can avoid rebuilding established solvers.
**Relevance:** choose as benchmark/optional dependency after pinning version. Must compare state, heat-rate and voltage conventions.
**Limit:** existence of a model/parameter set does not validate a particular commercial cell at XFC.

### S02 — liionpack (pack electrical/thermal network comparator)
Repo: https://github.com/pybamm-team/liionpack
**Source checked:** repository README. Uses PyBaMM models in a pack/netlist; example records volume-averaged temperature and heating. **Readme explicitly says maintenance mode**; critical fixes only, no planned features.
**Relevance:** pack-network reference rather than new custom pack architecture by default.
**Limit:** dependency compatibility, cooling topology representation and test validity need checks.

### S03 — BattMo (continuum electrochemical-thermal alternative)
Repo: https://github.com/BattMoTeam/BattMo
**Source checked:** README; MATLAB/MRST continuum electrochemical modelling, coupled thermo-electrochemical simulations, finite-volume grid infrastructure.
**Relevance:** independent higher-fidelity modeling approach and geometry/finite-volume reference.
**Limit:** MATLAB/MRST toolchain and cell data; not a plug-in measured fast-charge cooling reference.

### S04 — Dedicated BTMS community models
Search: https://github.com/topics/battery-thermal-management
**Status:** discovery only; individual implementations not technically audited. Do not cite arbitrary project outputs as validation.

## Experimental datasets

### D01 — NASA Ames Li-ion Battery Aging Dataset
https://data.nasa.gov/dataset/li-ion-battery-aging-datasets
**Source checked:** original NASA catalog and field list.
**Fields:** charge profiles record time, measured current, terminal voltage and temperature; ambient temperature and EIS/discharge records also supplied. Time series from 18650 cells.
**Pros:** measurable coupled electro-thermal outputs useful for first thermal/electrical benchmarking.
**Concerns:** aging and moderate-charge domain, unknown exact charging regime/thermal convection at each record, external dataset license shown as *not specified*. Download/raw metadata must be inspected before declaring fit for holdout tests. No redistribution until license clarified.

### D02 — Oxford Battery Degradation Dataset 1
https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac
**Source checked:** repository metadata plus indexed readme. Includes time/voltage/charge/temperature for some records, eight small pouch cells.
**Pros:** experimental T and V with cycling.
**Concerns:** archival page blocked during inspection; file-level check not yet made; ageing/1C not XFC. Not selected as XFC validation.

### D03 — Stanford Chueh group charging and cycle-life resources
https://chuehlab.stanford.edu/datasets
**Source checked:** original group dataset directory. Includes Attia et al. 2020 closed-loop fast-charging protocol dataset/code and Severson et al. 2019 cycle-life dataset/code.
**Pros:** fast-charge protocol design and cell ageing evidence.
**Concerns:** verify original data field schema and whether measured temperature + thermal boundaries are actually provided. Fast-charge cycle life cannot be substituted for heat-transfer validation.

### D04 — Published discharge experimental dataset (2021)
https://pmc.ncbi.nlm.nih.gov/articles/PMC7941039/
**Source checked:** indexed abstract.
**Pros:** Panasonic NCR18650B, LG INR21700-M50 and A123 ANR26650m1-B, including surface temperature, current, voltage and varied discharge conditions.
**Concerns:** raw data and uncertainty must be checked; discharge profiles cannot independently validate charge XFC.

## Dataset qualification checklist
- [ ] Stable original download, version, and license
- [ ] Chemistry, cell product, cell type, capacity and dimensions known
- [ ] Current sign, time step, units, SOC and voltage thresholds known
- [ ] Temperature sensor location, calibration and ambient chamber arrangement documented
- [ ] Rest, charging, discharge, pulse and ageing sequences segregated
- [ ] Heat transfer boundary and uncertainty known or independently estimable
- [ ] Calibration and independent holdouts predetermined
- [ ] Rate, temperature, SOC domain supports final claimed application
- [ ] Reproduction script and hash recorded (only after dataset access)

## Software decision
**Do not build a new electrochemical solver yet.** First benchmark suitability of PyBaMM and liionpack and locate an experimental dataset whose measured boundaries and outputs can support identifiable heat-generation and thermal models. Custom development should target a demonstrable unmet scientific need, especially reproducible matched-service cooling comparisons and uncertainty accounting.

## Licensing
No datasets or third-party code are vendored in BatteryThermalBench. Verify every project's license and each dataset's independent terms before future reuse.


## 2026-11-23 correction following direct user-provided files
The earlier Oxford entry above described a metadata-only search. **That status is superseded:** the original 254 MiB `.mat` and a first-cycle `.mat` were provided and directly inspected. Oxford's README explicitly states ODbL 1.0/DbCL 1.0, so the prior 'archive blocked; file-level check not yet made' limitation no longer applies. The Stanford Catenaro/Onori primary 8-page paper was also manually reviewed, but its raw Excel files were not. The NASA catalog currently says 'This dataset has no data', and its license remains unspecified. For validated dataset status see [the dataset audit](DATASET_AUDIT_01_OXFORD_STANFORD_NASA.md); this addendum overrides any conflicting earlier statements in this file.
