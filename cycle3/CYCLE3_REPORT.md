# Cycle 3 — Chapin microclimate, weather provenance and AQI sensitivity

Generated 2026-11-02T02:43:32.869445+00:00. Descriptive technical audit; no causal or litigation-readiness certification.

## Executive findings and gate disposition

- **Gate 1A baseline preserved:** live 3×3 raster retrieval independently reproduces every prior center temperature exactly (maximum absolute difference 0°F). This check does not reopen the prior point-sample audit.
- **Gate 1B acquisition COMPLETE; original Ambient provenance NOT conclusively reproduced.** All 12 dates × 3 sites × 2 requested models were acquired, with exact CSV/STAC UTC timestamps. The published Ambient column is inconsistent with overpass-hour 2 m air temperature and is strongly consistent with a local-calendar-day maximum from `best_match`, not a homogeneous ERA5-Land overpass series. Original requests, model settings, elevation adjustments and retrieval vintage remain unverified.
- **Buffer sensitivity COMPLETE:** all 324 pixels are nonfill, clear under the bits-0–5 screen, and unsaturated. Mean and median thermal excess remain positive on 12/12 dates. A centered 3×3 buffer does **not** explain the individual-control discrepancies.
- **AQI exploratory acquisition COMPLETE; event reanalysis/inversion verification OPEN.** CAMS/Open-Meteo forecasts support elevated modeled PM2.5 at Oregon City, but do not reproduce the screenshot value 91 or a uniquely isolated pocket. ERA5 for November 1 returns nulls at retrieval; recent forecast meteorology is explicitly not reanalysis. No inversion profile, local monitor validation, tree-removal effect or common causal summer/winter mechanism is demonstrated.

## 1. Evidence intake and timestamp reconciliation

The original chat-uploaded ZIP was corrupt. The user-supplied public Google Drive folder provided intact extracted files and an older Cycle 2 ZIP that passed integrity testing. Both requested prerequisite Markdown documents were read first. The current Drive audit files were then downloaded individually and used as authoritative inputs. The source reproduction script encountered Google's executable download warning; the actual 2,037-byte Python file was subsequently downloaded, not executed from the warning HTML. Inputs are retained in this package; SHA-256 hashes provide integrity from this acquisition onward, not historical authenticity.

All 12 timestamps in `scene_validation.csv` agree with the saved STAC feature metadata. Live STAC item checks are exported separately. **All 12 timestamps in the narrative supplement differ from the CSV/STAC values.** For example, July 31, 1994 is **18:14:07.763056 UTC**, not 18:19:53.268063 UTC. This audit uses CSV/STAC values, including full fractional seconds, rather than the approximate 18:19–18:56 range in the request. See `outputs/supplement_timestamp_discrepancies.csv` and `outputs/live_stac_timestamp_verification.csv`.

The screenshot visibly shows **My Location, US AQI 91**, a yellow Oregon City-area feature and green surrounding areas at this map scale. Neither the capture date nor an authenticated location/GPS record is embedded in the visible image; November 1, 2026 08:45 PST is the supplied attribution, not independently authenticated. That attribution converts to **2026-11-01 16:45 UTC**. The screenshot alone neither identifies the pollutant driving AQI nor proves an inversion or ground-level monitor reading. AQI 91 is Moderate; the next category starts at 101, not 100.

## 2. Gate 1B methods and weather reconciliation

Endpoint: `https://archive-api.open-meteo.com/v1/archive`. Requested models `era5_land` and `best_match`; temperature unit Fahrenheit. Coordinates: Chapin 45.33286, -122.61601; Rivercrest 45.34510, -122.60766; Hillendale 45.32901, -122.59703. Default Open-Meteo terrain/elevation selection was retained; response coordinates, elevation and offset are exported. These are gridded model estimates, not parcel thermometers. `best_match` is an automatically selected/mixed product, not an assurance of ERA5-Land-only provenance.

For each UTC overpass, let f = elapsed seconds since 18:00 / 3600. Interpolated temperature = T18 + f(T19 − T18). This is linear time interpolation, not an additional observation. Two daily definitions were audited: the API's daily maximum for the UTC date and the local-day maximum derived from 48 UTC hourly values using the actual America/Los_Angeles calendar.

**Timezone safeguard:** the local-time API responses returned fixed **−28,800-second** offsets even for summer historical dates. Their hour labels must be interpreted with that returned offset, not retroactively localized as summer PDT. Primary hourly comparisons therefore use UTC responses. The true local-day hourly maximum uses IANA timezone conversion of the 48 UTC timestamps. Raw local-time API daily maxima remain separately labeled; their aggregation is not silently assumed to be the same as the DST-correct local-day maximum. API daily aggregation and maxima of rounded hourly samples can differ slightly.

There are 144 weather provenance rows: 12 dates × 3 sites × 2 models × 2 requested timezone modes. They represent paired timezone requests, not 144 independent weather observations. All request URLs, status codes, retrieval timestamps and raw JSON bodies are retained. Temperatures are API-rounded to tenths, so extra displayed interpolation digits do not add measurement accuracy.

### Chapin reconciliation (°F)

| date       |   Published °F |   ERA5-Land overpass °F |   best_match overpass °F |   ERA5-Land local max °F |   best_match local max °F |
|:-----------|---------------:|------------------------:|-------------------------:|-------------------------:|--------------------------:|
| 1994-07-31 |         83.300 |                  71.142 |                   71.142 |                   83.400 |                    83.400 |
| 1998-08-27 |         82.000 |                  71.762 |                   71.762 |                   82.000 |                    82.000 |
| 2002-07-29 |         81.000 |                  73.558 |                   73.558 |                   81.000 |                    81.000 |
| 2004-07-26 |         82.600 |                  71.692 |                   71.692 |                   82.700 |                    82.700 |
| 2006-07-24 |         96.400 |                  88.777 |                   88.777 |                   96.500 |                    96.500 |
| 2010-08-20 |         73.000 |                  64.916 |                   64.916 |                   73.000 |                    73.000 |
| 2013-07-27 |         77.700 |                  69.866 |                   69.866 |                   77.800 |                    77.800 |
| 2015-08-18 |         95.500 |                  85.635 |                   85.635 |                   95.600 |                    95.600 |
| 2018-08-18 |         83.500 |                  73.795 |                   72.241 |                   84.200 |                    83.400 |
| 2021-07-25 |         91.200 |                  79.123 |                   80.804 |                   87.300 |                    91.100 |
| 2023-08-16 |        101.500 |                  92.239 |                   92.619 |                  100.500 |                   101.500 |
| 2024-07-09 |         99.700 |                  91.584 |                   91.093 |                   99.600 |                    99.700 |

For **best_match local-day hourly maxima**, MAE versus published Ambient is **0.058°F**, RMSE **0.076°F**, and all 12 differences are at most 0.1°F (5 within 0.05°F). For **ERA5-Land local-day hourly maxima**, MAE is **0.517°F**, RMSE **1.182°F**, driven in part by July 25, 2021 (87.3 versus published 91.2°F).

By contrast, exact-overpass interpolation is lower than published Ambient by a mean **9.443°F for ERA5-Land** and **9.441°F for best_match**; no date matches within 0.15°F. ERA5-Land T18 and T19 mean deficits are 11.958°F and 8.675°F, respectively. The closest tested candidate is therefore a **best_match local-day maximum**. This is a provenance inference from numeric agreement, not proof of the original API call. Label the historical Ambient column as “published daily-high-like ambient, original provenance unresolved,” not “verified overpass ERA5-Land temperature.”

Control-site results and every candidate's error metrics are in `outputs/weather_comparison_summary.csv`. Local model grid cells can overlap between sites and are not independent local weather controls.

## 3. Centered 3×3 spatial-buffer check

The source STAC scene IDs and thermal asset selection logic were reused. Planetary Computer signs current Azure asset URLs; rasterio transforms each WGS84 site coordinate into the raster CRS, uses `ds.index` for the containing center pixel, and reads the 3×3 window centered on it. Distributed raster pixel size is 30 m, so the window is nominally **90×90 m**. This does not imply nine independent native thermal observations: sensor thermal footprints and resampling limit effective spatial resolution.

Scaling: K = DN × 0.00341802 + 149; °F = (K − 273.15) × 1.8 + 32. Validity requires DN ≠ 0, QA_PIXEL bits 0–5 unset and QA_RADSAT = 0. All **324/324** pixels passed, so masked and unmasked means coincide. Pixel values, masks, row/column indices, CRS and raw arrays are retained. ST_QA is also archived and summarized but no additional uncertainty threshold was imposed. Center pixels exactly reproduce the supplied baseline.

### Mean Chapin excess over the two equally weighted control windows

| method       | regime      |   n |   mean_excess_f |   min_excess_f |   max_excess_f |
|:-------------|:------------|----:|----------------:|---------------:|---------------:|
| center_f     | heat_ge90   |   5 |          12.860 |          9.856 |         17.313 |
| center_f     | normal_lt90 |   7 |          10.986 |          7.020 |         14.089 |
| mean_3x3_f   | heat_ge90   |   5 |          12.077 |          9.608 |         16.185 |
| mean_3x3_f   | normal_lt90 |   7 |          10.479 |          7.743 |         12.879 |
| median_3x3_f | heat_ge90   |   5 |          12.707 |          9.856 |         17.058 |
| median_3x3_f | normal_lt90 |   7 |          10.983 |          7.020 |         14.237 |

The published <90°F / ≥90°F Ambient groupings are held fixed in this table. They are descriptive, not verified contemporaneous overpass heatwave classifications. Using reproduced ERA5-Land daily maxima moves 2021 below 90°F; overpass-based classifications change substantially. Alternative classifications are exported in `outputs/regime_reclassification_sensitivity.csv`.

All dates remain positive: mean-window excess spans **7.743–16.185°F**, median-window excess **7.020–17.058°F**. Excluding the disclosed 2010 Tier 2 scene also leaves every remaining date positive. The mean-window estimates are lower than point estimates in both published regimes, but the summer surface-temperature contrast is robust to this particular buffer choice. This does not establish parcel-wide air-temperature exposure, removal causality, or representativeness of all summer scenes.

### Does buffering explain the control offsets?

| method       |   control_site_date_matches |   both_controls_matched_dates |   control_mae_f |   control_max_abs_error_f |
|:-------------|----------------------------:|------------------------------:|----------------:|--------------------------:|
| center_f     |                           6 |                             3 |           1.286 |                     3.988 |
| mean_3x3_f   |                           0 |                             0 |           1.408 |                     5.303 |
| median_3x3_f |                           2 |                             0 |           1.335 |                     3.988 |

At a ±0.005°F tolerance, center pixels match both published single-control columns on 3 dates, whereas neither the centered 3×3 mean nor median matches both on **any** date. Mean-window control MAE is worse than point MAE. Thus this tested geometry does not reconcile the 9 discrepant dates; different coordinates, weights or historical extraction logic would require original documentation. It would be inappropriate to search arbitrary geometries until the published numbers fit and then call that provenance established.

## 4. AQI and boundary-layer stagnation: qualified model comparison

Sources: Open-Meteo Air Quality API with `domains=cams_global`, PM2.5, PM10, US AQI and PM-specific subindices; ERA5 Historical Weather API with boundary-layer height, 10 m wind and 2 m temperature; and, explicitly as a recent-data fallback, the Open-Meteo forecast API for the same meteorological variables. Requested interval: **October 31–November 2, 2026 UTC**. Some November 2 forecast hours are future relative to retrieval; they are flagged and excluded from the event anchor and dawn summaries. Querying an historical date through a forecast archive does not make it assimilated reanalysis or a monitor observation.

The five broader valley controls were analyst-selected city centers: Portland, Gresham, Newberg, McMinnville and Salem. Lincoln City is a separate coast comparator; Rivercrest and Hillendale are retained as nearby controls. Exact coordinates are in raw requests and exported rows. They are exploratory comparisons, not matched causal controls.

ERA5 returned HTTP 200 but **null meteorological values** for the event date, consistent with the documented reanalysis latency; a successful request is not verified event weather. The recent forecast fallback is not substituted into a “reanalysis” label. No vertical temperature profile was retrieved; boundary-layer height plus weak surface wind cannot by themselves demonstrate a temperature inversion.

### 16:45 UTC / 08:45 PST anchor

The table linearly interpolates the 16:00 and 17:00 modeled values (75% weight on 17:00); it is not an observed 08:45 reading. Wind is in m/s, boundary-layer height in m, particulate matter in µg/m³. The ventilation proxy is boundary-layer height × **10 m** wind; this is only a screening proxy, not a standard mixed-layer ventilation coefficient based on layer-mean wind.

| site               |   us_aqi |   pm2_5 |   pm10 |   boundary_layer_height |   wind_speed_10m |   temperature_2m |   ventilation_proxy_m2_s |
|:-------------------|---------:|--------:|-------:|------------------------:|-----------------:|-----------------:|-------------------------:|
| chapin             |   79.000 |  23.150 | 24.800 |                 151.250 |            0.865 |            5.125 |                  130.831 |
| gresham            |   56.750 |  15.850 | 18.675 |                 201.250 |            1.180 |            5.425 |                  237.475 |
| hillendale         |   20.750 |   5.875 |  7.625 |                 151.250 |            0.865 |            5.200 |                  130.831 |
| lincoln_city_coast |   50.000 |  12.800 | 14.700 |                  43.750 |            0.950 |            6.800 |                   41.562 |
| mcminnville        |   83.000 |  19.825 | 21.700 |                  86.250 |            0.290 |            4.350 |                   25.012 |
| newberg            |   79.000 |  23.150 | 24.800 |                 138.750 |            0.940 |            5.150 |                  130.425 |
| portland           |   63.000 |  24.700 | 27.475 |                 207.500 |            1.103 |            6.000 |                  228.769 |
| rivercrest         |   79.000 |  23.150 | 24.800 |                 152.500 |            0.875 |            5.250 |                  133.438 |
| salem              |   63.250 |   6.675 |  7.975 |                 141.250 |            0.598 |            5.150 |                   84.397 |

At Oregon City/Chapin, modeled AQI is **79**, not screenshot AQI 91: a **12-point** non-reproduction. PM2.5 is **23.15 µg/m³**, PM10 **24.80 µg/m³**; the PM2.5 AQI subindex equals total AQI at the anchor. AQI subindices use their own concentration/time-averaging logic; do not recompute instantaneous AQI from one hourly PM value and assume exact equivalence.

Against the median of the five broader valley sites, Oregon City has **+15.75 AQI points** and **+3.325 µg/m³ PM2.5 (+16.8%)**. However, **McMinnville AQI is 83**, Newberg is also 79, and Portland PM2.5 is 24.70 µg/m³. This retrieval does **not** support “Oregon City alone elevated while the entire surrounding valley is green.” The screenshot and model products may differ in provider, resolution, averaging, geolocation and vintage; their disagreement is retained, not forced into agreement.

Forecast Chapin boundary-layer height is **151.25 m**, 10 m wind **0.865 m/s**, and ventilation proxy **130.83 m²/s**. These indicate a modeled shallow/weak-wind state, but not uniquely severe local trapping: the five-site median boundary-layer height is 141.25 m and median ventilation proxy 130.425 m²/s; McMinnville is much less ventilated in this forecast. Evidence for uniquely stronger Oregon City stagnation is therefore not established.

**Spatial-product caution:** the API reports the same latitude/longitude for Chapin, Rivercrest and Hillendale, yet Hillendale's AQ/PM series differs markedly. Independent single-location requests reproduce every multi-location AQ/PM value exactly (648 site-hour-variable checks), so this is not a response-ordering mistake. The API's reported coordinate is not proof of independent native pollution grid cells or a neighborhood-resolved physical contrast. The cause of the same-coordinate discrepancy is unresolved; do not use Hillendale's lower modeled AQI as proof of sub-neighborhood trapping. The documented CAMS global product is coarse (~0.4° native grid); hourly/interpolated output or finer returned coordinate spacing does not confer parcel resolution.

The 12:00–17:00 UTC dawn-window summaries and joined hourly PM/meteorology series are exported. Serially correlated modeled hours, nearby overlapping cells and one selected event do not support independent-sample significance tests or a causal tree-canopy conclusion. Cool-season particulate accumulation and summer surface heating can be considered distinct environmental hazards, but this audit does not demonstrate that the same local mechanism caused both.

## 5. Deliverables, rerun and unresolved work

- `outputs/weather_provenance_verified.csv`: reproduced response-level weather values; “verified” refers to acquisition/derivation, not verification of published original provenance.
- `outputs/buffer_pixel_samples.csv`: all 324 thermal/QA pixels; `outputs/buffer_site_sensitivity.csv`: 36 site-date summaries; `outputs/buffer_thermal_excess.csv`: 36 date-method excess rows.
- `outputs/aqi_meteorology_hourly.csv`: all requested model products, including null ERA5 rows; snapshots, spatial contrasts, dawn summaries and future flags are separate exports.
- `raw/`: complete JSON bodies, metadata and raster window arrays. `inputs/`: prerequisite documents and source evidence. `docs/`: captured official documentation used to interpret models and limitations.
- `scripts/run_cycle3.py`: acquisition and reproducibility, caching raw responses. `scripts/analyze_and_report.py`: analysis, tables and figures. `scripts/package.py`: SHA-256 manifest and ZIP creation.
- Install dependencies from `requirements.txt`; run acquisition script then analysis script then packaging script. Caches preserve this retrieval; remove cached raw files and request metadata to reacquire current data. Raw responses can change with provider revisions. Live signing and network access are required for raster reruns.

**Still needed before event/mechanism claims:** reacquire ERA5 after latency and verify nonnull data; obtain a vertical temperature profile and suitable local PM monitoring (with QA and averaging definitions); authenticate the screenshot timestamp/location/provider; recover the original Ambient API request and model/elevation settings; recover original control extraction geometry; expand beyond selected dates/events; obtain independently verified canopy/removal evidence and a defensible causal design. No permit, legal, health-outcome or removal-causation conclusion is made here.

## Official source references captured at acquisition

1. Open-Meteo Historical Weather documentation: https://open-meteo.com/en/docs/historical-weather-api — model selection, spatial resolutions, variable availability and ERA5 latency.
2. Open-Meteo Air Quality documentation: https://open-meteo.com/en/docs/air-quality-api — CAMS global forecast product, native spatial/temporal resolution, AQI variable semantics and archived forecast access. Attribution: CAMS ENSEMBLE/Copernicus Atmosphere Monitoring Service through Open-Meteo.
3. Microsoft Planetary Computer Landsat Collection 2 Level-2 STAC collection: https://planetarycomputer.microsoft.com/api/stac/v1/collections/landsat-c2-l2 — asset metadata and scene identities; full per-scene STAC records are retained.
4. USGS Landsat Collection 2 Level-2 temperature scaling is implemented consistently with the supplied Gate 1A reproduction script and the thermal raster metadata. Raw DN values and exact formula are retained for independent checking.

Integrity: `SHA256_MANIFEST.csv` hashes all package members except itself. A separate archive checksum verifies the outer ZIP. SHA-256 integrity does not authenticate historical claims or provider accuracy.
