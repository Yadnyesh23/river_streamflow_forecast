# Data Dictionary

## Project: Deep Learning Time-Series Forecasting of River Streamflow in Drought-Prone Basins (Krishna/Cauvery) under El Niño

This document describes every dataset and feature used in the River Streamflow Forecasting project.

---

# Dataset Overview

| Dataset | Source | Frequency | Purpose |
|---------|--------|-----------|---------|
| Krishna Streamflow | India-WRIS / CWC | Daily | Target variable for Krishna basin. |
| Cauvery Streamflow | India-WRIS / CWC | Daily | Target variable for Cauvery basin. |
| Krishna Rainfall | IMD | Daily | Daily basin rainfall. |
| Cauvery Rainfall | IMD | Daily | Daily basin rainfall. |
| Krishna Tmax | IMD | Daily | Maximum daily temperature. |
| Krishna Tmin | IMD | Daily | Minimum daily temperature. |
| Cauvery Tmax | IMD | Daily | Maximum daily temperature. |
| Cauvery Tmin | IMD | Daily | Minimum daily temperature. |
| Oceanic Niño Index (ONI) | NOAA CPC | Monthly | El Niño / La Niña climate indicator. |

---

# Krishna Rainfall Dataset

**Rows:** 9,131

**Columns:** 2

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Daily observation date. |
| `rainfall` | float | mm/day | Daily average rainfall over the Krishna River Basin. |

---

# Cauvery Rainfall Dataset

**Rows:** 9,131

**Columns:** 2

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Daily observation date. |
| `rainfall` | float | mm/day | Daily average rainfall over the Cauvery River Basin. |

---

# Krishna Streamflow Dataset

**Rows:** 343,261

**Columns:** 7

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Daily discharge observation date. |
| `station_name` | string | — | River gauge station name. |
| `river` | string | — | River where discharge is measured. |
| `basin` | string | — | River basin name (Krishna). |
| `latitude` | float | Degrees | Latitude of gauge station. |
| `longitude` | float | Degrees | Longitude of gauge station. |
| `streamflow` | float | m³/s | Manual daily river discharge. |

---

# Cauvery Streamflow Dataset

**Rows:** 266,597

**Columns:** 7

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Daily discharge observation date. |
| `station_name` | string | — | River gauge station name. |
| `river` | string | — | River where discharge is measured. |
| `basin` | string | — | River basin name (Cauvery/Kaveri). |
| `latitude` | float | Degrees | Latitude of gauge station. |
| `longitude` | float | Degrees | Longitude of gauge station. |
| `streamflow` | float | m³/s | Manual daily river discharge. |

---

# Krishna Tmax Dataset

**Rows:** 9,131

**Columns:** 2

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Daily observation date. |
| `tmax` | float | °C | Maximum daily temperature over the Krishna Basin. |

---

# Krishna Tmin Dataset

**Rows:** 9,131

**Columns:** 2

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Daily observation date. |
| `tmin` | float | °C | Minimum daily temperature over the Krishna Basin. |

---

# Cauvery Tmax Dataset

**Rows:** 9,131

**Columns:** 2

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Daily observation date. |
| `tmax` | float | °C | Maximum daily temperature over the Cauvery Basin. |

---

# Cauvery Tmin Dataset

**Rows:** 9,131

**Columns:** 2

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Daily observation date. |
| `tmin` | float | °C | Minimum daily temperature over the Cauvery Basin. |

---

# Oceanic Niño Index (ONI) Dataset

**Rows:** 919

**Columns:** 2

| Column | Data Type | Unit | Description |
|--------|-----------|------|-------------|
| `date` | datetime | YYYY-MM-DD | Monthly ONI observation date (first day of each month). |
| `oni` | float | ONI Index | Sea Surface Temperature anomaly in the Niño 3.4 region. Positive values indicate El Niño conditions, while negative values indicate La Niña conditions. |

---

# Derived Feature (Phase 1.3)

The following feature will be created before model training.

| Feature | Formula | Unit |
|---------|---------|------|
| `temperature` | `(tmax + tmin) / 2` | °C |

This represents the daily average temperature for each river basin.

---

# Final Master Dataset (Planned)

The processed dataset used for EDA and model training will contain one row per day.

| Feature | Data Type | Unit | Role |
|---------|-----------|------|------|
| `date` | datetime | YYYY-MM-DD | Time index |
| `rainfall` | float | mm/day | Input feature |
| `temperature` | float | °C | Input feature |
| `oni` | float | ONI Index | Climate input feature |
| `streamflow` | float | m³/s | Target variable |

**Time Period:** January 2001 – December 2025

**Frequency:** Daily (ONI will be expanded from monthly to daily during preprocessing).

**Target Variable:** `streamflow`

**Primary Basin for Model Training:** Krishna River Basin

**Secondary Basin:** Cauvery River Basin (comparison and future scope).