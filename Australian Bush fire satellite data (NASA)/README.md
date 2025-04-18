# 🔥 Australian Wildfire Detection Using Satellite Data (NASA)  
## Unsupervised + Supervised Machine Learning with Explainability

This project is part of my master's thesis:  
**"AI-Powered Wildfire Detection and Monitoring Using Satellite Imagery with Explainable Deep Learning Models"**

It leverages real NASA satellite data (MODIS and VIIRS) to identify fire-prone zones across Australia, classify fire severity, and provide interpretable AI insights that support emergency response and climate monitoring efforts.

---

## 📂 Dataset

- Source: [NASA FIRMS Fire Data](https://earthdata.nasa.gov/active-fire-data)
- Files used:  
  - `fire_archive_M6_101673.csv`  
  - `fire_archive_V1_101674.csv`  
  - `fire_nrt_M6_101673.csv`  
  - `fire_nrt_V1_101674.csv`

Combined and processed into `processed_bushfire_data.csv`.

---

## 🎯 Project Objectives

- ✅ Detect spatial patterns of wildfire zones using **unsupervised clustering (KMeans)**
- ✅ Predict fire severity categories (**Low**, **Medium**, **High**) using **Random Forest Classifier**
- ✅ Interpret model decisions using **Permutation Feature Importance**
- ✅ Visualize fire intensity and clusters across Australia using maps and plots

---

## 📊 Machine Learning Pipeline

### 1. **Clustering (KMeans)**
- Features: `latitude`, `longitude`, `brightness`, `frp`
- Optimal clusters (k=4) found via **Elbow Method**
- Result: Clear geospatial fire zones based on regional behavior and intensity

### 2. **Classification (Random Forest)**
- Target: Fire Severity (based on `frp` thresholds)
- Accuracy: **98.1%**
- Features: `brightness`, `confidence`, `bright_t31`, `scan`, `track`, `latitude`, `longitude`

### 3. **Explainability**
- Used **Permutation Importance** to identify key features:
  - `brightness` and `confidence` were most influential
- Added decorators to time and log critical ML functions

---

## 📌 Results

- 🔥 Fire-prone zones discovered across Australia, especially along the Eastern coast
- 🔍 High accuracy in classifying fire severity for early intervention
- ✅ Aligned with UN SDG 13: **Climate Action** through data-driven wildfire mitigation

---

## 🧠 Thesis Relevance

This project is part of my Master’s thesis focused on combining satellite data with interpretable ML to improve wildfire monitoring systems. It explores both **unsupervised pattern discovery** and **supervised prediction with explainability**, enabling AI to support real-world climate challenges.

---

## 📎 Folder Structure



https://www.kaggle.com/code/dilrabonu/australian-bush-fire-satellite-data-nasa
