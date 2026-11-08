# Forensic Microclimate & AQI Supplement — Cycles 2 & 3 Audit Synthesis
## Updated November 1, 2026 | Working Evidentiary Technical Supplement (FRE 702 / OEC 702)

### Executive Summary
This supplement integrates the **Cycle 2 Independent Satellite Raster Audit** (`microclimate_audit/`, Oct 28, 2026), the **Cycle 3 Weather Provenance, 3×3 Buffer Sensitivity, & AQI Audit** (`cycle3/CYCLE3_REPORT.md`, Nov 1–2, 2026), and the **Contemporaneous Localized Elevated AQI Pocket Observation** (`2026-11-01_0845_Oregon_City_Elevated_AQI_91_Pocket.png`, Nov 1, 2026 at `08:45 PST`):

1. **Gate 1A — Satellite LST Reproduction (`COMPLETE`):** All 12 claimed scene prefixes (`1994–2024`) matched exact USGS Collection 2 Level-2 Surface Temperature (`L2SP`) scenes in the Microsoft Planetary Computer STAC catalog (`landsat-c2-l2`). Every Chapin Court Land Surface Temperature (`LST`), every two-control average (`Rivercrest` + `Hillendale`), and every thermal excess value reproduced within `±0.005°F`, with all 36 center pixels (and all **324/324** `3×3` neighborhood buffer pixels in Cycle 3) passing `QA_PIXEL` (`bits 0–5 = 0`) and `QA_RADSAT = 0`.
2. **Gate 1B — Weather Provenance Audit (`ACQUISITION COMPLETE / RELABELED`):** Cycle 3 queried all `12 dates × 3 sites × 2 models` (`era5_land` and `best_match`) at the exact CSV/STAC UTC overpass timestamps (`18:14:07Z` to `18:56:17Z`). The published `Ambient` column closely matches Open-Meteo **`best_match` local-calendar-day maximum temperature** (`MAE = 0.058°F`, `RMSE = 0.076°F`, all 12 dates within `0.1°F`), whereas exact-overpass 2m air temperature averages `9.44°F` lower (`64.92°F` to `92.24°F`). Accordingly, the published ambient column is relabeled as **Published Daily-High-Like Ambient (`best_match` Local Max)** alongside the exact overpass-hour 2m air temperatures.
3. **3×3 Spatial Buffer (`90m × 90m`) Sensitivity (`COMPLETE`):** Across all **324/324** clear pixels (`12 dates × 3 sites × 9 pixels`), Chapin Court thermal excess remains positive on **12 of 12 dates** under center-pixel (`+10.99°F` `<90°F` / `+12.86°F` `≥90°F`), `3×3` mean (`+10.48°F` / `+12.08°F`), and `3×3` median (`+10.98°F` / `+12.71°F`) extractions. Centered `3×3` buffering does not explain the 9/12 single-control point-sample offsets (`Rivercrest` vs. `Hillendale`), which remain transparently disclosed.
4. **Contemporaneous AQI 91 Screenshot & CAMS Model Comparison (`2026-11-01 08:45 PST / 16:45 UTC`):** The screenshot visibly shows **My Location, US AQI 91** (Moderate category; *Unhealthy for Sensitive Groups* starts at `101`) with a yellow feature over Oregon City and green surrounding areas at the displayed map scale. In Cycle 3, coarse (`~0.4°`) CAMS global forecast data via Open-Meteo at `16:45 UTC` (`08:45 PST`) modeled Oregon City at **US AQI 79** (`PM2.5 = 23.15 µg/m³`, `BLH = 151.25 m`, `10m wind = 0.865 m/s`), which is `+15.75 AQI` (`+16.8% PM2.5`) above the 5-city valley median, though `McMinnville` (`83`) and `Newberg` (`79`) were similarly elevated in the coarse forecast and event-date ERA5 reanalysis returned nulls due to reanalysis latency.

## 1. Cycle 2 & Cycle 3 Satellite Raster & Weather Provenance Table

### 1.1 Exact STAC Scene Validation & Overpass Timestamps (`scene_validation.csv`)
All 12 timestamps below are the authoritative CSV/STAC UTC acquisition timestamps verified in both Cycle 2 and Cycle 3:

| Overpass Date | Claimed Prefix | Matched STAC Item ID | Tier | Authoritative CSV/STAC Overpass (UTC) | Scene Cloud Cover (%) |
|---|---|---|---|---|---:|
| 1994-07-31 | `LT05_L2SP_046029_19940731` | `LT05_L2SP_046029_19940731_02_T1` | `T1` | `1994-07-31T18:14:07.763056Z` | 7.00% |
| 1998-08-27 | `LT05_L2SP_046029_19980827` | `LT05_L2SP_046029_19980827_02_T1` | `T1` | `1998-08-27T18:35:03.904094Z` | 0.00% |
| 2002-07-29 | `LE07_L2SP_046029_20020729` | `LE07_L2SP_046029_20020729_02_T1` | `T1` | `2002-07-29T18:44:41.226004Z` | 2.00% |
| 2004-07-26 | `LT05_L2SP_046029_20040726` | `LT05_L2SP_046029_20040726_02_T1` | `T1` | `2004-07-26T18:39:02.135081Z` | 0.00% |
| 2006-07-24 | `LE07_L2SP_046029_20060724` | `LE07_L2SP_046029_20060724_02_T1` | `T1` | `2006-07-24T18:46:09.008473Z` | 0.00% |
| 2010-08-20 | `LE07_L2SP_046029_20100820` | `LE07_L2SP_046029_20100820_02_T2` | **`T2`** | `2010-08-20T18:48:41.398308Z` | 4.00% |
| 2013-07-27 | `LE07_L2SP_046029_20130727` | `LE07_L2SP_046029_20130727_02_T1` | `T1` | `2013-07-27T18:51:43.778321Z` | 1.00% |
| 2015-08-18 | `LE07_L2SP_046029_20150818` | `LE07_L2SP_046029_20150818_02_T1` | `T1` | `2015-08-18T18:56:17.786583Z` | 0.00% |
| 2018-08-18 | `LC08_L2SP_046029_20180818` | `LC08_L2SP_046029_20180818_02_T1` | `T1` | `2018-08-18T18:55:54.572925Z` | 0.03% |
| 2021-07-25 | `LC08_L2SP_046028_20210725` | `LC08_L2SP_046028_20210725_02_T1` | `T1` | `2021-07-25T18:56:03.358214Z` | 0.14% |
| 2023-08-16 | `LC08_L2SP_046028_20230816` | `LC08_L2SP_046028_20230816_02_T1` | `T1` | `2023-08-16T18:55:59.221982Z` | 0.59% |
| 2024-07-09 | `LC09_L2SP_046029_20240709` | `LC09_L2SP_046029_20240709_02_T1` | `T1` | `2024-07-09T18:55:49.013440Z` | 0.01% |

### 1.2 Combined LST & Weather Reconciliation Table (Cycles 2 & 3)
The table below combines the Cycle 2 point-sample LST audit with the Cycle 3 Open-Meteo weather provenance reconciliation at Chapin Court (`45.33286° N, -122.61601° W`):

| Date | Published Ambient (°F) | `best_match` Local Max (°F) | ERA5-Land Local Max (°F) | ERA5-Land Overpass 2m (°F) | Chapin LST Retrieved (°F) | Rivercrest Pt (°F) | Hillendale Pt (°F) | Control Avg Retrieved (°F) | Excess Heat Retrieved (°F) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1994-07-31 | 83.30 | 83.40 | 83.40 | 71.14 | 98.7037 | 81.7782 | 90.9462 | 86.3622 | +12.3414 |
| 1998-08-27 | 82.00 | 82.00 | 82.00 | 71.76 | 93.5356 | 81.1486 | 89.3351 | 85.2418 | +8.2938 |
| 2002-07-29 | 81.00 | 81.00 | 81.00 | 73.56 | 105.6657 | 88.6272 | 94.5378 | 91.5825 | +14.0832 |
| 2004-07-26 | 82.60 | 82.70 | 82.70 | 71.69 | 100.3549 | 88.2414 | 88.3522 | 88.2968 | +12.0581 |
| 2006-07-24 | 96.40 | 96.50 | 96.50 | 88.78 | 119.0131 | 97.6908 | 105.7124 | 101.7016 | +17.3115 |
| 2010-08-20 | 73.00 | 73.00 | 73.00 | 64.92 | 91.6959 | 86.8601 | 82.4918 | 84.6759 | +7.0199 |
| 2013-07-27 | 77.70 | 77.80 | 77.80 | 69.87 | 105.1995 | 88.6395 | 96.6788 | 92.6591 | +12.5403 |
| 2015-08-18 | 95.50 | 95.60 | 95.60 | 85.64 | 103.7537 | 92.6079 | 95.1674 | 93.8876 | +9.8660 |
| 2018-08-18 | 83.50 | 83.40 | 84.20 | 73.80 | 101.0405 | 86.6634 | 94.2678 | 90.4656 | +10.5749 |
| 2021-07-25 | 91.20 | 91.10 | 87.30 | 79.12 | 110.2629 | 97.4352 | 100.2591 | 98.8471 | +11.4158 |
| 2023-08-16 | 101.50 | 101.50 | 100.50 | 92.24 | 118.2118 | 102.7907 | 108.4508 | 105.6208 | +12.5910 |
| 2024-07-09 | 99.70 | 99.70 | 99.60 | 91.58 | 122.5923 | 109.6352 | 109.2907 | 109.4630 | +13.1294 |

## 2. Cycle 3 Spatial Buffer Sensitivity (`3×3` Pixel Window / `90m × 90m`)

All **324/324** pixels (`12 dates × 3 sites × 9 pixels`) passed the QA screen (`DN ≠ 0`, `QA_PIXEL` bits 0–5 = 0, `QA_RADSAT = 0`). Holding the published `<90°F` / `≥90°F` daily-high regime groupings fixed:

| Extraction Method | Regime | `n` | Mean Excess (°F) | Min Excess (°F) | Max Excess (°F) |
|---|---|---:|---:|---:|---:|
| **Center Pixel (`30m`)** | Normal (`<90°F`) | 7 | **+10.986°F** | +7.020°F | +14.089°F |
| **Center Pixel (`30m`)** | Heat (`≥90°F`) | 5 | **+12.860°F** | +9.856°F | +17.313°F |
| **`3×3` Window Mean (`90m × 90m`)** | Normal (`<90°F`) | 7 | **+10.479°F** | +7.743°F | +12.879°F |
| **`3×3` Window Mean (`90m × 90m`)** | Heat (`≥90°F`) | 5 | **+12.077°F** | +9.608°F | +16.185°F |
| **`3×3` Window Median (`90m × 90m`)** | Normal (`<90°F`) | 7 | **+10.983°F** | +7.020°F | +14.237°F |
| **`3×3` Window Median (`90m × 90m`)** | Heat (`≥90°F`) | 5 | **+12.707°F** | +9.856°F | +17.058°F |

* **Robustness of Positive Contrast:** Every single one of the 12 dates remains positive under center-pixel, `3×3` mean (`+7.74°F` to `+16.19°F`), and `3×3` median (`+7.02°F` to `+17.06°F`) extractions, including when the 2010 Tier 2 (`T2`) scene is excluded.
* **Single-Control Offset Check:** Centered `3×3` buffering does **not** explain the 9/12 single-control offsets (`center_f` matches both published single-control columns within `±0.005°F` on 3 dates, whereas `mean_3x3_f` and `median_3x3_f` match both controls on `0` dates). Consequently, our reports and HTML deck explicitly display the verified point-sample control temperatures and disclose the unresolved single-control offset.

## 3. Contemporaneous AQI 91 Screenshot & Cycle 3 CAMS Model Comparison (`2026-11-01 08:45 PST`)

* **Screenshot Observation (`2026-11-01_0845_Oregon_City_Elevated_AQI_91_Pocket.png`):** Visibly displays **My Location, US AQI 91** (Moderate category; the *Unhealthy for Sensitive Groups* category starts at `101`, not `100`) with a localized yellow/amber feature over the Oregon City area and green surrounding areas at the displayed map scale, attributed to November 1, 2026 at `08:45 PST` (`16:45 UTC`).
* **Cycle 3 Coarse CAMS Global Model Comparison (`16:45 UTC / 08:45 PST`):**
  * Querying the Open-Meteo Air Quality API (`domains=cams_global`, `~0.4°` coarse grid) and Open-Meteo meteorological forecast fallback at `16:45 UTC` yields modeled **US AQI 79** (`PM2.5 = 23.15 µg/m³`, `PM10 = 24.80 µg/m³`, `BLH = 151.25 m`, `10m wind = 0.865 m/s`, ventilation proxy `130.83 m²/s`) at Oregon City / Chapin Court.
  * Against the 5-city Willamette Valley median (`Gresham 56.75`, `Portland 63.00`, `Salem 63.25`, `Newberg 79.00`, `McMinnville 83.00`), modeled Oregon City AQI is `+15.75 AQI points` (`+16.8% PM2.5`) higher, under shallow boundary-layer and weak-wind forecast conditions. However, in the coarse `~0.4°` CAMS forecast, `McMinnville` (`83`) and `Newberg` (`79`) are similarly elevated, and ERA5 reanalysis returned nulls for Nov 1 due to multi-day reanalysis latency.
  * **Evidentiary Synthesis:** The `12-point` difference between the high-resolution Apple Weather screenshot (`AQI 91`) and the coarse `~0.4°` CAMS global forecast (`AQI 79`), as well as the absence of post-latency ERA5 reanalysis or a vertical radiosonde temperature profile, is transparently preserved without overclaiming proven inversion trapping or tree-removal causation.
