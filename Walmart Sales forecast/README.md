
# 🛒 Walmart Weekly Sales Forecasting with Machine Learning

📌 **Project Goal**: Predict Walmart's weekly sales per store and department using historical, promotional, and store metadata. This real-world use case supports better inventory planning, staffing, and marketing decisions in the retail industry.

---

## 📦 Dataset Overview

The dataset is composed of four CSV files:

| File             | Description                                              |
|------------------|----------------------------------------------------------|
| `train.csv`      | Historical weekly sales data per store & department     |
| `test.csv`       | Data for which weekly sales need to be predicted        |
| `features.csv`   | Additional data (temperature, fuel price, markdowns, etc.) |
| `stores.csv`     | Store-level metadata (type, size)                       |

---

## 🔧 ML Pipeline Overview

### ✅ 1. Data Preparation & Merging
- Merged all CSV files using common keys: `Store`, `Date`
- Handled missing values with forward fill and feature-based imputation

### 🧠 2. Feature Engineering
- Time-based features: `Year`, `Month`, `Week`
- Lag features: `Prev_Week_Sales`
- Rolling means: 4-week moving average
- One-hot encoding for `Store Type`

### 📈 3. Model Training & Evaluation
Trained and validated multiple regression models:

| Model      | RMSE (Validation) ↓ |
|------------|---------------------|
| LightGBM   | 3470.19              |
| XGBoost    | 3557.52              |
| **CatBoost** | ⭐ **3011.03**        ✅ Best Performer

Evaluation metric: **Root Mean Squared Error (RMSE)**

### 📤 4. Submission File
- Predictions were post-processed to clip negative sales (sales can't be negative)
- Final submission formatted with `Id` (Store_Dept_Date) and `Weekly_Sales`

---

## 📊 Model Performance Visualization

A bar chart was created to compare model performance visually:

![Model Comparison](model_comparison.png)

---

## 💡 Key Takeaways

- 🧩 Feature engineering on time-series data significantly improved model performance.
- 🧠 CatBoost handled categorical features and missing values with minimal preprocessing.
- 📦 Real-world data is messy — robust preprocessing is more important than complex models.
- 📈 Model performance (RMSE) can guide business impact in supply chain & retail operations.

---

## 🛠 Tech Stack

- **Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, LightGBM, XGBoost, CatBoost
- **Environment**: Kaggle Notebook (Docker Image: `kaggle/python`)

---

![image](https://github.com/user-attachments/assets/aca3a45b-9c97-4482-9579-70d83cc1d67e)

https://www.kaggle.com/code/dilrabonu/walmart-sales-forecast
