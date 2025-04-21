# 🔥 Forest Fire Burned Area Prediction using Machine Learning

## 🎓 Thesis-Aligned Research Project
This project aims to predict the **burned area of forest fires** using structured meteorological and environmental data. It is a critical sub-component of my **Master’s Thesis** titled:

> **"AI-Powered Wildfire Detection and Monitoring Using Satellite Imagery with Explainable Deep Learning Models"**

---

## 🌍 Project Objective

The main goal is to develop a supervised machine learning model that can **predict the size of forest fire spread (area)** using:
- Fire weather indices (FFMC, DMC, DC, ISI)
- Meteorological conditions (temperature, humidity, wind, rainfall)
- Seasonal variables (month, day)

Such predictive modeling is essential for:
- Early alert systems
- Firefighting resource allocation
- Environmental risk planning

---

## 📊 Dataset

- Source: Kaggle – [Forest Fires Data Set](https://www.kaggle.com/datasets)
- Total observations: 517
- Target variable: `area` (ha) burned
- Preprocessing:
  - Removed duplicates and rows with area = 0 (as they introduce noise)
  - Applied `log1p()` transformation to normalize skewed area distribution
  - One-hot encoded categorical variables (`month`, `day`)

---

## 🧠 Machine Learning Models

| Model                | Type         | Purpose         | R² Score |
|---------------------|--------------|------------------|----------|
| Linear Regression   | Supervised   | Baseline         | ~1.00    |
| Random Forest Regressor | Ensemble Tree | Final Model | ~1.00    |

📌 *Note: High accuracy achieved post noise filtering and balanced target values.*

---

## ✅ Results

- **Mean Squared Error** reduced significantly after log-transformation and filtering
- **R² Score ≈ 1.0** using `RandomForestRegressor` indicates excellent fit on cleaned data
- Visual comparison between predicted and actual `log(area)` confirms accurate predictions

![Prediction vs Actual](images/prediction_vs_actual.png)

---

## 🔍 Visualizations

- Correlation heatmap
- Area distribution (before/after transformation)
- Model predictions vs actual values (scatter plot)

---

## 🔗 Link to Master Thesis

This structured ML pipeline is aligned with my thesis work on:
- **Satellite-based wildfire detection using deep learning**
- **Explainable AI models (SHAP, Grad-CAM)** for transparency and trust
- **Multimodal learning** combining tabular data with imagery

---

## 📬 Contact & Collaboration

I'm open to collaboration on:
- Remote sensing & wildfire modeling 🛰️  
- Climate AI & sustainability 🔥🌿  
- Multimodal machine learning research 🧠  
- Academic publishing and thesis co-review 📚

Reach me via [LinkedIn](https://www.linkedin.com/in/dilrabokhidirova) or GitHub issues.

---

## 🧪 Future Work

- Integrate with Sentinel-2 satellite imagery
- Implement U-Net segmentation to detect fire zones
- Use SHAP for model interpretability
- Deploy as a Streamlit or Flask web app

---

## 🧠 Key Learnings

- Real-world data is often noisy — preprocessing is vital
- Regression modeling can uncover powerful patterns in environmental science
- ML is not only prediction — it's a tool for **policy-making**, **disaster response**, and **climate resilience**

---

## 🛠️ Tech Stack

- Python 3.9
- pandas, numpy
- seaborn, matplotlib
- scikit-learn
- Jupyter Notebook

---


https://www.kaggle.com/code/dilrabonu/forest-fire
