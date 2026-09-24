# 🌊 River Streamflow Forecasting using Temporal Convolutional Networks (TCN)

An end-to-end Deep Learning project that predicts river streamflow in drought-prone river basins (Krishna/Cauvery) under the influence of **El Niño** using **Temporal Convolutional Networks (TCN)**.

This project is being developed as part of the **Project Based Learning (PBL)** course and follows a structured learning-first approach, where every concept is learned and implemented step by step.

---

## 📌 Problem Statement

Develop a high-accuracy time-series forecasting model to predict future river streamflow in drought-prone basins such as **Krishna** and **Cauvery** using **Temporal Convolutional Networks (TCN)** while considering climatic factors such as **El Niño**.

---

## 🎯 Project Objectives

- Understand river streamflow forecasting.
- Analyze the impact of El Niño on river discharge.
- Perform exploratory data analysis on hydrological datasets.
- Build a baseline Machine Learning model.
- Build an LSTM model for time-series forecasting.
- Build a Temporal Convolutional Network (TCN).
- Compare model performance.
- Deploy the best model as a web application.

---

## 🏗️ System Architecture

```text
                    User
                      │
                      ▼
              React Frontend
                      │
                      ▼
              FastAPI Backend
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
 PostgreSQL Database          Trained AI Model
        │                           │
        └─────────────┬─────────────┘
                      ▼
              Streamflow Prediction
```

---

## 🛠️ Tech Stack

### Programming
- Python

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib

### Machine Learning
- Scikit-learn

### Deep Learning
- PyTorch

### Backend
- FastAPI

### Frontend
- React

### Database
- PostgreSQL

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
river-streamflow-forecasting/
│
├── README.md
├── ROADMAP.md
├── TODO.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── research/
│   ├── diagrams/
│   └── report/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│
├── src/
│
├── models/
│
├── backend/
│
├── frontend/
│
└── outputs/
```

---

## 🚀 Development Workflow

```text
Research
    ↓
Dataset Collection
    ↓
Exploratory Data Analysis
    ↓
Data Preprocessing
    ↓
Feature Engineering
    ↓
Machine Learning Baseline
    ↓
LSTM Development
    ↓
TCN Development
    ↓
Model Comparison
    ↓
Backend Development
    ↓
Frontend Development
    ↓
Deployment
```

---

## 📊 Models

This project compares multiple approaches for river streamflow forecasting.

| Model | Category | Status |
|--------|----------|--------|
| Linear Regression | Machine Learning | ⏳ Planned |
| LSTM | Deep Learning | ⏳ Planned |
| Temporal Convolutional Network (TCN) | Deep Learning | ⏳ Planned |

---

## 📈 Evaluation Metrics

The models will be evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 📅 Project Roadmap

- [x] Problem Understanding
- [x] River Streamflow Basics
- [x] El Niño Basics
- [x] Time-Series Forecasting Basics
- [x] LSTM Overview
- [x] TCN Overview
- [ ] Dataset Collection
- [ ] Exploratory Data Analysis
- [ ] Data Preprocessing
- [ ] Feature Engineering
- [ ] Linear Regression
- [ ] LSTM Implementation
- [ ] TCN Implementation
- [ ] Model Comparison
- [ ] Backend Development
- [ ] Frontend Development
- [ ] Deployment

---

## 📚 Learning Approach

This repository follows a **Learn → Implement → Apply** methodology.

For every phase:

1. Learn the underlying concepts.
2. Build a small implementation.
3. Apply the concept to the project.
4. Document the learnings.

---

## 📖 Documentation

- `ROADMAP.md` → Complete learning and development roadmap.
- `TODO.md` → Task tracker.
- `CHANGELOG.md` → Daily development log.

---

## 🎓 Project Status

**Current Phase:** Project Planning & Learning

---

## 👨‍💻 Author

**Yadnyesh Hemant Halde**

B.Tech – Artificial Intelligence & Data Science

K. J. Somaiya Institute of Technology

---

## ⭐ Future Scope

- Real-time forecasting
- Integration with weather APIs
- Multi-river support
- Interactive dashboard
- Cloud deployment
- Model optimization


## Data Source 
- ONI 
- Temperature 
  tmax - https://www.imdpune.gov.in/cmpg/Griddata/Max_1_Bin.html
  tmin - https://www.imdpune.gov.in/cmpg/Griddata/Min_1_Bin.html
- Rainfall
- Streamflow
- Boundaries 