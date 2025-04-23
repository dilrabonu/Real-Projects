
# 🛍️ Retail Sales Prediction & Customer Segmentation

This project demonstrates a complete end-to-end Machine Learning workflow using a real-world **Retail Sales Dataset**. It combines both **supervised** and **unsupervised** learning techniques to predict customer spending and uncover hidden customer segments.

---

## 📌 Project Overview

**Objective**:
- Predict customer `Total Amount` spent using regression techniques
- Segment customers into meaningful clusters based on age and spending patterns

**Dataset**:
- 1000 transaction records including:
  - Customer demographics (Gender, Age)
  - Purchase behavior (Product Category, Quantity, Price)
  - Outcome variable: `Total Amount`

---

## 📈 Supervised Learning: Sales Prediction

A **Linear Regression** model was trained to predict the `Total Amount` spent by each customer based on their:
- Gender
- Age
- Quantity
- Price per Unit

### 🔍 Results:
- **R² Score**: `0.8569`
- **MAE**: `$172.95`

✅ The model shows strong predictive performance and explains ~86% of the variance in spending.

---

## 🧠 Unsupervised Learning: Customer Segmentation

Using **KMeans Clustering**, we segmented customers based on:
- Age
- Total Amount spent
- Product Category (encoded)

### 🔎 Process:
- Applied **StandardScaler** for normalization
- Used the **Elbow Method** to find optimal `k=3`
- Trained `KMeans(n_clusters=3)` and assigned cluster labels

### 🧠 Segment Insights:
- **Cluster 0**: Low spenders — discount-target group
- **Cluster 1**: Average spenders — focus on loyalty
- **Cluster 2**: High spenders — VIP treatment & upselling

---

## 📦 Tech Stack

- Python
- Pandas, NumPy
- Scikit-Learn
- Matplotlib, Seaborn
- Jupyter Notebook / Kaggle

---

## 📁 Files

| Filename                     | Description                           |
|-----------------------------|---------------------------------------|
| `retail_sales_dataset.csv`  | Original dataset                      |
| `retail_sales_segmented.csv`| Dataset with cluster labels           |
| `notebook.ipynb`            | Full ML pipeline with code & outputs  |
| `/images/`                  | Visualizations (prediction, clusters) |

---

## 🚀 How to Use

1. Clone the repo
2. Open `notebook.ipynb` in Jupyter or Kaggle
3. Install dependencies: `pip install pandas scikit-learn seaborn matplotlib`
4. Run all cells to reproduce results

---

## 👩‍💻 Author

**Dilrabo Khidirova**  
Machine Learning & Data Science Enthusiast  
📍 Building AI-powered tools for business and research  
🌐 https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/

---

https://www.kaggle.com/code/dilrabonu/retail-sales
![image](https://github.com/user-attachments/assets/f9322697-14c9-454b-b3f8-e945bc70c6c1)
