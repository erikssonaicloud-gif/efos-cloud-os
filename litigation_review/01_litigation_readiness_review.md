# Forensic Microclimate Report — Litigation Readiness Review
## Cycle 1 (Oct 19, 2026) + Cycle 2 Raster Audit & Nov 1, 2026 AQI Update | Working technical critique, not an expert certification

> **Cycle 2 & Nov 1, 2026 Update:** On October 28, 2026 (`microclimate_audit/`), Gate 1 satellite raster verification was executed against USGS Landsat Collection 2 Level-2 scenes via the Microsoft Planetary Computer STAC API. All 12 Chapin Court LST values, all 12 two-control averages, and all 12 thermal excess differentials reproduced within `0.005°F`, with all 36 `QA_PIXEL` samples clear (`bits 0–5 = 0`) and `QA_RADSAT = 0`. Two nuances were identified and disclosed: (1) the `2010-08-20` scene is Collection 2 Tier 2 (`T2`) while the other 11 scenes are Tier 1 (`T1`); and (2) on 9 of 12 dates, individual point-sample control values (`Rivercrest` and `Hillendale`) differ from the published single-control columns by equal and opposite amounts (up to `3.99°F` in 2010), leaving the two-control mean and excess heat unchanged. Additionally, on November 1, 2026 (`08:45 PST`), a contemporaneous localized elevated AQI pocket (**US AQI 91**) centered over Oregon City was archived (`2026-11-01_0845_Oregon_City_Elevated_AQI_91_Pocket.png`). See `03_cycle2_raster_audit_and_aqi_supplement_2026-11-01.md` for full details.

### Executive assessment
The report presents a testable local-heating hypothesis, a readable comparison table, candidate controls and a potentially relevant municipal-record theory. It is not presently a demonstrated causal analysis or a certified litigation-ready expert report. The supplied prior review is useful as a list of leads, but its endorsements of statistical significance, matched-control adequacy and a coherent proven causal chain are not established by the materials inspected.

This review inspects all 16 slides, embedded narration, and the supplied prior review; reconstructs the 12-row table; recalculates descriptive statistics and ordinary least-squares diagnostics; and consults primary technical documentation and governing rule texts. No raw satellite rasters, scene metadata, weather responses, permit files, canopy classifications, indoor logs, expert credentials or case pleadings were supplied. “Verified” below means verified against the displayed table or retrieved documentation, not independent validation of underlying measurements. The linked website has not been changed.

## 1. Immediate correction priorities

### P0 — Withdraw unsupported significance and causation assertions
Using the two displayed control-site temperatures to reconstruct their equal-weight mean:

| Quantity | Recalculation | Interpretation |
|---|---:|---|
| Below-90°F observations | 7 | Seven selected overpasses, not all normal summer days |
| At-least-90°F observations | 5 | Classification uses the reported ambient values, not a validated heatwave event definition |
| Below-90°F mean excess | 10.985°F | Supports the descriptive rounded value +10.99°F |
| At-least-90°F mean excess | 12.860°F | Supports the descriptive value +12.86°F |
| Between-regime difference | 1.875°F | Not a 12.86°F incremental heatwave effect |
| Welch two-sided test of excess, between regimes | p ≈ 0.265 | Does not reproduce p < 0.01 for widening of the gap |
| Chapin slope versus ambient | 0.90710°F/°F; R² ≈ 0.710 | Slope reproduces; reported R² = 0.88 does not |
| Mean-control slope versus ambient | 0.77141°F/°F; R² ≈ 0.763 | Approximately reproduces slope, not reported R² = 0.91 |
| Excess slope versus ambient | 0.13569°F/°F | Positive point estimate only |
| Excess-slope test | p ≈ 0.126; 95% CI −0.04562 to +0.31699 | Does not support a statistically established positive differential slope |
| Printed site-fixed-effect model, ordinary OLS | interaction ≈ 2.637°F; p ≈ 0.423 | Refit of the equation as printed does not reproduce asserted significance |

All tests are exploratory diagnostics on rounded transcribed values. The Welch comparison and the continuous excess-slope test address different hypotheses. The printed-model refit uses 36 site-date rows, but these are not 36 independent weather events; shared-date dependence makes conventional OLS standard errors unsuitable as a final inferential basis. None of these calculations establishes absence of a real canopy effect. An author may have used other data or specifications, but those must be disclosed before the published p-values can be defended. A small p-value for Chapin being warmer than controls would not establish widening under heat or municipal causation.

Action: remove “statistically proven,” “p < 0.01,” “disproves,” “proximate cause,” “admissible,” and “withstands challenges” unless accompanied by an appropriate disclosed analysis or court determination. Correct narration as well as visible slides.

### P0 — Fix the causal design
The printed model includes site effects, ambient temperature and Chapin × HeatWave, but no removal treatment, post-removal indicator or event-time term. It is a heat-regime interaction model, not a removal-policy difference-in-differences design. It cannot identify the effect of the alleged 2009–2018 removal program.

Counterevidence must be addressed: the largest displayed differential occurs in 2006, before the alleged removal wave. Unadjusted period means are 12.814°F before 2009 (n=5), 9.999°F during 2009–2018 (n=4), and 12.377°F afterward (n=3). The post-minus-pre contrast is approximately −0.437°F. These sparse, weather-unbalanced samples do not estimate a causal treatment effect, but they contradict a simple claim that the displayed table itself demonstrates post-removal widening.

Proposed next design, only after treatment records are verified: estimate a date-fixed-effect/site-fixed-effect model with a defined treated × post term, and optionally treated × post × heat-regime plus its necessary lower-order terms. Identify whether the estimand is parcel-specific canopy change, a corridor removal program, or heat sensitivity; these are not interchangeable. A 10-year removal window is not a single intervention date. Use verified removal dates or measured canopy-loss intensity where feasible. Prespecify eligibility, exclusion criteria and controls; inspect pretrends, differential development, spillovers and treatment contamination. Do not treat date clustering, bootstrap resampling or adding interpolated pixels as a cure for one treated neighborhood and two controls. Obtain methods review and substantially broader independent observations before confirmatory inference.

### P0 — NDVI is not percent canopy cover
NDVI is a dimensionless spectral ratio, not the percentage of an area occupied by tree canopy. Delete “11.5% canopy,” “52.7% canopy,” “44.8% canopy,” and “78.2% shade loss.” The arithmetic relative difference between 0.115 and 0.527 is not measured canopy loss, especially not change over time. Vegetation also includes lawns and other non-tree cover. Preserve the values only as unverified reported NDVI values pending sensor/date/geometry and processing disclosure. Estimate actual canopy fractions from validated imagery classification or a suitable canopy product, with acquisition dates, season, uncertainty and reference labels. [S3]

### P0 — Surface temperature is not personal exposure
Call the satellite product land-surface temperature (LST), not measured indoor temperature, mean radiant temperature, heat index or a human thermal dose. It represents an observed/resampled surface footprint at acquisition time. It does not independently establish nighttime heat, indoor habitability, medical injury or a universal 120°F injury threshold. “100% of incoming irradiance becomes sensible heat” is physically incorrect: shortwave reflection, net longwave exchange, storage, ground heat flux, sensible heat and latent heat must be considered. Replace it with a qualified mechanism hypothesis rather than a numerical energy allocation. [S1]

## 2. Remote-sensing and weather validation

1. **Acquire actual products.** The listed scene strings are prefixes, not full Collection 2 product identifiers. Obtain complete product IDs, processing dates, collection/tier, MTL acquisition UTC, platform/sensor, processing version and raw archive URLs. Verify each acquisition exists, contains the target and controls, and has valid ST data.
2. **Distinguish grid spacing from sensor information.** USGS lists native thermal resolution of 120 m for Landsat 5, 60 m for Landsat 7 and 100 m for Landsat 8/9, with resampling to a 30 m grid. A 30 m product cell does not establish independent 30 m thermal detail or isolate an individual roof. Show a scale map, thermal footprints and mixture of roads, roofs, lawns and trees. Use consistent geometry and sensitivity tests for pixel selection, buffers and registration. [S2]
3. **Audit the particularly relevant emissivity issue.** USGS documents a vegetation-adjustment anomaly that can produce erroneous ST where NDVI changed significantly between ASTER and Landsat eras. Because vegetation change is the proposed treatment, this is a targeted potential bias, not a generic footnote. Check the current product status, acquisition-specific metadata, QA and effect of plausible alternative emissivity handling; do not assume the anomaly affected these pixels or that it has already been corrected. [S1]
4. **Quality masks and uncertainty.** Archive QA_PIXEL, saturation and applicable ST QA, cloud-distance and emissivity layers. Specify how cloud/shadow/cirrus, fill, cloud adjacency and low-quality retrievals were rejected for every site. The claim “<0.1% cloud cover over target pixel” needs a defined metric. Scene-level cloud percentage does not establish local validity. Audit post-2003 Landsat 7 SLC-off gaps, including the four displayed 2006–2015 Landsat 7 observations. Report instrument/retrieval and spatial representativeness uncertainty, not two decimal places as implied accuracy. [S1, S2]
5. **Reproduce conversion.** USGS Collection 2 scaling is Kelvin = DN × 0.00341802 + 149.0; then °F = (K − 273.15) × 9/5 + 32. Record ST band, fill rules and whether software had already scaled the values. Validate all three sites consistently. [S1]
6. **Weather provenance.** ERA5-Land is gridded reanalysis, not an “Oregon City Station.” Record exact endpoint, model selection, variable, requested and returned coordinates/elevation, grid resolution, downscaling settings, timezone, UTC pairing and interpolation. Verify 2 m air temperature versus skin/surface temperature and instantaneous versus daily maximum values. A service’s default blended model is not evidence of exclusive ERA5-Land use. The historical API documentation distinguishes these variables and models. [S4, S5]
7. **Heatwave definition.** State whether ≥90°F refers to the acquisition-time air value, a daily maximum, or an externally defined event. Those are different exposures. The row dated July 25, 2021 is not itself a June 2021 observation; remove “PNW Heat Dome (2021)” as an event label unless the relevant event dates are documented. Do not infer June exposure from July imagery.

## 3. Controls and confounding
Elevation proximity is a useful starting point, not proof that every other feature is identical. The stated subject/control elevations imply differences of 13 ft and 32 ft; “±16 ft” relative to the subject is inconsistent. Verify elevations with the same terrain product. Shared municipal boundaries do not eliminate air-flow, terrain, aspect, wind or moisture differences. Avoid “only canopy diverged.” Document roof material/color and replacement history, pavement/impervious fraction, building density, irrigation, parcel geometry, slope/aspect, shade at overpass time, historical development and each control’s canopy trajectory. Select controls without using desired thermal outcomes, and show separate-control estimates and leave-one-date-out sensitivity. A single hot 2006 observation is particularly influential evidence to investigate, not delete.

## 4. Permit-to-canopy-to-exposure chain
The report's illustrative permit rows show 75 permits and 30 removals across four years. They neither reconcile to 167 permits nor establish 167 tree removals. Treat “167 corridor permits,” “compelled removal,” and “zero replacement” as unverified allegations pending records. Distinguish sidewalk permits, tree authorizations, trees actually removed, locations, reasons, dates and replacements. Do not equate authorization with completion or city sidewalk enforcement with a mandatory order to remove a specific tree.

Build a geocoded ledger: unique permit ID; issuing authority; parcel/address; notice/order and service date; inspection; hazard/removal rationale; options offered; owner/contractor action; actual removal and corroboration; tree count/species/size; replacement conditions and survival; subject/control buffers; document Bates IDs and custodian. Deduplicate amended or related permits. Show all corridor boundaries and distance/exposure rules before counting. Reconcile every year to the aggregate and document missing records. Obtain both mitigation-positive and mitigation-negative records to avoid selection bias. Compare before/after imagery at the same locations.

For indoor or health assertions, separately assemble calibrated indoor/outdoor logs, room and sensor placement, shielding, logging interval, humidity, HVAC functionality and failures, roof/insulation/window changes, occupancy and contemporaneous records. Medical causation requires appropriate medical assessment; satellite LST is not a substitute. Keep protected medical material out of a public demonstrative.

## 5. Litigation packaging and legal boundaries
Federal Rule 702 requires a court-facing foundation for qualifications, sufficient facts/data, reliable methods and reliable application; a federal sensor does not certify an expert's analysis. Oregon's expert rule is ORS 40.410 (OEC 702), and the applicable state-law framework must be assessed separately. Do not state that Daubert and OEC are interchangeable or promise admissibility or survival of summary judgment. Obtain counsel review of the actual forum, claims, procedural requirements, deadlines and applicable case law. No jurisdiction-specific municipal duty, immunity, notice, limitations or liability determination was made here. [S6, S7]

Separate: (a) observed or reported values, (b) method-dependent estimates, (c) expert opinions within stated qualifications, and (d) legal arguments for counsel. Add author credentials, role/compensation, assumptions, contrary evidence, uncertainty, data/software versions and signature only after actual qualified review. “Tax Lot: Tower Vista Subdivision” is not a unique parcel identifier; supply the assessor account/tax-lot reference and map.

Preserve raw files and acquisition provenance; hash snapshots; version code and derived products; retain all inclusion/exclusion decisions and missing data; create a source/Bates-to-claim index. Retrieval hashes establish integrity of the captured bytes, not authenticity of agency records or truth of their contents. Seek custodian certification or other appropriate authentication with counsel. Keep a neutral evidentiary report separate from advocacy graphics.

The report title spans 1994–2026, but its thermal table ends in 2024. Use “1994–2024 selected observations; reviewed October 19, 2026” unless additional data are actually obtained. The former is a 30-year endpoint span; 1994–2026 is 32 years. Twelve selected dates do not constitute an unbroken 30-year record. “Historic record” should become “highest value among these 12 listed observations.” Only one listed Chapin value exceeds 120°F, so narration that it “routinely” does so is unsupported.

## 6. Improvement cycle and release gates
**Completed:** frozen source and supplied-review copies; all slide/narration extraction; reconstructed dataset; executable audit; correction register; conservative replacement report draft; review of primary method/rule documentation. This is a substantive first revision, not a completed expert opinion.

**Gate 1 — Measurement reproduction (Satellite LST Verified in Cycle 2; ERA5-Land Pending):** Cycle 2 (`microclimate_audit/`, Oct 28, 2026) verified all 12 USGS Collection 2 Level-2 scene IDs, UTC overpass timestamps (`18:19–18:56 UTC`), `QA_PIXEL`/`QA_RADSAT` flags, Chapin Court LST values (`±0.005°F`), two-control means (`±0.005°F`), and excess values (`±0.005°F`, including resolving the 2004 rounding question: `100.3549 - 88.2968 = 12.0581°F -> 12.06°F`). Remaining Gate 1 items: reconcile the 9/12 individual-control offsetting differences (by reporting exact point-sample control values alongside published values) and archive raw ERA5-Land hourly 2m air temperature responses at the exact UTC overpass timestamps.

**Gate 2 — Mechanism evidence:** verified permit ledger, historical canopy maps and control balance. Demonstrate local removals, timing and exposure rather than infer them from a regional count.

**Gate 3 — Inference:** prespecified estimand/design; expanded eligible-scene inventory; complete inclusion/exclusion log; honest uncertainty; sensitivity to dates, controls, masks, sensor and canopy measurement. More scenes are useful only if comparable and not selectively chosen. Bootstrap results cannot create independent treatment replications.

**Gate 4 — Case-specific review:** independent remote-sensing/statistical review; qualified expert and counsel review; authenticated exhibits; privacy review; print/accessibility and narration parity check. Do not circulate the original conclusory version as a validated final expert report while these gates remain unmet.

## Sources consulted (retrieved October 19, 2026)
[S1] USGS, Landsat Collection 2 Surface Temperature: scaling, inputs, limitations, ASTER vegetation/emissivity anomaly. https://www.usgs.gov/landsat-missions/landsat-collection-2-surface-temperature
[S2] USGS, What are the band designations for the Landsat satellites? Native thermal resolution versus resampled spacing. https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites
[S3] USGS, Landsat Normalized Difference Vegetation Index: spectral ratio and scaling. https://www.usgs.gov/landsat-missions/landsat-normalized-difference-vegetation-index
[S4] Copernicus Climate Data Store, ERA5-Land hourly data documentation. https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview
[S5] Open-Meteo, Historical Weather API documentation: models, coordinates, elevation, variables and timing. https://open-meteo.com/en/docs/historical-weather-api
[S6] Federal Rule of Evidence 702 and amendment notes, text reproduced by Cornell LII. https://www.law.cornell.edu/rules/fre/rule_702
[S7] Oregon Legislature, ORS Chapter 40, ORS 40.410 (OEC 702). https://www.oregonlegislature.gov/bills_laws/ors/ors040.html

These references establish methodological/rule context, not the authenticity of the report's underlying observations or permit counts. No current municipal code version or permit was independently verified. Saved text captures are included for inspection; unrelated navigation text may be present.
