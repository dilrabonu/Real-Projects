
# 🌊 Ocean Climate & Marine Biodiversity Prediction using Machine Learning

## 📌 Project Overview

This project explores how oceanic climate conditions impact marine biodiversity and coral bleaching events. Using a realistic marine dataset from Kaggle, we apply data science and machine learning techniques to analyze, visualize, and predict:

- 🐠 The number of **marine species observed**
- 🌡️ The occurrence of **marine heatwaves**
- 🧪 The severity of **coral bleaching**

---

## 🎯 Objectives

- Understand climate variables affecting biodiversity: **SST (Sea Surface Temperature), pH Level, Location**
- Detect ecological stress patterns via **advanced visualizations**
- Apply machine learning to:
  - 🔍 Predict **Marine Heatwaves** (Classification)
  - 📈 Estimate **Species Observed** (Regression)
- Tune and evaluate models using **GridSearchCV** and residual analysis

---

## 🧠 Machine Learning Models

### 1. `Marine Heatwave Prediction`
- **Type**: Classification
- **Model**: `RandomForestClassifier`
- **Features**: SST, pH, Species Observed, Bleaching Severity (encoded), Latitude, Longitude
- **Evaluation**: Precision, Recall, F1-score

### 2. `Species Observed Prediction`
- **Type**: Regression
- **Model**: `RandomForestRegressor`
- **Evaluation**: R² Score, MSE, Residual plots
- **Tuning**: GridSearchCV for best hyperparameters

---

## 📊 Exploratory Data Analysis (EDA)

- Distribution plots of **SST**, **pH**, and **Species**
- Boxplots for **outlier detection**
- Categorical breakdown of **Bleaching Severity**
- Geospatial scatter plot (Latitude vs Longitude) to visualize ecological risk zones

---

## 📁 Files

| File/Notebook | Description |
|---------------|-------------|
| `ocean_climate_eda.ipynb` | Data cleaning, visualization, outlier detection |
| `marine_ml_models.ipynb` | Model training, evaluation, and tuning |
| `visualizations/` | Saved plots (boxplots, scatter maps, residuals) |
| `data/` | Raw and cleaned datasets |
| `README.md` | Project documentation |

---

## 📌 Key Takeaways

- Climate data requires thoughtful preprocessing and encoding
- Even moderate R² scores can be meaningful in environmental data modeling
- **Latitude and Longitude** are powerful geospatial features
- Residual analysis is critical for diagnosing regression performance

---


https://www.kaggle.com/code/dilrabonu/ocean
