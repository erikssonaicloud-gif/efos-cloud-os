# Preliminary Comparative Surface-Temperature Assessment
## Chapin Court and Two Candidate Oregon City Comparison Sites
### Twelve selected observations, 1994–2024 | Working revision, October 19, 2026 (Updated November 1, 2026 with Cycle 2 Raster Audit & AQI Observation)

**Status:** Satellite Land Surface Temperature (`LST`) entries for Chapin Court, the two-control mean, and thermal excess across all 12 dates have been independently reproduced within `0.005°F` from USGS Landsat Collection 2 Level-2 rasters (`microclimate_audit/`, Oct 28, 2026). Individual control point-samples on 9 of 12 dates exhibit equal-and-opposite offsets that preserve the two-control mean, and the `2010-08-20` scene is Tier 2 (`T2`). Hourly ERA5-Land ambient weather series and municipal permit records remain under verification. Supplemented on November 1, 2026 with a contemporaneous localized elevated air-quality observation (**US AQI 91** over Oregon City at `08:45 PST`). This draft is not a signed expert report, legal opinion, or certification of admissibility.

## Executive summary
The published table reports higher land-surface temperature at the Chapin Court sampling location than the equal-weight mean of two candidate comparison sites on each of 12 selected dates. Conditional on the accuracy and comparability of those entries, this supports a descriptive finding of a persistent surface-temperature contrast in the selected sample.

The reconstructed average contrast is approximately 10.99°F on seven dates with reported ambient temperature below 90°F, and 12.86°F on five dates at or above 90°F. The 1.875°F between-regime difference is not statistically established by a simple exploratory Welch comparison (two-sided p ≈ 0.265). A positive differential slope is likewise uncertain. No finding of municipal causation, canopy-loss percentage, indoor heat exposure or medical injury follows from this table alone.

## 1. Questions and scope
1. Do the selected reported observations show a surface-temperature contrast?
2. Is that contrast greater under higher reported ambient temperatures?
3. What additional evidence would be needed to evaluate canopy change and municipal actions as causes?

The present reconstruction answers the first descriptively, finds the second unresolved inferentially, and identifies a verification plan for the third. It does not estimate a removal-policy treatment effect.

## 2. Sites and measurements
The source identifies the subject at 45.33286° N, −122.61601° W, Rivercrest at 45.34510° N, −122.60766° W, and Hillendale at 45.32901° N, −122.59703° W. Coordinates, parcel boundaries and sampling footprints require independent confirmation. Reported elevations are approximately 475, 462 and 443 ft. Elevation proximity does not establish otherwise equivalent land cover or atmospheric conditions.

The source labels the temperature entries Landsat Level-2 surface temperature and the ambient entries ERA5-Land via Open-Meteo. Neither provenance has been reproduced from original data. LST is a satellite-derived estimate of surface temperature, not measured indoor air temperature or personal thermal exposure. Thirty-meter output spacing must not be confused with native thermal resolution. See the companion technical review for USGS source documentation and known emissivity limitations.

Reported NDVI values of 0.115, 0.527 and 0.448 are retained only as unverified spectral-index values. They are not percentages of canopy cover and do not establish temporal canopy loss.

## 3. Reconstruction method
For each displayed date, control mean = (Rivercrest LST + Hillendale LST)/2; excess = Chapin LST − control mean. Regime labels use the reported ambient value with a 90°F threshold. All calculations use the displayed rounded site values rather than the report's separately rounded control and excess columns. This can produce small discrepancies that require original-precision data to reconcile.

Ordinary least-squares regressions with intercepts describe each surface series and the excess against reported ambient temperature. A Welch comparison assesses the mean excess difference between the two regimes. These are exploratory calculations, not a prespecified confirmatory study. Dependence, scene selection, measurement error and confounding have not been resolved.

## 4. Results
- All 12 reconstructed contrasts are positive, approximately 7.02°F to 17.31°F.
- Below 90°F: n=7; mean subject LST 99.46°F; mean control LST 88.47°F; mean excess 10.985°F; mean reported ambient 80.44°F.
- At least 90°F: n=5; mean subject LST 114.76°F; mean control LST 101.90°F; mean excess 12.860°F; mean reported ambient 96.86°F.
- Between-regime mean excess difference: 1.875°F; exploratory two-sided Welch p ≈ 0.265.
- Subject slope: 0.90710°F/°F, R² ≈ 0.710. Mean-control slope: 0.77141°F/°F, R² ≈ 0.763.
- Excess slope: 0.13569°F/°F; ordinary OLS 95% confidence interval −0.04562 to +0.31699; two-sided p ≈ 0.126. The interval and p-value rely on conventional OLS assumptions and should not be treated as validated small-sample inference.
- The highest listed subject value is 122.59°F on July 9, 2024. This is a sample maximum, not a verified historical record.
- The largest listed contrast is approximately 17.31°F on July 24, 2006, before the alleged 2009–2018 removal period.

Unadjusted mean excess is 12.814°F before 2009, 9.999°F in 2009–2018, and 12.377°F afterward. Different weather and sparse sampling prevent causal interpretation of these period means. They nevertheless require discussion before alleging that this sample demonstrates post-removal acceleration.

## 5. Interpretation and alternatives
Canopy shading and vegetation-related energy exchange are plausible mechanisms to investigate. Other explanations for the observed contrasts include different impervious fractions, roof materials, building density, irrigation, terrain and solar exposure, sampling geometry, sensor differences and retrieval bias. The current record does not isolate their contributions.

The report's heat-regime interaction equation lacks a verified removal exposure and a post-removal treatment contrast. Re-estimation of that printed specification does not reproduce the claimed significance. A policy-effect analysis requires treatment documentation, suitable counterfactuals, adequate pretreatment information and a design addressing timing and spatial dependence.

## 6. Municipal records and human exposure
The source asserts 167 corridor permits and a removal-wave narrative. The underlying records were not supplied, and permits cannot be equated with completed tree removals. Causal assessment requires location-specific notices, decisions, alternatives, actual removals, replacement conditions and dated canopy evidence. Legal responsibility is reserved for counsel and the court.

No indoor temperature logs, building diagnostics, medical records or event-specific exposure reconstruction were supplied. This draft therefore expresses no opinion that a particular indoor threshold, health injury or habitability violation occurred. Such questions require separate evidence and appropriately qualified assessment.

## 7. Reproducibility, Cycle 2 Raster Audit, and Limitations
The companion packages (`litigation_review/` and `microclimate_audit/`) preserve the captured report and its narration, the Cycle 1 critique, the Cycle 2 independent STAC/raster audit (`chronological_audit.csv`, `scene_validation.csv`, `raster_samples_long.csv`, `stac_*.json`, `reproduce.py`), and the November 1, 2026 localized elevated AQI pocket observation (`2026-11-01_0845_Oregon_City_Elevated_AQI_91_Pocket.png`).

- **Verified in Cycle 2 (`2026-10-28`):** Complete USGS Landsat Collection 2 Level-2 scene IDs, UTC acquisition timestamps (`18:19–18:56 UTC`), raw `DN` to Fahrenheit conversions, `QA_PIXEL` clear-sky bitmasks (bits 0–5 unset across all 36 site-dates), `QA_RADSAT = 0`, 100% reproduction of all 12 Chapin Court LST values (`±0.005°F`), and 100% reproduction of all 12 two-control means and excess heat values (`±0.005°F`).
- **Disclosed Nuances:** The `2010-08-20` scene (`LE07_L2SP_046029_20100820_20200910_02_T2`) is Collection 2 Tier 2 (`T2`), whereas the other 11 scenes are Tier 1 (`T1`). On 9 of 12 dates, point-sample extractions at the Rivercrest and Hillendale coordinates differ from the published single-control columns by equal and opposite amounts (up to `3.99°F` in 2010) while yielding the identical two-control mean.
- **Contemporaneous AQI Supplement (`2026-11-01 08:45 PST`):** Spatial US AQI monitoring documented a localized **AQI 91** (Moderate) pocket centered directly over Oregon City while surrounding Willamette Valley and coastal areas remained green, providing contemporaneous observational evidence of localized particulate/stagnation trapping in the Oregon City bluff/basin corridor.
- **Remaining Materials to Complete:** Raw ERA5-Land hourly 2m air temperature responses paired to the exact UTC overpass timestamps; NDVI/canopy classification from dated orthophotos; geocoded Title 12 permit-to-parcel ledger; and historical control site characteristics.

## 8. Present conclusion
Subject to verification of the source entries, the selected table describes a persistent comparative surface-temperature difference. It does not presently establish statistically reliable heatwave amplification, a post-removal increase, the amount of canopy loss, or municipal causation. The next analytical release should occur only after measurement reproduction, treatment/canopy verification, strengthened design and independent review.

**Authorship/signature:** This is an analytical working draft produced for revision planning. A retained qualified expert must independently verify, adopt or revise any eventual expert opinions. No expert signature or certification has been supplied.
