
# 🌍 Global CO₂ Emissions Analysis & Forecasting

Welcome to my end-to-end machine learning project exploring global CO₂ emissions data. This project leverages real-world environmental data to understand, visualize, cluster, and predict emission trends across countries using Python and scikit-learn.

---

## 📌 Project Overview

In this project, I worked with CO₂ emission data from OECD spanning the years **2000 to 2018**, aiming to:

- Understand global emission trends over time
- Predict 2018 emissions using historical data
- Cluster countries based on emission behavior
- Generate insights for policy and planning using visual analytics

---

## 📁 Dataset

- **Source**: OECD (2021) International Input-Output Database
- **File Used**: `_COE28282_Emissions2C_Emissions_Intensities2C_and_Emissions_Multipliers.csv`
- **Features**:
  - Country, ISO codes, CO₂ emission indicators
  - Emission values from 2000 to 2018
  - Source metadata and environmental descriptors

---

## 🔧 Technologies Used

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Machine Learning**: scikit-learn (LinearRegression, KMeans, StandardScaler)
- **Visualization**: Seaborn heatmaps, Matplotlib scatter and line plots
- **Notebook Environment**: Kaggle Kernels

---

## 🧠 What I Did

### 📈 1. Exploratory Data Analysis (EDA)
- Cleaned column names for Pythonic usage
- Checked for missing values and duplicates
- Used `.groupby()` and `.sum()` to aggregate emissions by country and year

### 🧮 2. Supervised Learning: Linear Regression
- Trained a model to predict **2018 emissions** using 2000–2017 data
- Achieved high performance:
  - **R² Score**: `0.973`
  - **RMSE**: `130.36`

### 📊 3. Unsupervised Learning: KMeans Clustering
- Standardized country-year features
- Clustered countries into 4 emission behavior groups
- Visualized clusters in 2D space using scaled components

### 🎨 4. Visualization Highlights
- Time-series plots for top 10 emitting countries
- Heatmap of emissions (2000–2018)
- Scatter plot of actual vs predicted values
- Cluster plot of grouped countries

---

## 📊 Results Summary

| Metric | Value |
|--------|-------|
| MAE | 32.96 |
| MSE | 16,995 |
| RMSE | 130.36 |
| R² Score | 0.973 |

---

## 🔍 Insights & Takeaways

- Countries show strong linear trends in emissions — ideal for predictive modeling
- Clustering reveals distinct behavioral groups, helping in policy targeting
- Data-driven emission forecasting is feasible and actionable using historical patterns

---



https://www.kaggle.com/code/dilrabonu/global-co2-emission-real
