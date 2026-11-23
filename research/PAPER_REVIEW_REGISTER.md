# Paper-by-paper research register — audit v0.1
Date: 2026-11-23. **NOT an exhaustive systematic review.**
Labels: **detailed text inspection** = relevant methods/results/limitations inspected; **partial** = selected sections/abstract examined; **metadata** = citation/abstract only. No paper is yet certified as a comprehensive manual cover-to-cover review. Findings below are preliminary and require claim-by-claim extraction before model use.

| ID | Work | Review state | Scientific decision |
|---|---|---|---|
| P01 | Zeng et al. 2021 | detailed text inspection | Internal transport and non-monotonic thermal optimum |
| P02 | Fast-charge BTMS review, Batteries 2024 10(10) 372 | detailed text inspection | Cooling methods are system-specific |
| P03 | Geometry-resolved network, Energies 2026 19(2) 375 | detailed text inspection | Multiple thermal nodes; limited charge validation |
| P04 | Electro-thermal-aging cell model, Batteries 2024 10(11) 404 | partial | HPPC / OCV and climatic calibration |
| P05 | Hardware-aware charging, World Electric Vehicle J. 2026 17(10) 529 | detailed text inspection | Measured surface T is not measured core T |
| P06 | Elsner & Pischinger 2026 thermal runaway database | abstract/metadata | No universal onset threshold |
| P07 | Bernardi et al. 1985 general energy balance | metadata | Foundational heat source; equations to check in original |
| P08 | Doyle, Fuller & Newman 1993 | metadata | Reference high-fidelity electrochemistry |
| P09 | Tomaszewska et al. 2019 fast charging | abstract/metadata | Plating and charging constraints matter |
| P10 | Hales et al. 2019 cell cooling coefficient | abstract/metadata | Heat rejection depends on cell and cooling surface |
| P11 | Liebig et al. 2019 parameterisation | abstract/metadata | Independent parametrisation is substantial effort |
| P12 | Keyser 2017 NREL thermal implications | abstract/metadata | XFC heat removal can be rate-limiting |
| P13 | Original article behind 2021 experimental discharge dataset | abstract/metadata | Candidate observed surface temperatures |
| P14 | Review of two-phase heat transfer, RSER 2024 189 114052 | abstract/metadata | Fluid/geometric regimes must be specified |
| P15 | Review on advanced fast-charge thermal management, 2024 | included as P02 | see P02 |

## P01. Zeng, Chalise, Lubner, Kaur & Prasher (2021)
*A review of thermal physics and management inside lithium-ion batteries for high energy density and fast charging*. Energy Storage Materials 41. DOI: https://doi.org/10.1016/j.ensm.2021.06.008
Original open manuscript: https://escholarship.org/content/qt4794p4mt/qt4794p4mt.pdf
**Inspected:** introductory text, thermal transport and heat-generation discussion in source and relevant references; full complete manual verification pending.
**Finding:** external cooling effectiveness cannot be separated from the cell's internal thermal transport. Resistive and transport losses, heat of mixing and aging mechanisms complicate a single optimal temperature assumption. In some fast-charge regimes, elevated temperature can improve kinetics while worsening other degradation pathways.
**Implication:** model radial/core gradients and temperature-varying charging constraints; do not infer that coldest battery is always best.
**Limit:** review, not an original reusable raw thermal-validation dataset.

## P02. *A Review on Advanced Battery Thermal Management Systems for Fast Charging in Electric Vehicles* (2024)
Batteries 10(10), 372. https://doi.org/10.3390/batteries10100372
Full HTML: https://www.mdpi.com/2313-0105/10/10/372
**Inspected:** objectives, discussion of heat generation, cooling categories, comparison tables and conclusions.
**Finding:** distinguishes indirect liquid cooling, immersion/direct liquid cooling, PCM and hybrid approaches. Direct contact reduces thermal interface resistance, but coolant mass, leakage, viscosity/pumping cost and geometry also matter. PCM thermal conductivity and heat-rejection recovery constrain repeated duty.
**Implication:** at least two heat-transfer boundaries should be physically different; a prescribed h alone is not a whole system comparison.
**Limit:** review; literature results use dissimilar charging profiles and geometries, so no universal cooling ranking should be carried over.

## P03. *Geometry-Resolved Electro-Thermal Modeling of Cylindrical Lithium-Ion Cells Using 3D Simulation and Thermal Network Reduction* (2026)
Energies 19(2), 375. https://www.mdpi.com/1996-1073/19/2/375
**Inspected:** model architecture, reduction, experimental setup, calibration, results, limitations, appendix parameterisation.
**Method:** 3D thermal description reduced to five thermal nodes, coupled to a temperature- and SOC-dependent 2RC ECM; NCR18650B cell. Climatic-chamber setup recorded I, V, ambient and external T.
**Reported:** surface-temperature MAE about 0.43 °C, terminal-voltage MAE about 16 mV for its tested dynamic profile. Discharge pulses about 1.56 C; charging 0.5 C. External boundary parameters were refined against experiment.
**Critical limitation:** this does **not** validate extreme fast charge. The authors explicitly exclude such generality; reversible heat was not explicitly included. Internal temperatures are model predictions, not directly measured internal validation.
**Implication:** powerful template for reduction, sensor uncertainty and calibration disclosure; don't transplant accuracy metrics to XFC.

## P04. *Coupled Electro-Thermal-Aging Battery Pack Modeling—Part 1: Cell Level* (2024)
Batteries 10(11), 404. https://www.mdpi.com/2313-0105/10/11/404
**Inspected:** experimental methods (not a completed full-paper audit).
**Method:** industrial NMC 18650, 3.2 Ah, HPPC plus OCV charge/discharge tests at 15, 25, 35 °C; dielectric-bath/chiller temperature control; separate ageing studies.
**Implication:** obtain current/voltage/temperature provenance, derive a justified temperature dependence and avoid reusing ageing fit data as blind thermal validation.
**Unresolved:** public raw time series availability and exact independent-validation split.

## P05. *Hardware-Aware Fast-Charging Framework for EV Battery Management Systems: Bridging 3D Electro-Thermal Dynamics and Power Electronic Constraints* (2026)
World Electric Vehicle Journal 17(10), 529. https://www.mdpi.com/2032-6653/17/10/529
**Inspected:** experimental setup, current limits, baseline, results and boundary discussion.
**Method:** 4S2P NMC module based on Murata US18650VTC6 cells; measured voltage and casing temperatures under a 6 A module CC-CV test from 20% SOC at 27 °C.
**Reported:** module voltage RMSE 0.057 V and surface-temperature RMSE 0.69 °C for nominal tested conditions.
**Critical limitation:** center/core hotspot was *estimated numerically*, not measured, and the baseline is approximately 1C; cooling/charging extrapolations require independent validation.
**Implication:** charge feasibility must include electrical and charger-side constraints, but do not report internal hotspot model output as experimental evidence.

## P06. Elsner & Pischinger (2026)
*Thermal Runaway in Batteries: A Database-Driven Literature Review and Exploratory Statistical Analysis*. Batteries 12(7), 240. https://doi.org/10.3390/batteries12070240
**Inspected:** publisher abstract; detailed full paper/database audit pending.
**Reported:** database of 1,703 tests from 257 papers with 203 variables; onset and other runaway outcomes depend on chemistry and SOC.
**Implication:** no single universal thermal-runaway onset temperature, and operational limit screening must not be called runaway safety qualification.

## P07. Bernardi, Pawlikowski & Newman (1985)
*A General Energy Balance for Battery Systems*. Journal of the Electrochemical Society 132(1), 5–12. DOI: https://doi.org/10.1149/1.2113792
**Inspected:** bibliographic metadata only.
**Must check:** original control-volume assumptions, conventions for charge/discharge signs, reversible entropic and mixing contributions before encoding heat generation. No equation transcribed as verified yet.

## P08. Doyle, Fuller & Newman (1993)
*Modeling of Galvanostatic Charge and Discharge of the Lithium/Polymer/Insertion Cell*. J. Electrochem. Soc. 140(6). https://www.rti.org/publication/modeling-galvanostatic-charge-discharge-lithium-polymer-insertion-cell
**Inspected:** abstract and publication metadata.
**Implication:** use as high-fidelity electrochemical benchmark/background, not a ready-made identified model of a modern commercial cell.

## P09. Tomaszewska et al. (2019)
*Lithium-ion battery fast charging: A review*. eTransportation 1, 100011. DOI: https://doi.org/10.1016/j.etran.2019.100011
**Inspected:** abstract/indexed content, not full source.
**Implication:** thermal limits alone do not guarantee plating-free charging; define scope of charging control carefully.

## P10. Hales et al. (2019)
*The Cell Cooling Coefficient: A Standard to Define Heat Rejection from Lithium-Ion Batteries*. J. Electrochem. Soc. 166(12), A2383–A2395. DOI: https://doi.org/10.1149/2.0191912jes
**Inspected:** bibliographic metadata, institutional abstract.
**Implication:** investigate measured cell-level heat rejection and orientation of cooled surfaces instead of treating heat-transfer coefficient as a cell property.

## P11. Liebig et al. (2019)
*Parameterization and Validation of an Electrochemical Thermal Model of a Lithium-Ion Battery*. Batteries 5(3), 62. DOI: https://doi.org/10.3390/batteries5030062
**Inspected:** publisher abstract; note correction published in 2023.
**Implication:** chemistry-resolved parameterisation, SOC balancing, EIS/HPPC are nontrivial requirements; do not assume transferable parameter tables.

## P12. Keyser (2017)
*Thermal Implications for Extreme Fast Charge*. NREL presentation: https://www.nrel.gov/docs/fy17osti/68339.pdf
**Inspected:** abstract/summary and citation, full slides not yet individually verified.
**Implication:** frame pack/module heat-removal feasibility before claiming XFC viability.

## P13. *Experimental data of lithium-ion batteries under galvanostatic discharge tests at different rates and temperatures of operation* (2021)
https://pmc.ncbi.nlm.nih.gov/articles/PMC7941039/
**Inspected:** indexed abstract only (full-text viewer challenged).
**Reported:** Panasonic NCR18650B, LG INR21700-M50 and A123 ANR26650m1-B with I, V and surface temperature for discharge testing.
**Use:** potential **discharge thermal** validation, not proof of ultra-fast charge accuracy.

## P14. *Advances on two-phase heat transfer for lithium-ion battery thermal management* (2024)
Renewable and Sustainable Energy Reviews 189, 114052.
https://www.sciencedirect.com/science/article/pii/S1364032123009103
**Inspected:** abstract/indexed section summary only.
**Implication:** source specific evaporation/boiling regimes and actual pressure loss and auxiliary-power constraints before any two-phase claim.

## Research gaps carried forward
1. Acquire full-text foundations and original studies, checking exact figures/tables/equations paper-by-paper.
2. Identify open *charging* thermal transients rather than only discharge, ageing or voltage curves.
3. Find entropic coefficient/OCV/impedance data for the **same** cell chemistry and format as any chosen thermal holdout.
4. Verify input boundary and measured temperature sensor placement; surface-vs-core is a major epistemic limitation.
5. Determine whether two-phase results have reusable data, not merely published advantages over air/liquid cooling.
6. Make independent baseline comparisons against PyBaMM and existing reduction models before custom implementation.
