# 🗺️ Project Roadmap — River Streamflow Forecasting using TCN

> **Project:** Deep Learning Time-Series Forecasting of River Streamflow in Drought-Prone Basins (Krishna/Cauvery) under El Niño
>
> **Course:** Project Based Learning (Semester V)
>
> **Institute:** K. J. Somaiya Institute of Technology

---

## 📌 Project Vision

Build an end-to-end AI-powered web application that predicts river streamflow using historical hydrological and climatic data. The project compares a traditional Machine Learning model (**Linear Regression**) with two Deep Learning models (**LSTM** and **Temporal Convolutional Network**) and deploys the best-performing model using **FastAPI** and **React**.

---

# 🏗️ Overall Project Architecture

```text
                 Historical Datasets
       (Streamflow + Rainfall + Temperature + ONI)
                            │
                            ▼
                 Data Collection & Validation
                            │
                            ▼
            Exploratory Data Analysis (EDA)
                            │
                            ▼
              Data Preprocessing & Cleaning
                            │
                            ▼
                 Feature Engineering
                            │
          ┌─────────────────┼──────────────────┐
          ▼                 ▼                  ▼
 Linear Regression         LSTM               TCN
   (Baseline)        (Deep Learning)   (Deep Learning)
          └─────────────────┼──────────────────┘
                            ▼
                 Model Evaluation & Comparison
                            │
                            ▼
               Best Performing Model (.pt/.pkl)
                            │
                            ▼
                  FastAPI Prediction Backend
                            │
                            ▼
                PostgreSQL Prediction Storage
                            │
                            ▼
                  React Web Dashboard
                            │
                            ▼
                    Docker + Deployment
```

---

# 📍 Phase 0 — Project Foundation

**Goal:** Prepare the repository and development environment.

### Learn

- GitHub project structure.
- Virtual environments.
- Requirements management.

### Implement

- Project folder structure.
- README.md
- ROADMAP.md
- TODO.md
- requirements.txt
- .gitignore

### Deliverables

- Ready-to-use GitHub repository.
- Development environment configured.

**Status:** ✅ Completed

---

# 📍 Phase 1 — Dataset Collection & Understanding

**Goal:** Collect and understand all datasets required for forecasting.

### Learn

- Time-series datasets.
- Pandas DataFrames.
- DateTime handling.
- Dataset inspection.

### Datasets

| Dataset | Source | Purpose |
|---------|--------|---------|
| River Streamflow | India-WRIS / CWC | Target variable |
| Rainfall | IMD | Weather feature |
| Temperature | IMD | Weather feature |
| Oceanic Niño Index (ONI) | NOAA CPC | El Niño feature |

### Implementation

- Load all datasets.
- Convert date columns.
- Inspect data.
- Check missing values.
- Create data dictionary.

### Deliverables

```
data/raw/
streamflow.csv
rainfall.csv
temperature.csv
oni.csv

docs/data_dictionary.md
```

### Skills Gained

- Pandas
- CSV handling
- DateTime processing

---

# 📍 Phase 2 — Exploratory Data Analysis (EDA)

**Goal:** Understand trends, distributions, correlations, and seasonality.

### Learn

- Line plots.
- Histograms.
- Box plots.
- Heatmaps.
- Correlation analysis.
- Outlier detection.

### Implementation

Generate visualizations for:

- Streamflow over time.
- Rainfall trends.
- Temperature trends.
- ONI trends.
- Monthly streamflow.
- Seasonal streamflow.
- Correlation matrix.
- Missing value analysis.

### Deliverables

```
notebooks/02_eda.ipynb

outputs/eda/
├── streamflow_trend.png
├── rainfall_trend.png
├── temperature_trend.png
├── oni_trend.png
├── monthly_streamflow.png
├── correlation_heatmap.png
└── outlier_boxplot.png
```

### Skills Gained

- Matplotlib
- Time-series visualization
- Data interpretation

---

# 📍 Phase 3 — Data Preprocessing

**Goal:** Convert raw datasets into a clean training dataset.

### Learn

- Missing value handling.
- Interpolation.
- Scaling.
- Chronological train-test split.

### Implementation

- Merge datasets.
- Remove duplicates.
- Fill missing values.
- Normalize features.
- Split train, validation, and test datasets.

### Deliverables

```
data/processed/
final_dataset.csv
```

### Skills Gained

- Scikit-learn preprocessing.
- Data cleaning workflow.

---

# 📍 Phase 4 — Feature Engineering

**Goal:** Create meaningful temporal features for forecasting.

### Learn

| Topic | Purpose |
|-------|---------|
| Lag Features | Previous observations |
| Rolling Mean | Short-term trends |
| Rolling Std | Variability |
| Month & Season | Seasonality |
| ONI Category | Climate condition |

### Implementation

Create:

- Lag-1
- Lag-3
- Lag-7
- Rolling rainfall average.
- Rolling temperature average.
- Month feature.
- Season feature.
- El Niño category.

### Deliverables

```
data/processed/model_dataset.csv
```

### Skills Gained

- Feature Engineering.
- Time-series transformations.

---

# 📍 Phase 5 — Linear Regression Baseline

**Goal:** Build the first prediction model.

### Learn

- Supervised Regression.
- Linear Regression.
- Evaluation metrics.

### Implementation

- Train baseline model.
- Predict streamflow.
- Calculate MAE.
- Calculate RMSE.
- Calculate R² Score.

### Deliverables

```
models/linear_regression.pkl

outputs/linear_regression/
├── actual_vs_predicted.png
├── residual_plot.png
└── metrics.json
```

### Skills Gained

- Scikit-learn model training.
- Baseline evaluation.

---

# 📍 Phase 6 — Time-Series Dataset Preparation

**Goal:** Prepare sequential data for deep learning models.

### Learn

- Sliding Window.
- Forecast Horizon.
- PyTorch Dataset.
- DataLoader.

### Implementation

Convert tabular data into sequences.

Example:

```
Input (30 Days)
↓
[Day1 ... Day30]

Output
↓
Day31 Streamflow
```

### Deliverables

```
src/training/
dataset.py
window_generator.py
```

### Skills Gained

- PyTorch Dataset API.
- Sequence generation.

---

# 📍 Phase 7 — LSTM Model Development

**Goal:** Train a Long Short-Term Memory model.

### Learn

- Neural Networks.
- LSTM architecture.
- Hidden State.
- Cell State.
- Training loop.

### Implementation

- Build LSTM.
- Train model.
- Validate model.
- Save model.
- Generate prediction plots.

### Deliverables

```
models/lstm.pt

outputs/lstm/
├── training_loss.png
├── validation_loss.png
└── prediction_graph.png
```

### Skills Gained

- PyTorch.
- LSTM implementation.
- Deep learning workflow.

---

# 📍 Phase 8 — Temporal Convolutional Network (TCN)

**Goal:** Implement the project's primary deep learning model.

### Learn

| Topic | Why Learn |
|-------|-----------|
| 1D Convolution | Time-series feature extraction |
| Causal Convolution | Prevent future leakage |
| Dilated Convolution | Capture long-term dependencies |
| Residual Blocks | Stable deep networks |

### Implementation

- Build TCN blocks.
- Train model.
- Validate model.
- Save trained model.
- Plot prediction graphs.

### Deliverables

```
models/tcn.pt

outputs/tcn/
├── training_loss.png
├── validation_loss.png
└── prediction_graph.png
```

### Skills Gained

- Temporal Convolutional Networks.
- Convolution for sequential data.

---

# 📍 Phase 9 — Model Evaluation & Comparison

**Goal:** Compare all forecasting models.

### Learn

- MAE
- RMSE
- NSE
- R² Score
- Residual Analysis

### Implementation

Compare:

| Model | Metrics |
|-------|---------|
| Linear Regression | MAE, RMSE, R² |
| LSTM | MAE, RMSE, R² |
| TCN | MAE, RMSE, R² |

Generate comparison graphs.

### Deliverables

```
outputs/model_comparison/
├── metrics_table.csv
├── mae_comparison.png
├── rmse_comparison.png
├── r2_comparison.png
└── best_model_summary.md
```

### Skills Gained

- Model benchmarking.
- Hydrological evaluation metrics.

---

# 📍 Phase 10 — FastAPI Backend

**Goal:** Serve the trained model using REST APIs.

### Learn

- FastAPI.
- Pydantic.
- Model inference.
- Swagger UI.

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/health` | Health check |
| GET | `/models` | Available models |
| POST | `/predict` | Predict streamflow |

### Deliverables

```
backend/
├── main.py
├── api/
├── services/
├── schemas/
└── ml/
```

### Skills Gained

- AI model serving.
- REST API development.

---

# 📍 Phase 11 — Database Integration

**Goal:** Store prediction history.

### Learn

- PostgreSQL.
- SQLAlchemy ORM.
- Alembic migrations.

### Tables

- Users
- Predictions
- Model Metrics

### Deliverables

```
backend/database/
├── models.py
├── crud.py
├── database.py
└── migrations/
```

### Skills Gained

- Database integration.
- ORM workflow.

---

# 📍 Phase 12 — React Frontend Dashboard

**Goal:** Build an interactive prediction dashboard.

### Learn

- React Hooks.
- Axios.
- Forms.
- Charts.

### Pages

| Page | Feature |
|------|---------|
| Home | Project overview |
| Predict | Streamflow prediction form |
| Prediction History | Previous predictions |
| Model Comparison | Metrics & charts |
| About | Project information |

### Deliverables

```
frontend/
├── pages/
├── components/
├── services/
└── charts/
```

### Skills Gained

- React.
- API integration.
- Dashboard development.

---

# 📍 Phase 13 — Deployment & Final Documentation

**Goal:** Deploy the complete application.

### Learn

- Docker.
- Docker Compose.
- Environment variables.
- Vercel.
- Render.

### Deployment Stack

| Component | Platform |
|-----------|----------|
| Frontend | Vercel |
| Backend | Render / VPS |
| Database | Neon PostgreSQL |
| Model Storage | Backend Server |

### Deliverables

- Live website.
- Docker configuration.
- Deployment guide.

---

# 📚 Learning Roadmap (Study Before Each Phase)

| Phase | Study Topics |
|-------|--------------|
| 1 | Pandas, NumPy, DateTime |
| 2 | Matplotlib, EDA, Correlation |
| 3 | Missing Values, Scaling, Train-Test Split |
| 4 | Feature Engineering, Lag Features, Rolling Window |
| 5 | Linear Regression, MAE, RMSE, R² |
| 6 | PyTorch Tensors, Dataset, DataLoader |
| 7 | LSTM, Neural Networks, Optimizers |
| 8 | 1D Convolution, TCN, Dilated & Causal Convolution |
| 9 | Model Evaluation, NSE, Residual Analysis |
| 10 | FastAPI, Pydantic, Model Inference |
| 11 | PostgreSQL, SQLAlchemy, Alembic |
| 12 | React, Axios, Recharts |
| 13 | Docker, Deployment, Environment Variables |

---

# 🎯 Final Deliverables

- ✅ Clean processed dataset.
- ✅ Three trained models (Linear Regression, LSTM, TCN).
- ✅ Model comparison report with MAE, RMSE, NSE, and R².
- ✅ FastAPI backend serving predictions.
- ✅ PostgreSQL database storing prediction history.
- ✅ React dashboard for streamflow forecasting.
- ✅ Dockerized deployment.
- ✅ Final PBL report, PPT, and GitHub documentation.

---

# 🏁 Success Criteria

- [ ] Historical datasets collected and documented.
- [ ] Complete EDA with visual insights.
- [ ] Clean feature-engineered dataset.
- [ ] Linear Regression baseline completed.
- [ ] LSTM model trained and evaluated.
- [ ] TCN model trained and evaluated.
- [ ] Best model selected using evaluation metrics.
- [ ] Backend API integrated with trained model.
- [ ] Frontend dashboard connected to backend.
- [ ] Project deployed and documented.