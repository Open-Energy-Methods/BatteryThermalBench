# BatteryThermalBench — literature-first research programme

**Status:** research screening only. No battery model or cooling architecture is qualified for implementation.
**Initial audit:** 2026-11-23.
**Application context:** DTU TRAIN-FAST, job ID 8624. This is an independent Open Energy Methods research project, not an official DTU project.

## Research question
Which experimentally supportable electro-thermal model and cooling-system boundary conditions permit fair, reproducible comparisons of lithium-ion cell/module charging behaviour?

## Literature review policy
1. Separate primary experiments, numerical papers, reviews, data repositories and software.
2. Identify exact chemistry, cell format, charge current, SOC window, temperatures, thermal boundaries, sensor positions and test protocol.
3. For each paper record: DOI/URL; what was directly inspected; methods; validation; numerical results with context; gaps; applicability.
4. **Do not mark a paper 'full-text reviewed' unless every relevant methods, results and limitations section has been examined against original source.** Abstract-only sources are labelled *screened*.
5. Distinguish calibration data from independent test data. Validation is conditional on test envelope and observable (measured surface temperature is not measured core temperature).
6. A literature-reported cell temperature limit is not a universal runaway threshold, certification criterion, or fast-charging safety proof.
7. Check dataset licenses before redistribution. Link original sources, do not mirror by default.
8. New claims require a source-to-claim trace and a falsifiable verification/validation plan.

## Decision gates (currently unresolved)
- D0: One or more experimentally accessible cell datasets with time-resolved I, V, surface T, ambient and documented thermal boundary.
- D1: Chemistry, format, C-rate, SOC and voltage limits selected only after source assessment.
- D2: Electrical source and sign convention independently verified.
- D3: Thermal network complexity justified against thermal observability and geometry.
- D4: Fair cooling comparison includes cooling-loop duty, coolant outlet temperature, pressure loss, auxiliaries and applicable correlations.
- D5: Charging constraint formulation treats plating/degradation risks as out of scope unless specifically modeled/validated.
- D6: Leave-out tests and extrapolation labeling agreed before calibration.

## Research-only releases
- R0: literature and source audit with paper-by-paper records
- R1: dataset feasibility and identifiability assessment
- R2: pre-implementation scientific specification and validation plan
- Only then: code development

See [paper-by-paper review](PAPER_REVIEW_REGISTER.md) and [software and dataset audit](SOFTWARE_DATA_AUDIT.md).
