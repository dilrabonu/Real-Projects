# 📱 Average Daily Screen Time for Children – ML Analysis

Welcome to this machine learning project where we analyze and predict **average daily screen time** in children based on demographic and temporal factors using various models including **Linear Regression**, **Random Forest**, and **XGBoost**.

---

## 📦 Dataset Description

The dataset contains insights on how children's screen time varies based on:

- **Age**
- **Gender**
- **Screen Time Type**: Educational, Recreational, Total
- **Day Type**: Weekday vs Weekend
- **Sample Size** per group

🗂 File: `screen_time.csv`  
🧮 Total entries: 108 rows  
📊 Source: [Kaggle](https://www.kaggle.com/datasets)

---

## 🎯 Project Goals

1. **Explore patterns in children's screen time behavior**
2. **Analyze how age, gender, and day type influence screen time**
3. **Predict total average screen time using ML models**
4. **Evaluate model performance using RMSE, MAE, and R²**
5. **Identify most important features influencing screen time**

---

## 🧪 ML Models Used

- ✅ Linear Regression (Baseline)
- 🌲 Random Forest Regressor
- ⚡ XGBoost Regressor (with hyperparameter tuning)
- 🧪 K-Fold & LOOCV Cross-Validation

---

## 📊 Key Findings

- **Age** is the most significant predictor of screen time.
- **Gender** had very little impact on overall screen time.
- **Weekend screen time** was slightly higher than weekdays.
- XGBoost performed best on test data (R² ≈ 0.99), but showed instability under K-Fold CV due to small dataset size.

---

## 📁 Folder Structure


