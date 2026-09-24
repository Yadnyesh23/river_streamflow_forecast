# Dataset Sources

## Project: Deep Learning Time-Series Forecasting of River Streamflow in Drought-Prone Basins (Krishna/Cauvery) under El Niño

This document describes the source, format, preprocessing pipeline, and usage of every dataset used in this project.

---

# Dataset Summary

| Dataset | Source | Raw Format | Converted Format | Frequency |
|---------|--------|------------|------------------|-----------|
| River Streamflow | India-WRIS / Central Water Commission (CWC) | CSV | CSV | Daily |
| Rainfall | India Meteorological Department (IMD) | NetCDF (`.nc`) | CSV | Daily |
| Maximum Temperature (Tmax) | India Meteorological Department (IMD) | GRD (`.GRD`) | CSV | Daily |
| Minimum Temperature (Tmin) | India Meteorological Department (IMD) | GRD (`.GRD`) | CSV | Daily |
| Oceanic Niño Index (ONI) | NOAA Climate Prediction Center (CPC) | ASCII Text (`.txt`) | CSV | Monthly |

---

# 1. River Streamflow Dataset

**Source:** India-WRIS (Water Resources Information System) / Central Water Commission (CWC). <Cite refs={["turn525328search6","turn525328search5"]}/>

### Description

Daily river discharge observations collected from multiple hydrological gauge stations across Indian river basins.

### Coverage

- **River Basins:** Krishna and Cauvery.
- **Time Period:** January 2001 – December 2025.
- **Frequency:** Daily.

### Raw Dataset

- Multiple state-wise CSV files.
- Contains observations from several gauge stations.

### Preprocessing

Script used:

```text
scripts/convert_streamflow.py
```

Operations performed:

- Filtered records for Krishna and Cauvery basins.
- Converted `Data Acquisition Time` to datetime.
- Renamed discharge column to `streamflow`.
- Retained station name and geographical coordinates.

### Output Files

```text
data/interim/
├── krishna_streamflow.csv
└── cauvery_streamflow.csv
```

---

# 2. Rainfall Dataset

**Source:** India Meteorological Department (IMD) Gridded Daily Rainfall Dataset (0.25° × 0.25° resolution). <Cite refs={["turn525328search2","turn525328search11"]}/>

### Description

Observed daily rainfall values over India stored as yearly NetCDF files.

### Coverage

- **Resolution:** 0.25° × 0.25°.
- **Time Period:** 2001–2025.
- **Frequency:** Daily.

### Raw Dataset

- 25 NetCDF (`.nc`) files.
- One file per year.

### Preprocessing

Script used:

```text
scripts/convert_rainfall.py
```

Operations performed:

- Read NetCDF files using `xarray`.
- Extracted rainfall values for Krishna and Cauvery basin boundaries.
- Computed daily basin-average rainfall.
- Exported one CSV per basin.

### Output Files

```text
data/interim/
├── krishna_rainfall.csv
└── cauvery_rainfall.csv
```

Each CSV contains:

| Column | Description |
|--------|-------------|
| `date` | Daily observation date |
| `rainfall` | Basin-average rainfall (mm/day) |

---

# 3. Temperature Dataset

**Source:** India Meteorological Department (IMD) Daily Gridded Temperature Dataset. <Cite ref="turn525328search1"/>

### Description

Daily gridded maximum and minimum temperature observations over India.

### Coverage

- **Time Period:** 2001–2025.
- **Frequency:** Daily.
- **Variables:** Tmax and Tmin.

### Raw Dataset

```text
tmax/
    2001.GRD
    ...
    2025.GRD

tmin/
    2001.GRD
    ...
    2025.GRD
```

### Preprocessing

Script used:

```text
scripts/convert_temperature.py
```

Operations performed:

- Read binary `.GRD` files using NumPy.
- Converted missing value `99.9` to `NaN`.
- Extracted Krishna and Cauvery basin temperature values.
- Generated separate Tmax and Tmin CSV files.

### Output Files

```text
data/interim/
├── krishna_tmax.csv
├── krishna_tmin.csv
├── cauvery_tmax.csv
└── cauvery_tmin.csv
```

Each CSV contains:

| Column | Description |
|--------|-------------|
| `date` | Daily observation date |
| `tmax` / `tmin` | Basin-average daily temperature (°C) |

---

# 4. Oceanic Niño Index (ONI)

**Source:** NOAA Climate Prediction Center (CPC). <Cite ref="turn525328search1"/>

### Description

Monthly Oceanic Niño Index representing sea surface temperature anomalies in the Niño 3.4 region of the Pacific Ocean.

### Coverage

- **Time Period:** 1950–2025.
- **Frequency:** Monthly.

### Raw Dataset

```text
oni.ascii.txt
```

Columns:

- `SEAS`
- `YR`
- `TOTAL`
- `ANOM`

### Preprocessing

Script used:

```text
scripts/convert_oni.py
```

Operations performed:

- Parsed ASCII text using Pandas.
- Converted seasonal codes (`DJF`, `JFM`, `FMA`, etc.) into monthly timestamps.
- Kept the `ANOM` column as the ONI value.
- Exported monthly CSV.

### Output File

```text
data/interim/oni.csv
```

Columns:

| Column | Description |
|--------|-------------|
| `date` | First day of each month |
| `oni` | Oceanic Niño Index anomaly |

---

# Data Conversion Pipeline

| Raw File | Conversion Script | Output CSV |
|----------|-------------------|------------|
| `oni.ascii.txt` | `convert_oni.py` | `oni.csv` |
| `*.nc` | `convert_rainfall.py` | `krishna_rainfall.csv`, `cauvery_rainfall.csv` |
| `*.GRD` | `convert_temperature.py` | `krishna_tmax.csv`, `krishna_tmin.csv`, `cauvery_tmax.csv`, `cauvery_tmin.csv` |
| State Streamflow CSVs | `convert_streamflow.py` | `krishna_streamflow.csv`, `cauvery_streamflow.csv` |

---

# Final Dataset Statistics

| Dataset | Rows | Columns |
|---------|------|---------|
| Krishna Rainfall | 9,131 | 2 |
| Krishna Tmax | 9,131 | 2 |
| Krishna Tmin | 9,131 | 2 |
| Krishna Streamflow | 343,261 | 7 |
| Cauvery Rainfall | 9,131 | 2 |
| Cauvery Tmax | 9,131 | 2 |
| Cauvery Tmin | 9,131 | 2 |
| Cauvery Streamflow | 266,597 | 7 |
| ONI | 919 | 2 |

---

# Next Processing Step

The converted CSV datasets stored in `data/interim/` will be used in **Phase 2 (Exploratory Data Analysis)** and **Phase 3 (Data Preprocessing & Feature Engineering)** to create the final model-ready datasets:

```text
data/processed/
├── krishna_master_dataset.csv
└── cauvery_master_dataset.csv
```

These master datasets will contain daily rainfall, temperature, ONI, and streamflow values aligned by date and will serve as input for the Linear Regression, LSTM, and Temporal Convolutional Network (TCN) models.

---

# References

1. India Meteorological Department (IMD) – Gridded Daily Rainfall and Temperature Datasets. <Cite refs={["turn525328search2","turn525328search0"]}/>
2. Central Water Commission (CWC) / India-WRIS – Hydrological Observation and River Discharge Data. <Cite refs={["turn525328search6","turn525328search5"]}/>
3. NOAA Climate Prediction Center – Oceanic Niño Index (ONI). <Cite ref="turn525328search1"/>