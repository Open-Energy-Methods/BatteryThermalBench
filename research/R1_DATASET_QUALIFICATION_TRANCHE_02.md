# R1 dataset qualification tranche 02 — source-led audit
Audit date: **2026-11-27**. This file is a **paper/documentation review**, not proof that all source data were downloaded or executed. The Oxford structural QC and pre-registered holdout proposal are in `R1_OXFORD_QC_AND_HOLDOUT_PROTOCOL.md`.

## Research decision — new priority
**Highest priority now:** actual high-rate *charge* plus measured spatial-temperature data from the 2026 A123 LFP pouch study. This evidence is a better candidate for validating temperature nonuniformity than Oxford single-point, 40°C, largely 1C characterization. Do not treat author-reported model accuracy as our independent reproduction.

### R1-D05: High-power LFP pouch-cell thermal data (2026) — **priority A / raw data not yet locally inspected**
- Paper: *Electrochemical–thermal modelling of high power Li-ion pouch cells*, Journal of Power Sources (2026), DOI **10.1016/j.jpowsour.2025.238764**.
- Original public GitHub: https://github.com/Battery-Intelligence-Lab/pouch-cell-thermal ; checked repository README directly through GitHub connector.
- Companion Oxford repository: https://doi.org/10.5287/ora-eonzaxjpm .
- Original README: `Expivium.mat` is N x 4: sample, voltage (V), current (A), mean temperature (°C). `ExpIR.mat` is Ny x Nz x N: spatial infrared surface temperatures (°C), single precision.
- Runs explicitly listed: **constant-current 2C, 4C, 6C, 8C, 10C in both charge and discharge**, plus 2C/4C 100-second and 8C 50-second square pulses at 30%, 50%, 70% SOC.
- **Source QC warning from maintainers:** 1C CC data omitted due to bad camera calibration.
- Paper reports **~15 mV voltage RMSE and 0.35°C temperature RMSE at 10C charge on an independent validation dataset**; these are *authors' reported scores*, not our results.
- **Open:** downloadability, raw matrix dimensions and completeness, camera calibration/registration, emissivity, response time, true ambient/cooling boundaries, full SOC intervals, dataset license, independent holdout independence, how 10C was constrained.
- Decision: strongest direct cell-level XFC thermal candidate; qualify original MAT arrays and thermal conditions **before** model choice. Not validated for cooling architectures by itself.

### R1-D06: Chen et al. LG M50 validation data (2020) — **priority B / exact file URLs found**
- Zenodo version DOI **10.5281/zenodo.4032561** (concept DOI **10.5281/zenodo.4032560**): https://zenodo.org/records/4032561
- Files: `LGM50_cell02.csv` (597.7 kB, md5 0bbf959cbfc367296ec69d7a74d2f5c1), `LGM50_cell03.csv` (590.8 kB, md5 a09cbd8eff0af55dfe9bc8728fa89908), `LGM50_cell04.csv` (596.0 kB, md5 f17615476283d2e15087165697ff9d7c); three commercial LG M50 cells, approximately 1.8 MB.
- Original publication: Chen et al., J. Electrochem. Soc. **167** 080534 (2020), DOI **10.1149/1945-7111/ab9050**.
- Dataset metadata: CC-CV charge; C/10, C/2, 1C, 1.5C discharge; measured current, voltage, cell surface temperature and thermal chamber temperature. CC BY 4.0.
- An exact CSV could be viewed through indexed web retrieval. **No bytes were successfully downloaded to the execution environment**: a container download attempt failed. No signal QC or actual cell-level holdout performed.
- Decision: promising low/moderate rate cell-and-chamber thermal validation complement, NOT independently evidenced continuous XFC.

### R1-D07: Khan et al. 2025 high-power NMC P42A data — **priority A for pulse/ECM; NOT 8C continuous charge**
- Paper: *High-power lithium-ion battery characterization dataset for stochastic battery modeling*, Scientific Data 12:1506 (2025), DOI **10.1038/s41597-025-05725-y**.
- **Primary full-text HTML reviewed:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12394511/ . The paper reports 45 initially screened, 12 Molicel INR-21700-P42A cells selected for detailed tests; 10 representative plus 2 outliers. NMC cathode, graphite–Si anode, 4.2 Ah nameplate.
- Phase 2: chamber setpoints 5°C, 25°C, 40°C; discharge/charge characterization, EIS and high-C-rate GITT/pulse testing **0.5C, 1C, 2C, 3C, 6C, 8C** in both directions, at specified SOC points. **8C pulses are not full continuous 8C charge**.
- XLSX Phase 2 fields: `Test_time(s)`, `Voltage(V)`, `Current(A)`, `Aux_Temperature(°C)` (cell surface). Current positive for charge and negative for discharge. EIS XLSX fields `Freq`, `Zmod`, `Zphz`.
- **Important authors' reported experimental QC:** at the 5°C EIS setpoint ~20% of runs were actually 8–10°C due to imperfect chamber regulation. Do not label these as exactly 5°C validation.
- Original OSF data: **10.17605/OSF.IO/9CEAV** (paper has accompanying plotting scripts). XLSX files not downloaded or programmatically inspected in this tranche; raw dataset license requires checking.
- Decision: compelling source for SOC/T/rate-dependent pulse impedance and cell variability; **only transient thermal/pulse claim**, not full-charge XFC or cooling benchmark.

### R1-D08: 36-cell pack cycling with temperature sensors (2025) — **priority B for module**
- Paper: *Lithium-Ion Battery Pack Cycling Dataset with CC-CV Charging and WLTP/Constant Discharge Profiles*, Scientific Data 12:1942 (2025), DOI **10.1038/s41597-025-06229-5**.
- Primary data record: https://doi.org/10.34810/data2395 , CORA Dataverse (v3 located); parquet format.
- Published description: CC-CV charge and WLTP/constant-discharge operation, 36 cells, multiple temperature measurement points and controlled environment.
- Dataset page and full-text article inaccessible in direct review; individual Parquet metadata, thermal sensor mapping, charging C-rate and license **not independently checked**.
- Decision: module thermal gradients/pack variation candidate; **not currently qualified for fast charging or cooling comparison**.

### R1-D09: Core & surface measured LG M50 dataset (2026) — **priority B for core/surface network**
- Paper: *Dataset of internal temperature during lithium-ion battery ageing*, Data in Brief (2026), DOI **10.1016/j.dib.2026.113403**.
- Original Mendeley v2: https://data.mendeley.com/datasets/bf6fksxpp2/2 , DOI **10.17632/bf6fksxpp2.2**, CC BY 4.0; landing page checked.
- Authors' data description: 6 LG INR21700 M50 cells (3 pristine, 3 instrumented with **embedded core thermocouples**), ageing over 550 cycles, 45-minute real urban drive cycle characterization; related article DOI **10.1016/j.est.2022.105260**.
- Raw files not downloadable through the retrieved Mendeley HTML. Sensor installation may modify core thermal behavior; original core thermocouple calibration and test protocol are required.
- Decision: excellent possible check for 2-node core/surface network; not evidence of ultra-fast charging, need raw data and instrument perturbation assessment.

### R1-D10: Cell cooling-coefficient experiment (2022) — **priority B for thermal boundary**
- Dataset: https://zenodo.org/records/6421061 , *Cell Cooling Coefficient Data for Base Cooled LG M50T & Samsung 30Q*, DOI **10.5281/zenodo.6421061**.
- Index reports original dataset `M50.zip` ~90 MB; full record/detail not accessible in this pass (Zenodo 429).
- Decision: promising physical thermal-boundary benchmark, requires primary paper, file license/sensor data and experimental geometry audit.

### R1-D11: Stanford Catenaro & Onori (2021) — status unchanged
- Data in Brief 35, 106894, DOI 10.1016/j.dib.2021.106894; dataset https://data.mendeley.com/datasets/kxsbr4x3j2/2 .
- Eight-page original user-supplied PDF already reviewed separately. Full workbook files remain **not downloaded**. Six-step testing includes CC-CV/rest/discharge/rest, but *whether all steps are retained in deposited workbooks remains unconfirmed*.
- Do not reclassify discharge profiles as fast-charge experiments.

## Evidence/claim ladder
- Metadata inspected: title, abstract, repository listing only.
- Primary methodology inspected: experimental protocol, sensor definitions, source limitations (paper).
- Raw source inspected: actual files opened and checked (NOT achieved for D05–D11 this tranche).
- Independent reproduced: our software reproduces source physical/numerical measurements (NONE).
- Qualified continuous XFC & cooling architecture performance: **NONE**.

## Proposed pre-registered validation partitions (no model built)
1. **High-rate spatial temperature:** D05 pulse/2C/4C training, **independent 6C/8C/10C holdouts** only if paper partitions and sensor uncertainty permit. If paper uses same data for fit, pick separately untouched conditions and report domain extrapolation explicitly. Record geometry/pixel mask/airflow/IR uncertainty.
2. **High-rate pulse ECM:** D07 train on specific cells and SOC/temperature subsets, reserve selected entire *cells* and temperature windows for unseen tests; preserve two author-designated outliers as explicit stress tests.
3. **Two-node thermal gradient:** D09 core/surface data may verify internal lag only after probe modification, temperature uncertainties and usable raw files are confirmed; D05 spatial IR is **surface**, not core.
4. **Module:** D08 separate train and holdout entire pack cycle sessions; repeated time samples are not independent statistical units.
5. **Cooling:** do **not** infer comparative cooling performance from D05/D07; obtain measured flow, temperature, boundary duty and pressure drop for each coolant architecture.
6. **Model selection:** resist the urge to build Rint/1RC/2RC or DFN before verifying actual charge/current, entropic data and geometries; consider PyBaMM baseline and reuse source author models when licensed.

## Decision
Literature/data acquisition progressing. **R1 gate remains NOT PASSED** until at least one candidate high-rate charging dataset is opened locally, physically screened, its test envelope documented, and its independent validation partition fixed. This finding supports **changing dataset research priorities**, not claiming completed battery model validation.
