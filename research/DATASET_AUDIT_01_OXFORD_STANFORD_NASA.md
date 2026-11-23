# Data qualification audit 01 — Oxford, Stanford, NASA
Date: 2026-11-23. **Direct file inspection** for Oxford; **original eight-page article inspected** for Stanford; **live catalog inspected** for NASA. No simulation or parameter fitting performed.

## D02 — Oxford Battery Degradation Dataset 1 (local files directly inspected)
Source: https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac
Source README, 2017: Birkl / Howey. Dataset DOI and Birkl (2017) PhD thesis should be cited when data are used; retrieve canonical DOI from archive.
**File checks:** Oxford_Battery_Degradation_Dataset_1.mat ~254 MiB (MATLAB 5), top-level Cell1..Cell8; ExampleDC_C1.mat ~71 KiB (MATLAB 5), top-level ExampleDC_C1 with ch and dc; Readme.txt.
**Cell:** Kokam SLPB533459H4 740 mAh pouch, eight specimens; Binder chamber at 40 deg C; Bio-Logic MPG-205.
**Large file hierarchy:** CellX.cycYYYY.(C1ch|C1dc|OCVch|OCVdc).(t,v,q,T).
**Main characterization:** nominal 1C charge/discharge 740mA, pseudo-OCV 40mA, periodic ageing checkpoints every ~100 cycles (not necessarily every number present).
**Example file:** separate first-cycle nominal 2C charge (1480mA) and urban Artemis variable-current discharge; fields t,v,q,T,i with current mA.
**Direct observations, Cell1 cyc0000:**
- C1ch: 3510 samples; q from ~0 to +724.121 mAh; T from 41.296 to 40.114 deg C.
- C1dc: 3608 samples; q from 0 to -739.111 mAh.
- OCVch: 12803 samples; q from ~0 to +744.988 mAh.
- OCVdc: 13831 samples; q from 0 to -739.819 mAh.
- Cell1 cyc8200: C1ch 2580 samples ending +530.596 mAh; C1dc 2732 samples ending -560.650 mAh. A change of capacity with ageing is observable but these two samples **do not** establish causal ageing mechanisms.
**Direct observations, ExampleDC_C1:**
- ch: 840 samples; elapsed t 188484–189322 s; q 0–345.193 mAh; current mainly ~1483 mA; voltage 3.77971–4.19986 V; surface T 40.139–40.963 deg C.
- dc: 3145 samples; t 189322–192466 s; q 0 to -483.44 mAh; i ranges about -4998.73 to +1595.76 mA; surface T 39.927–41.087 deg C.
**Time convention:** main-file t values near 735954 are MATLAB serial datenum (days); example t is elapsed numerical seconds, not MATLAB datenum. Transform using documented provenance and verify against q-integrated current.
**Caution:** the example 2C segment contains only ~345 mAh of charging; do NOT interpret it as a full 0–100% 2C charge. Initial SOC, protocol boundaries and cell temperature sensor placement remain insufficiently documented.
**Thermal measurement qualification:** single reported T channel; chamber setpoint 40 deg C is not a time-resolved coolant boundary; no core temperature or heat flux. Heat-transfer coefficient, cell thermal mass, entropic heat and electrical resistance cannot all be uniquely identified from these signals without further assumptions/measurements.
**License:** README explicitly identifies Open Database License (ODbL 1.0) and Database Contents License 1.0. Do not commit original files to this repository without license-compliance review.
**Decision:** APPROVED as exploratory 40 deg C electro-thermal *data source* for 1C/nominal example 2C only; NOT approved as independent XFC-thermal validation or cooling-technology experiment. Formal pre-registered calibration/holdout and sampling QA still pending.

## D04 — Catenaro & Onori (2021) — original paper manually inspected
Title: *Experimental data of lithium-ion batteries under galvanostatic discharge tests at different rates and temperatures of operation*.
Data in Brief **35**, 106894. DOI: https://doi.org/10.1016/j.dib.2021.106894
Primary dataset: https://data.mendeley.com/datasets/kxsbr4x3j2/2 DOI: 10.17632/kxsbr4x3j2.2 (version 2). Data license CC BY 4.0.
**Read:** all eight pages including experimental layout, Tables 1–4, Figures 1–5, description and references; raw XLSX dataset not yet downloaded/audited.
**Cells:** six samples per chemistry: Panasonic NCR18650B NCA (3350 mAh), LG INR21700-M50 NMC (4850 mAh), A123 ANR26650m1-B LFP (2500 mAh). All graphite anodes, three different cathodes.
**Test conditions:** chamber 5, 25, 35 deg C, conditioned at least 1 hour; CC-CV charge, rest 1 h, galvanostatic **discharge**, then rest. NCA/NMC C/20, 1C, 2C, 3C, 5C; LFP additionally 10C, 15C, 20C. Discharge stops on cutoff or 75 deg C surface-T limit.
**Measurement:** Arbin LBT21024, IncuMax IC-500R chamber, center-of-cell skin Type-T thermocouple, recorded at 1-s intervals, unfiltered. Reported Arbin current-control accuracy better than ±0.02% (equipment spec, not whole temperature uncertainty).
**Figures/tables:** Table 2 step sequence and stop conditions; Table 3 chemistry-rate-temperature allocation; Table 4 signal columns and sign/step-index illustration; Figure 2 raw workbook hierarchy; Figure 5 apparatus/thermal chamber and connections. **Important nuance:** full XLSX experiment files may contain pre-discharge charge and rest phases (Table 4 shows steps 1–6), while the authors' published analysis extracts *only Step 5 discharge*. Need inspect raw zip to establish if charging transient data are in fact usable.
**Limits:** tests are specifically designed for discharge characterization, not XFC charging; charge profile manufacturer standard; skin T not core T, boundary heat flux and HTC unknown. No numerical model validated by this data article.
**Decision:** high-quality candidate for multi-chemistry/multi-rate **discharge** electrical and surface thermal verification once raw data checked; XFC charging holdout **not qualified**.

## D01 — NASA Ames
Catalog: https://data.nasa.gov/dataset/li-ion-battery-aging-datasets
**Checked 2026-11-23:** NASA catalog has description and field schema, but explicitly states **'This dataset has no data'** under Data and Resources; license **'License not specified'**. Prior landing URL https://c3.nasa.gov/dashlink/resources/133/ failed to load in this audit.
**Decision:** metadata only / access blocked through catalog. No claim that this is a currently downloadable and licensed dataset. Seek a verified authoritative download before scientific use; any secondary mirrors require independent authenticity/license review.

## Pre-implementation decision matrix
| Question | Oxford | Stanford Catenaro/Onori | NASA |
|---|---|---|---|
| Raw files currently inspected | YES (two MAT) | NO (paper only) | NO |
| Time-resolved temperature measured | YES | YES per paper | YES per metadata |
| Charging transient candidate | YES (1C, example 2C; partial example segment) | Possibly present in XLSX, not yet verified | Metadata only |
| Controlled known environment | 40 deg C chamber | 5/25/35 deg C chamber | Variable ambient metadata |
| High-rate charging thermal qualification | NO | NO | NO |
| Core temperature measured | NO evidence | NO | NO evidence |
| Reuse license identified | ODbL/DbCL 1.0 | CC BY 4.0 | Not specified |

**Next specific audit:** obtain and inspect Mendeley raw XLSX/zip signal fields + experiment step boundaries, inspect all Oxford cell/cycle consistency and missing checkpoints, obtain original thesis/manufacturer data, pre-register held-out cell and ageing checkpoints, and identify an actually measured fast-charge thermal dataset with sensor and cooling boundaries. Numerical solver remains blocked by the pre-implementation research protocol.
