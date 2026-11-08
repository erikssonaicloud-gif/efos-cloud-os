# Chapin Court: independent point-sample raster audit

## Scope
This is an independent extraction from USGS Collection 2 Level-2 raster products,
accessed through Microsoft's Planetary Computer catalog and hosted raster copies.
It is not a parcel-average analysis, a canopy-change reconstruction, or a causal study.
Coordinates were taken from the supplied report, not independently geocoded.

Report: https://executive-function-os.github.io/executivefunctionos.com/forensic-microclimate.html
Catalog: https://planetarycomputer.microsoft.com/api/stac/v1
USGS scaling reference: https://www.usgs.gov/faqs/how-do-i-use-a-scale-factor-landsat-level-2-science-products
USGS product documentation: https://www.usgs.gov/landsat-missions/landsat-collection-2-surface-temperature
USGS QA reference: https://www.usgs.gov/landsat-missions/landsat-collection-2-quality-assessment-bands

## Method
1. Query landsat-c2-l2 for each claimed calendar date and a small bounding box around Chapin.
2. Match the report's sensor/path/row/date scene prefix exactly; retain full catalog responses.
3. Read the containing 30 m raster grid cell at each published coordinate. No averaging,
   interpolation, neighborhood search, or adjustment to match published temperatures.
4. Convert nonzero ST DN to kelvin using DN * 0.00341802 + 149, then to Fahrenheit.
5. Extract QA_PIXEL, QA_RADSAT, and the surface-temperature uncertainty asset ('qa').
6. Compare against the source table. Differences are retrieved minus published.

## Findings
- All 12 scene prefixes matched. The 2010 scene is Tier 2, not Tier 1.
- Every Chapin temperature reproduced within 0.005 F (rounds to the published hundredth).
- At each control, 9 of 12 dates differ by more than 0.011 F from the published value;
  maximum absolute difference is about 3.99 F.
- Despite this, all 12 two-control averages match published averages within 0.005 F.
- Example 2010: retrieved Rivercrest 86.8601 F versus published 82.88 F;
  retrieved Hillendale 82.4918 F versus published 86.48 F.
  The cause of this offsetting discrepancy is unresolved. It is not proof of misconduct.
- All 36 QA_PIXEL samples have bits 0 through 5 unset; all QA_RADSAT samples are zero.
  These checks are not a comprehensive assessment of cloud adjacency, emissivity bias,
  geolocation error, or retrieval uncertainty. Full QA values are preserved.
- Using retrieved gaps and UNVERIFIED published ambient temperatures gives cool/hot means
  10.9861 F / 12.8598 F and Welch two-sided p = 0.26605.

## Interpretation limits
Scene existence is distinct from temperature reproduction. Point-sample reproduction
is distinct from a property-wide estimate. Neither validates ambient reanalysis values,
canopy percentages, canopy-loss dates, control comparability, or causal attribution.
The report's policy-era labels are copied as claims, not independently verified events.
Overpass timestamps are UTC, not local civil time.
Temperature uncertainty DN values are preserved without treating them as confidence intervals.
Source HTML is a retrieval snapshot, not a historical publication-date authentication.

## Deliverables
- chronological_audit.csv / .xlsx: claims, extracted values, differences, timestamps, QA.
- raster_samples_long.csv: raw values, coordinates, pixel indices and stable asset URLs.
- scene_validation.csv and stac_*.json: scene validation and catalog provenance.
- source_snapshot.html: source-page snapshot.
- reproduce.py: independent re-extraction script.
- manifest.json: retrieval timestamp and SHA-256 hashes for package files.

## Next priority
Reproduce hourly ambient temperature from explicit ERA5-Land request parameters at exact
overpass times; separately obtain dated aerial imagery and parcel/corridor boundaries.
Ask the report author for the code or extraction geometries explaining individual-control
differences before interpreting either control as a validated site time series.

## November 1, 2026 Supplement — Contemporaneous Elevated AQI Pocket Observation
- **Added Asset:** `2026-11-01_0845_Oregon_City_Elevated_AQI_91_Pocket.png` (also archived in `../aqi_observations/`).
- **Observation Summary:** Recorded November 1, 2026 at `08:45 PST`, showing a localized **US AQI 91** (Moderate, approaching the 100 Unhealthy for Sensitive Groups threshold) pocket centered directly over Oregon City ("My Location") while the surrounding Portland metro area, Willamette Valley, and Oregon Coast remained in the green (Good AQI) zone.
- **Companion Report:** See `../litigation_review/03_cycle2_raster_audit_and_aqi_supplement_2026-11-01.md` and the updated interactive HTML deck (`../forensic-microclimate.html`).
