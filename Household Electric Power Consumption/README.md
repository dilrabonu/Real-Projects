
# 🔌 Household Power Consumption – ML Classification Project

This project aims to predict **high vs low household electricity usage** using supervised machine learning algorithms such as **Logistic Regression** and **Decision Tree Classifier**. The dataset used includes over **2 million records** of minute-level power consumption, voltage, and sub-metering data from a real household in France.

---

## 📊 Dataset Overview

- **Source**: UCI Machine Learning Repository / Kaggle
- **Original Format**: Time-stamped `.csv` with electrical measurements
- **Records**: ~2,000,000+
- **Features**:
  - `Global_active_power`, `Global_reactive_power`
  - `Voltage`, `Global_intensity`
  - `Sub_metering_1`, `_2`, `_3`
  - `Date` and `Time` (combined into `Datetime`)
  
---

## 🎯 Objective

Create a binary classification model to **detect high power usage events**, enabling:
- Smart grid responses
- Energy-efficient systems
- Forecasting extreme usage patterns

We define **high usage** as:
```python
Target = 1 if Global_active_power > 4.0 kW else 0
🔄 Workflow
1. 🧹 Data Cleaning
Converted all object columns to float64

Parsed Date + Time into a unified Datetime column

Handled missing values using median imputation

2. 📈 Exploratory Data Analysis (EDA)
Distribution of global power

Boxplots for voltage and current by class

Correlation heatmap for feature understanding

Target class imbalance review

3. 🧠 Model Training & Evaluation
Logistic Regression
ROC AUC: 0.99995

Precision, Recall, F1 for class 1 (high usage): 0.99

Decision Tree (max depth = 5)
ROC AUC: 1.00

Complete separation of classes

Interpretable feature splits

4. 📊 Visualizations
Confusion Matrix Heatmaps

ROC Curves

Feature Importance (for tree-based models)

💡 Key Learnings
Logistic Regression performs incredibly well with clear, clean features

Class imbalance needs careful consideration (F1 & ROC > Accuracy)

Visualization is critical for model explainability

Feature engineering with domain knowledge (threshold selection) matters more than complex models
https://www.kaggle.com/code/dilrabonu/household-power-consumption
