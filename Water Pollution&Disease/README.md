

the lionk of kaggle:
https://www.kaggle.com/code/dilrabonu/water-pollution-disease

# 🌍 Water Pollution & Disease Risk Prediction using Machine Learning

A full end-to-end machine learning project to **predict high-risk areas** for waterborne diseases (Diarrhea, Cholera, Typhoid) using global water pollution and healthcare data.

> 🚨 This project applies real-world ML techniques to a public health challenge — and highlights model evaluation, ethical trade-offs, and meaningful predictions.

---

## 📌 Project Overview

- **Dataset**: 3,000 records, 24 features (environmental, demographic, and health indicators)
- **Goal**: Predict whether a region is **high-risk (1)** or **low-risk (0)** for diarrheal disease, based on water pollution and access to clean water.

---

## 🧠 Key Features Used

- Contaminant Level (ppm), pH Level, Turbidity  
- Nitrate & Lead Concentration  
- Access to Clean Water (%)  
- Sanitation Coverage (%)  
- Healthcare Access Index  
- Infant Mortality, Rainfall, Temperature  
- Region, Water Source Type

---

## 🧼 Project Pipeline

### 1. Data Understanding & Cleaning
- Handled missing values (e.g. unknown water treatment method)
- Verified data types, nulls, and duplicate entries
- Replaced categorical NaNs with `"Unknown"`

### 2. Outlier Detection & Removal
- Used **IQR method** to identify and remove statistical outliers

### 3. Exploratory Data Analysis (EDA)
- Correlation heatmaps
- Disease count by region
- Scatter plots of key relationships (e.g. Nitrate vs Diarrheal Cases)

### 4. Feature Engineering
- Encoded categorical features using `OneHotEncoding`
- Removed disease-related features from input (to avoid leakage)

### 5. Binary Classification
- Created `High Risk` label (1 = >150 Diarrheal Cases/100k people)
- Used **Random Forest Classifier** with class balancing

---

## 📊 Model Performance

### ✅ Final Results (Random Forest Classifier)
| Metric   | Value  |
|----------|--------|
| Accuracy | 68.6%  |
| Recall (High Risk) | **98%** ✅ |
| ROC AUC  | Good Separation |

> ⚠️ Precision for Low-Risk areas was low — this is acceptable in public health, where **recall is prioritized** to avoid missing danger zones.

---

## 📈 Visualizations

- Confusion Matrix ✅
- Precision/Recall Heatmap ✅
- ROC Curve ✅

_All included in the repo `/plots/` folder_

---

## 💡 Key Takeaways

- Pollution and sanitation directly impact disease rates  
- Data leakage can mislead — always validate assumptions  
- Binary classification is better than regression for this target  
- High recall is critical in health-related predictions

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `water_pollution_disease.csv` | Cleaned dataset |
| `final_model.ipynb` | End-to-end ML pipeline |
| `plots/` | All evaluation visualizations |
| `README.md` | Project documentation |
| `confusion_matrix.png` | Confusion matrix |
| `classification_report_heatmap.png` | Precision/recall heatmap |
| `roc_curve.png` | ROC curve |


---

## 👩‍💻 Author

**Dilrabo Khidirova**  
Machine Learning Engineer | AI for Good Advocate | Data Science Portfolio Builder  
📍 Based in Uzbekistan | 🧠 Passionate about ethical ML  
🔗 [LinkedIn](https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/)

---

## 📌 Tags

`#DataScience` `#MachineLearning` `#PublicHealth` `#RandomForest` `#BinaryClassification` `#AIforGood` `#WomenInTech` `#Kaggle` `#Streamlit`
