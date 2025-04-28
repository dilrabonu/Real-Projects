
# 🔥 AI-Powered Wildfire Prediction

Welcome to my Master's Thesis project: an AI-driven model to predict wildfire burnt areas using historical data, advanced feature engineering, and machine learning models. 🌎🔥

---

## 📚 Project Overview

Wildfires are one of the most destructive environmental phenomena, and their accurate prediction can save lives, ecosystems, and resources.

In this project, I built a machine learning pipeline that:
- Cleans and preprocesses wildfire burnt area datasets
- Engineers new features like **Decade**, **Continent**, and **Burn Severity Category**
- Applies **logarithmic transformations** to stabilize variance
- Trains and evaluates **Linear Regression** and **Random Forest** models
- Achieves an R² score **above 97%** on unseen test data

This is Phase 1 of a larger goal: integrating climate data for even stronger prediction models.

---

## 🚀 Key Achievements

- ✅ Performed complete **EDA (Exploratory Data Analysis)**
- ✅ Built **new features**: Decade, Burn Severity Category, Continent
- ✅ Applied **One-Hot Encoding** for categorical variables
- ✅ Trained **Linear Regression** and **Random Forest** regressors
- ✅ Achieved **outstanding predictive performance** (R² > 97%)
- ✅ Visualized **Predicted vs Actual** results
- ✅ Saved models and datasets for deployment

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **Scikit-learn**
- **Joblib** (for model serialization)

---

## 📊 Dataset Description

- Historical records of **Annual Area Burnt by Wildfires**.
- Columns:
  - `Entity`: Country name
  - `Year`: Year of the record
  - `Area_Burnt`: Total burnt area (scaled)
  - `Area_Burnt_Log`: Log-transformed burnt area
  - `Decade`: Derived decade from Year
  - `Area_Burnt_Category`: Binned severity of fires
  - `Continent`: Geographic grouping

---

## 📈 Model Performance

| Model | Mean Squared Error (MSE) | R² Score |
|:---|:---|:---|
| Linear Regression | 0.0335 | 0.9737 |
| Random Forest | 0.0344 | 0.9730 |

✅ Both models show excellent predictive performance, demonstrating the power of effective feature engineering!

---

## 📦 Saved Artifacts

- `wildfire_final_dataset.csv`
- `linear_regression_model.pkl`
- `random_forest_model.pkl`
- Train-Test splits (`X_train.npy`, `X_test.npy`, etc.)

---

## 🌟 What's Next? (Phase 2)

- Enrich dataset with **external climate and weather data** (temperature, rainfall, drought index)
- Train **advanced models** (XGBoost, LightGBM)
- Perform **feature importance analysis**
- Build a **Streamlit web app** to visualize and predict wildfires interactively

---

## 🤝 Let's Connect!

I am passionate about using **Data Science and AI** to solve critical environmental challenges.  
If you're interested in collaboration, research, or professional opportunities, feel free to connect!

https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/
---

---

![image](https://github.com/user-attachments/assets/8655ac6a-b3f9-4cb9-8a52-683cff1566bd)

https://www.kaggle.com/code/dilrabonu/wildfires

