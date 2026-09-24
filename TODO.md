# River Streamflow Forecasting using TCN
> Project Based Learning (Semester V) • KJ Somaiya Institute of Technology

**Project:** Deep Learning Time-Series Forecasting of River Streamflow in Drought-Prone Basins (Krishna/Cauvery) under El Niño

---

## Project Progress

- [x] Phase 0 — Project Setup
- [ ] Phase 1 — Dataset Collection & Understanding
- [ ] Phase 2 — Exploratory Data Analysis (EDA)
- [ ] Phase 3 — Data Preprocessing
- [ ] Phase 4 — Feature Engineering
- [ ] Phase 5 — Linear Regression (Baseline Model)
- [ ] Phase 6 — Time-Series Sequence Generation
- [ ] Phase 7 — LSTM Model
- [ ] Phase 8 — Temporal Convolutional Network (TCN)
- [ ] Phase 9 — Model Evaluation & Comparison
- [ ] Phase 10 — FastAPI Backend
- [ ] Phase 11 — PostgreSQL Integration
- [ ] Phase 12 — React Frontend Dashboard
- [ ] Phase 13 — Deployment & Final Documentation

---

# Phase 0 — Project Setup

### Repository
- [x] Create GitHub repository.
- [x] Create project folder structure.
- [x] Add `README.md`.
- [x] Add `ROADMAP.md`.
- [x] Add `TODO.md`.
- [x] Add `.gitignore`.
- [x] Add `requirements.txt`.

### Environment
- [x] Create Python virtual environment.
- [x] Install required packages.
- [x] Verify project runs successfully.

**Git Commit:** `phase-0-project-setup`

---

# 📊 Phase 1 — Dataset Collection & Understanding

## Learn
- [x] Understand river streamflow dataset.
- [x] Understand rainfall dataset.
- [x] Understand temperature dataset.
- [x] Understand Oceanic Niño Index (ONI).
- [x] Learn Pandas basics for data loading.

## Implementation
- [x] Create `docs/data_dictionary.md`.
- [x] Download streamflow dataset (CWC / India-WRIS).
- [x] Download rainfall dataset (IMD).
- [x] Download temperature dataset (IMD).
- [x] Download ONI dataset (NOAA).
- [x] Create `01_dataset_understanding.ipynb`.
- [x] Load all CSV files.
- [x] Convert Date column to datetime.
- [x] Inspect data (`head`, `info`, `describe`).
- [x] Check missing values.
- [x] Document dataset observations.

## Deliverables
- [x] `data/raw/streamflow.csv`
- [x] `data/raw/rainfall.csv`
- [x] `data/raw/temperature.csv`
- [x] `data/raw/oni.csv`
- [x] `docs/data_dictionary.md`

**Git Commit:** `phase-1-dataset-understanding`

---

# 📈 Phase 2 — Exploratory Data Analysis (EDA)

## Learn
- [ ] Line plots.
- [ ] Histograms.
- [ ] Box plots.
- [ ] Correlation heatmaps.
- [ ] Seasonal analysis.

## Implementation
- [ ] Create `02_eda.ipynb`.
- [ ] Plot streamflow trend.
- [ ] Plot rainfall trend.
- [ ] Plot temperature trend.
- [ ] Plot ONI trend.
- [ ] Plot monthly average streamflow.
- [ ] Plot rainfall distribution.
- [ ] Detect outliers using box plots.
- [ ] Create correlation heatmap.
- [ ] Analyze missing values visually.
- [ ] Write EDA observations.

## Deliverables
- [ ] Save all graphs inside `outputs/eda/`.
- [ ] Complete EDA notebook.

**Git Commit:** `phase-2-complete-eda`

---

# 🧹 Phase 3 — Data Preprocessing

## Learn
- [ ] Missing value handling.
- [ ] Interpolation for time-series.
- [ ] Normalization.
- [ ] Standardization.
- [ ] Chronological train/test split.

## Implementation
- [ ] Create preprocessing notebook.
- [ ] Remove duplicate records.
- [ ] Handle missing values.
- [ ] Scale numerical features.
- [ ] Merge all datasets by Date.
- [ ] Split train/validation/test chronologically.
- [ ] Save processed dataset.

## Deliverables
- [ ] `data/processed/final_dataset.csv`
- [ ] Preprocessing notebook.

**Git Commit:** `phase-3-preprocessing`

---

# ⚙️ Phase 4 — Feature Engineering

## Learn
- [ ] Lag features.
- [ ] Rolling window features.
- [ ] Moving averages.
- [ ] Seasonality features.
- [ ] ONI category feature.

## Implementation
- [ ] Create Lag-1 streamflow.
- [ ] Create Lag-3 streamflow.
- [ ] Create Lag-7 streamflow.
- [ ] Create 7-day rolling rainfall average.
- [ ] Create rolling temperature average.
- [ ] Extract Month.
- [ ] Extract Season.
- [ ] Add El Niño category from ONI.
- [ ] Save engineered dataset.

## Deliverables
- [ ] `data/processed/model_dataset.csv`

**Git Commit:** `phase-4-feature-engineering`

---

# 📉 Phase 5 — Linear Regression Baseline

## Learn
- [ ] Linear Regression.
- [ ] Regression metrics.
- [ ] Model training workflow.

## Implementation
- [ ] Create `05_linear_regression.ipynb`.
- [ ] Train Linear Regression model.
- [ ] Predict streamflow.
- [ ] Calculate MAE.
- [ ] Calculate RMSE.
- [ ] Calculate R² Score.
- [ ] Plot Actual vs Predicted graph.
- [ ] Save trained model.

## Deliverables
- [ ] `models/linear_regression.pkl`
- [ ] Baseline metrics report.

**Git Commit:** `phase-5-linear-regression`

---

# 🧠 Phase 6 — Time-Series Sequence Generation

## Learn
- [ ] Sliding window.
- [ ] Forecast horizon.
- [ ] Sequence generation.

## Implementation
- [ ] Create 30-day input sequences.
- [ ] Create prediction labels.
- [ ] Convert data into tensors.
- [ ] Build PyTorch Dataset.
- [ ] Build DataLoader.

## Deliverables
- [ ] Sequence generation notebook.
- [ ] PyTorch Dataset module.

**Git Commit:** `phase-6-sequence-generation`

---

# 🔁 Phase 7 — LSTM Model

## Learn
- [ ] PyTorch basics.
- [ ] LSTM architecture.
- [ ] Hidden state & Cell state.
- [ ] Loss function.
- [ ] Optimizer.

## Implementation
- [ ] Build LSTM model.
- [ ] Create training loop.
- [ ] Train model.
- [ ] Validate model.
- [ ] Save trained model.
- [ ] Plot training loss.
- [ ] Plot validation loss.
- [ ] Plot prediction graph.

## Deliverables
- [ ] `models/lstm.pt`
- [ ] Loss graphs.
- [ ] Prediction graphs.

**Git Commit:** `phase-7-lstm-model`

---

# 🌊 Phase 8 — Temporal Convolutional Network (TCN)

## Learn
- [ ] 1D Convolution.
- [ ] Causal Convolution.
- [ ] Dilated Convolution.
- [ ] Residual Blocks.
- [ ] Receptive Field.

## Implementation
- [ ] Build Residual Block.
- [ ] Build TCN architecture.
- [ ] Train TCN model.
- [ ] Validate model.
- [ ] Save trained model.
- [ ] Plot loss curves.
- [ ] Plot prediction graph.

## Deliverables
- [ ] `models/tcn.pt`
- [ ] TCN prediction notebook.

**Git Commit:** `phase-8-tcn-model`

---

# 📊 Phase 9 — Model Evaluation & Comparison

## Learn
- [ ] RMSE.
- [ ] MAE.
- [ ] NSE.
- [ ] R² Score.
- [ ] Residual analysis.

## Implementation
- [ ] Evaluate Linear Regression.
- [ ] Evaluate LSTM.
- [ ] Evaluate TCN.
- [ ] Create comparison table.
- [ ] Plot MAE comparison.
- [ ] Plot RMSE comparison.
- [ ] Plot R² comparison.
- [ ] Select best-performing model.

## Deliverables
- [ ] `outputs/model_comparison.csv`
- [ ] `outputs/model_comparison_graphs/`

**Git Commit:** `phase-9-model-comparison`

---

# ⚡ Phase 10 — FastAPI Backend

## Learn
- [ ] FastAPI project structure.
- [ ] Pydantic schemas.
- [ ] Model inference.
- [ ] API testing using Swagger / curl.

## Implementation
- [ ] Create FastAPI project.
- [ ] Load trained model.
- [ ] Create `/predict` endpoint.
- [ ] Create `/health` endpoint.
- [ ] Create `/models` endpoint.
- [ ] Validate inputs.
- [ ] Return prediction response.

## Deliverables
- [ ] Working FastAPI backend.
- [ ] Swagger documentation.

**Git Commit:** `phase-10-fastapi-backend`

---

# 🗄️ Phase 11 — PostgreSQL Integration

## Learn
- [ ] PostgreSQL.
- [ ] SQLAlchemy ORM.
- [ ] Alembic migrations.

## Implementation
- [ ] Create Prediction table.
- [ ] Store prediction history.
- [ ] Fetch prediction history.
- [ ] Create CRUD operations.
- [ ] Connect backend to database.

## Deliverables
- [ ] PostgreSQL database schema.
- [ ] Prediction history API.

**Git Commit:** `phase-11-postgresql`

---

# 💻 Phase 12 — React Frontend

## Learn
- [ ] React components.
- [ ] React hooks.
- [ ] Axios.
- [ ] Charts.

## Implementation
- [ ] Home page.
- [ ] Prediction page.
- [ ] History page.
- [ ] Model comparison page.
- [ ] API integration.
- [ ] Display prediction charts.

## Deliverables
- [ ] Complete React dashboard.

**Git Commit:** `phase-12-react-dashboard`

---

# 🚀 Phase 13 — Deployment & Documentation

## Learn
- [ ] Docker.
- [ ] Environment variables.
- [ ] Deployment workflow.

## Implementation
- [ ] Dockerize backend.
- [ ] Deploy FastAPI.
- [ ] Deploy React.
- [ ] Connect PostgreSQL.
- [ ] Update README with setup instructions.
- [ ] Record demo video.
- [ ] Final testing.

## Deliverables
- [ ] Live website.
- [ ] Final documentation.
- [ ] Final report.

**Git Commit:** `phase-13-deployment`

---

# 🎓 Viva Preparation Checklist

## Machine Learning
- [ ] Supervised Learning.
- [ ] Regression.
- [ ] Feature Engineering.
- [ ] Evaluation Metrics.

## Deep Learning
- [ ] Neural Networks.
- [ ] LSTM.
- [ ] TCN.
- [ ] 1D Convolution.
- [ ] Dilated Convolution.
- [ ] Causal Convolution.

## Project
- [ ] Explain complete architecture.
- [ ] Explain dataset pipeline.
- [ ] Explain model comparison.
- [ ] Explain backend flow.
- [ ] Explain frontend flow.

---

# 📅 Weekly Progress Tracker

| Week | Status |
|-------|--------|
| Week 1 | ⬜ Dataset + EDA |
| Week 2 | ⬜ Preprocessing + Feature Engineering |
| Week 3 | ⬜ Linear Regression |
| Week 4 | ⬜ LSTM |
| Week 5 | ⬜ TCN |
| Week 6 | ⬜ Model Comparison |
| Week 7 | ⬜ Backend + Database |
| Week 8 | ⬜ Frontend + Deployment |

---

## 🏁 Final Goal

- [ ] End-to-End AI Streamflow Forecasting System.
- [ ] Compare Linear Regression, LSTM, and TCN.
- [ ] Deploy FastAPI + React application.
- [ ] Complete PBL report, PPT, and viva preparation.# 🌊 River Streamflow Forecasting using TCN
