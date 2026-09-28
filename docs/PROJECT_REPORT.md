# 🌊 Deep Learning Time-Series Forecasting of River Streamflow in Drought-Prone Basins (Krishna & Cauvery) under El Niño

> **Course:** Project Based Learning (PBL) — Semester V  
> **Institution:** K. J. Somaiya Institute of Technology  
> **Department:** Artificial Intelligence & Data Science  
> **Author:** Yadnyesh Hemant Halde  
> **Repository:** `river_streamflow_forecast`  
> **Document Version:** 1.0 (Comprehensive Project Report)  
> **Date:** September 2026  

---

## Executive Summary

River streamflow forecasting in peninsular India is a critical challenge for flood risk mitigation, agricultural water security, and reservoir dispatch. In rain-fed, non-snowmelt basins like the **Krishna** and **Cauvery**, streamflow dynamics are governed by monsoon precipitation and modulated by planetary climate phenomena such as the **Oceanic Niño Index (ONI)** / **El Niño–Southern Oscillation (ENSO)**.

This project delivers an end-to-end, empirical machine learning and deep learning forecasting pipeline. Spanning **25 years of daily meteorological and hydrological observations (2001–2025)** across **54 continuous gauge stations**, the study compares naive persistence baselines, ensemble tree methods (**Random Forest**, **LightGBM**), and sequence-learning deep neural networks (**Long Short-Term Memory - LSTM** and **Temporal Convolutional Networks - TCN**).

Evaluated on an untouched holdout test period (2023–2025), the **LSTM architecture achieved the highest performance** with a **Mean Absolute Error (MAE) of $51.45\text{ m}^3/\text{s}$** and a **Nash–Sutcliffe Efficiency (NSE) of $0.733$**, outperforming both the persistence baseline (NSE $0.624$) and tree-based models (Random Forest NSE $0.704$, LightGBM NSE $0.690$).

---

## 1. Problem Statement & Research Motivation

### 1.1 Problem Statement
Develop a high-accuracy, data-leakage-free time-series forecasting model to predict future daily river discharge ($\text{m}^3/\text{s}$) across river gauge stations in drought-prone basins (primarily the **Krishna River Basin**, with **Cauvery** as secondary comparative basin) under the influence of climatic drivers including **El Niño**, using deep learning architectures (TCN and LSTM) benchmarked against traditional machine learning models.

### 1.2 Hydrological & Meteorological Challenges
1. **Catchment Lag & Infiltration:** In rain-fed peninsular river basins, same-day rainfall correlates poorly with same-day streamflow (correlation coefficient $r = 0.07$ to $0.61$). Streamflow exhibits heavy autocorrelation with multi-day delays due to soil moisture saturation and runoff routing.
2. **Macro-Climatic Modulation (ENSO):** Sea Surface Temperature (SST) anomalies in the equatorial Pacific (Niño 3.4 region) disrupt Indian Summer Monsoon circulation. El Niño episodes frequently correlate with deficient rainfall and prolonged droughts, whereas La Niña phases trigger surplus precipitation and catastrophic flooding.
3. **Severe Hydrograph Skewness:** Streamflow distributions exhibit extreme positive skewness (thousands of low-flow dry season days versus brief, immense monsoon flood spikes exceeding $10,000\text{ m}^3/\text{s}$). Standard regression models trained on raw values heavily under-predict flood crests while failing on low-flow regimes.

---

## 2. Project Architecture & End-to-End Pipeline

```text
[ Raw Meteorological & Hydrological Data ]
  ├── CWC / India-WRIS State-wise Streamflow CSVs (Daily)
  ├── IMD Gridded High-Resolution Rainfall (0.25° × 0.25° NetCDF)
  ├── IMD Gridded Temperature (1.0° × 1.0° Binary .GRD: Tmax & Tmin)
  ├── NOAA CPC Oceanic Niño Index (Monthly ASCII .txt)
  └── Central Water Commission Subbasin Shapefiles (.shp)
                           │
                           ▼
[ Preprocessing & Spatial Masking Pipeline (scripts/) ]
  ├── scripts/convert_rainfall.py    (GeoPandas polygon clipping + xarray aggregation)
  ├── scripts/convert_temperature.py (NumPy binary parsing + 99.9 NaN masking)
  ├── scripts/convert_streamflow.py  (Basin filtering, datetime normalization)
  └── scripts/convert_oni.py         (Seasonal code to timestamp mapping)
                           │
                           ▼
[ Aligned Interim Datasets (data/interim/) ]
  └── Daily unified time-series for Krishna & Cauvery (9,131 days: 2001–2025)
                           │
                           ▼
[ Master Merging & Station Quality Screening (notebooks/02 & 03) ]
  ├── Merge weather + discharge tables
  ├── Missing date re-indexing (gap-aware calendar alignment)
  └── 54 usable stations selected based on historical continuity
                           │
                           ▼
[ Feature Engineering (notebooks/04) -> data/processed/krishna_features.csv ]
  ├── Autoregressive Streamflow Lags (Lag-1, 2, 3, 7 days)
  ├── Cumulative Rainfall Windows (3-day, 7-day, 14-day rolling sums)
  ├── Seasonal Indicators (month, is_monsoon flag)
  ├── Climate Teleconnection (90-day station-wise rolling ONI)
  └── Log-transform target: y = log(1 + streamflow)
                           │
                           ▼
[ Leakage-Free Time-Based Partitioning ]
  ├── Train Set:      2001–2020  (224,884 samples)
  ├── Validation Set: 2021–2022  (34,557 samples)
  └── Test Set:       2023–2025  (47,147 samples - touched once)
                           │
                           ▼
[ Model Benchmarking & Deep Learning (notebooks/05, 06, 07) ]
  ├── 1. Persistence Baseline      (y_hat_t = y_{t-1})
  ├── 2. Random Forest Regressor   (Log-transformed target, max_depth=12)
  ├── 3. LightGBM Regressor        (Gradient boosted trees with early stopping)
  ├── 4. Temporal ConvNet (TCN)    (Dilated causal Conv1D, d = [1, 2, 4, 8])
  └── 5. LSTM Sequence Model       (30-day multivariate sliding window)
                           │
                           ▼
[ Evaluation & Diagnostics ]
  ├── Aggregate Metrics: MAE, RMSE, Nash-Sutcliffe Efficiency (NSE)
  ├── Flood Event Peak Tracking (Wadenepally Gauge Station)
  └── ENSO Phase Stratified Evaluation (El Niño vs. La Niña)
                           │
                           ▼
[ Planned Deployment (Phases 10–13) ]
  ├── FastAPI Prediction Microservice (REST API)
  ├── PostgreSQL Database Storage
  └── React.js Interactive Dashboard + Docker Deployment
```

---

## 3. Data Sources & Specifications

| Dataset | Primary Source Agency | Native Format | Converted Format | Frequency | Geographic Coverage / Resolution |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **River Streamflow** | Central Water Commission (CWC) / India-WRIS | State-wise CSVs | Cleaned CSV | Daily ($\text{m}^3/\text{s}$) | Krishna (343,261 rows; 54 stations) & Cauvery (266,597 rows) |
| **Gridded Rainfall** | India Meteorological Department (IMD Pune) | NetCDF (`.nc`) | Tabular CSV | Daily ($\text{mm}/\text{day}$) | $0.25^\circ \times 0.25^\circ$ all-India grid (25 yearly files, 2001–2025) |
| **Gridded Temperature** | India Meteorological Department (IMD Pune) | Binary (`.GRD`) | Tabular CSV | Daily ($^\circ\text{C}$) | $1.0^\circ \times 1.0^\circ$ grid; Tmax and Tmin |
| **Oceanic Niño Index** | NOAA Climate Prediction Center (CPC) | ASCII (`.txt`) | Standard CSV | Monthly anomaly | Niño 3.4 SST anomalies ($5^\circ\text{N}$–$5^\circ\text{S}$, $170^\circ$–$120^\circ\text{W}$) |
| **Basin Boundaries** | CWC / India-WRIS GIS portal | ESRI Shapefile | Polygon mask | Static | Vector sub-basin boundaries (`Subbasin.shp`) |

### Geospatial Masking Methodology
Using [`scripts/convert_rainfall.py`](file:///c:/Users/yadny/OneDrive/Desktop/Yadnyesh/ResumeProjects/river_streamflow_forecast/scripts/convert_rainfall.py) and [`scripts/convert_temperature.py`](file:///c:/Users/yadny/OneDrive/Desktop/Yadnyesh/ResumeProjects/river_streamflow_forecast/scripts/convert_temperature.py), vector polygon geometry from `Subbasin.shp` is used to clip gridded rasters. Spatial weighted cell averages are computed to generate exact daily basin-average rainfall and temperature time-series spanning 9,131 days (2001 to 2025).

---

## 4. Feature Engineering & Preprocessing Strategy

All feature engineering logic is codified in [`notebooks/04_krishna_feature_engineering.ipynb`](file:///c:/Users/yadny/OneDrive/Desktop/Yadnyesh/ResumeProjects/river_streamflow_forecast/notebooks/04_krishna_feature_engineering.ipynb) resulting in [`data/processed/krishna_features.csv`](file:///c:/Users/yadny/OneDrive/Desktop/Yadnyesh/ResumeProjects/river_streamflow_forecast/data/processed/krishna_features.csv):

1. **Autoregressive Lags:**
   - `streamflow_lag_1`, `streamflow_lag_2`, `streamflow_lag_3`, `streamflow_lag_7`
   - Grouped station-wise so lookbacks never cross distinct river gauge locations.
2. **Cumulative Rainfall Infiltration Windows:**
   - `rainfall_sum_3d`, `rainfall_sum_7d`, `rainfall_sum_14d`
   - Captures basin retention, soil saturation, and delayed flood wave travel time.
3. **Seasonality Controls:**
   - `month` ($1$ to $12$)
   - `is_monsoon`: Binary flag ($1$ for June, July, August, September, October).
4. **ENSO Climate Teleconnection Feature:**
   - `oni_3month_avg`: 90-day station-wise rolling mean of the monthly Oceanic Niño Index. Captures the slow seasonal climate state of the Pacific Ocean.
5. **Target Transformation:**
   - $y_{\text{train\_log}} = \ln(1 + \text{streamflow})$
   - Predictions are inverted back to original units using $\hat{y} = \exp(\hat{y}_{\text{log}}) - 1$.
6. **Sliding Window Sequence Generation (for Deep Learning):**
   - Window size: $30$ days of raw multidimensional signals (`log_streamflow`, `rainfall`, `tmax`, `oni_3month_avg`, `is_monsoon`).
   - Gap-aware re-indexing prevents artificial splicing across missing dates.
   - Total generated 3D tensor: $245,736$ sequence samples of shape $(30, 5)$.

---

## 5. Experimental Results & Model Benchmarking

Models were trained on 2001–2020 data, tuned on 2021–2022 validation data, and evaluated on the independent **2023–2025 test set** ($47,147$ observation rows):

| Model Architecture | Model Class | Test MAE ($\text{m}^3/\text{s}$) | Test RMSE ($\text{m}^3/\text{s}$) | Test NSE | Key Hydrological Findings |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Persistence Baseline** | Naive Rule | $54.27$ | — | $0.624$ | Strong aggregate baseline due to streamflow auto-correlation; lags flood crests by 1 day. |
| **Random Forest** | Bagging Ensemble | $53.24$ | $401.75$ | $0.704$ | Outperforms persistence on MAE and NSE; struggles with non-linear peak flood magnitude. |
| **LightGBM** | Boosting Ensemble | $55.31$ | $411.55$ | $0.690$ | Sequential error correction; slightly overfits normal regime, leading to higher test error. |
| **TCN (Conv1D)** | Deep Learning | $52.58$ | — | $0.727$ | Exponential receptive field ($1, 2, 4, 8$) efficiently captures catchment lag without recurrent loops. |
| **LSTM** | Deep Learning | **$51.45$** | — | **$0.733$** | **Winner.** Best aggregate tracking of both low-flow dry spells and monsoon onset curves. |

### Hydrological Diagnostics: Flood Peak Analysis
Detailed time-series diagnostics conducted at the high-discharge **Wadenepally gauge station** revealed:
- Tree-based models (Random Forest) systematically "truncate" sharp flood crests because decision trees cannot extrapolate beyond observed leaf averages.
- Sequence models (LSTM and TCN) track the rising and falling limbs of hydrographs with substantially lower peak lag errors.

---

## 6. Technology Stack & Software Architecture

### Core Technologies
* **Language & Runtime:** Python 3.13 via dedicated `.venv` environment
* **Geospatial & Multidimensional Data:** `geopandas`, `shapely`, `xarray`, `rioxarray`
* **Data Processing & Scientific Computing:** `pandas`, `numpy`, `scipy`
* **Machine Learning & Gradient Boosting:** `scikit-learn`, `lightgbm`
* **Deep Learning Frameworks:** `tensorflow` / `keras` (LSTM, Conv1D, EarlyStopping callbacks), `torch`
* **Visualization:** `matplotlib`, `seaborn`
* **Development & Tooling:** Jupyter Notebooks, `ipykernel`, `tqdm`, `python-dotenv`

### Planned Application Architecture (Phases 10–13)
```text
┌─────────────────────────┐
│     React Dashboard     │  Interactive UI: Hydrographs, flood risk thresholds,
│    (Tailwind / Chart)   │  station selectors, real-time climate status
└────────────┬────────────┘
             │ HTTP / JSON
             ▼
┌─────────────────────────┐
│     FastAPI Backend     │  High-performance Python ASGI REST API:
│       (REST API)        │  /predict, /stations, /historical, /metrics
└──────┬───────────┬──────┘
       │           │
       ▼           ▼
┌──────────────┐ ┌──────────────────────────────────────┐
│  PostgreSQL  │ │ Loaded AI Weights (models/best_model)│
│   Database   │ │ Scaler parameters (log_sf_mean, std) │
└──────────────┘ └──────────────────────────────────────┘
```

---

## 7. Project Directory Structure

```text
river_streamflow_forecast/
├── README.md                      # Project overview and executive outline
├── ROADMAP.md                     # Comprehensive 14-phase development roadmap
├── TODO.md                        # Implementation task tracker
├── requirements.txt               # Project library dependencies
│
├── docs/                          # Technical project documentation
│   ├── PROJECT_REPORT.md          # Complete formal consolidated project report
│   ├── dataset_sources.md         # Source URLs, raw data structures, conversions
│   ├── data_dictionary.md         # Full feature schema, units, and descriptions
│   ├── master_eda.md              # 17-point EDA verification checklist
│   └── krishna_master_eda_debug.md# Station screening & coverage debug notes
│
├── scripts/                       # ETL & Conversion Pipeline Scripts
│   ├── convert_rainfall.py        # IMD NetCDF grid spatial polygon clipping
│   ├── convert_temperature.py     # Binary .GRD parser (Tmax / Tmin)
│   ├── convert_streamflow.py      # CWC discharge data cleaner
│   └── convert_oni.py             # NOAA CPC ASCII table parser
│
├── data/                          # Data Medallion Storage
│   ├── raw/                       # Raw downloads (.nc, .GRD, .txt, .shp, CSVs)
│   ├── interim/                   # Converted single-variable daily CSVs
│   └── processed/                 # krishna_features.csv, master clean tables
│
├── notebooks/                     # Analytical & Modeling Jupyter Notebooks
│   ├── 00_environment_check.ipynb
│   ├── 01_dataset_understanding.ipynb
│   ├── 02_merge_datasets.ipynb
│   ├── 03_krishna_eda.ipynb
│   ├── 04_krishna_feature_engineering.ipynb
│   ├── 05_krishna_split_and_baseline_model.ipynb
│   ├── 06_krishna_lightgbm.ipynb
│   ├── 07_krishna_lstm_tcn.ipynb
│   └── 08_kaveri_eda.ipynb
│
├── src/                           # Modular source code package
│   ├── features/                  # Feature generation modules
│   ├── models/                    # Model architecture scripts
│   ├── preprocessing/             # Cleaning and transformation utilities
│   ├── training/                  # Model fit and validation routines
│   └── utils/                     # Metrics (NSE, RMSE) and helper functions
│
├── models/                        # Serialized model checkpoints
└── outputs/                       # Visualizations, hydrograph comparison plots
```

---

## 8. Conclusions & Future Work

### Conclusions
1. **Model Hierarchy Established:** The empirical results demonstrate that deep learning sequence models outperform traditional machine learning models in capturing catchment memory and non-linear rainfall-runoff dynamics in the Krishna basin. The **LSTM** model is the top performer ($\text{MAE } 51.45\text{ m}^3/\text{s}$, $\text{NSE } 0.733$).
2. **Climate Index Teleconnection:** Incorporating the 90-day rolling ONI anomaly index accounts for multi-month seasonal monsoon dampening during El Niño phases, providing essential macro-climate context beyond local precipitation.
3. **Data Quality Rigor:** Filtering out fragmented stations down to 54 continuous gauge stations and enforcing strict time-based splits prevented synthetic data leakage.

### Future Scope
* **Phase 10:** Containerize and export the best-performing LSTM model into `models/lstm_krishna_v1.keras` or `torch` weights.
* **Phase 11:** Implement a **FastAPI** inference service with endpoints for single-station and basin-wide predictions.
* **Phase 12:** Build a modern, interactive web dashboard in **React** featuring dynamic hydrographs, flood alert levels, and climate scenario simulation.
* **Phase 13:** Multi-basin transfer learning: evaluate the generalizability of the trained Krishna model on the Cauvery River basin.
