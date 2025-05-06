
# 🧠 Breast Cancer Classification & Visualization with Unsupervised and Supervised Machine Learning

This project explores the **Breast Cancer Wisconsin (Original)** dataset using both **unsupervised learning** (PCA, t-SNE, KMeans) and **supervised learning** (Random Forest Classification) to visualize, understand, and predict the nature of tumors as **benign** or **malignant**.

---

## 📌 Project Goals

- 🧪 Perform **exploratory data analysis** on breast cancer features.
- 🔍 Use **PCA and t-SNE** for dimensionality reduction and visualization.
- 🎯 Apply **KMeans clustering** to evaluate pattern discovery without labels.
- 🧠 Train a **Random Forest classifier** to predict cancer diagnosis.
- 📊 Visualize performance using confusion matrices and feature importance.
- 💾 Save all processed datasets for reproducibility.

---

## 📁 Dataset

- Source: UCI ML Repository (via Kaggle)
- Samples: 675
- Features: 10 (numeric diagnostic features)
- Target: `Class` (2 = Benign, 4 = Malignant)

---

## 📊 Unsupervised Learning Techniques

| Technique | Purpose | Output |
|-----------|---------|--------|
| **PCA** | Linear dimensionality reduction | 2D visualization of feature variance |
| **t-SNE** | Non-linear dimensionality reduction | Visualize clusters and local structure |
| **KMeans** | Unsupervised clustering | Cluster patients into groups (k=2) |

---

## 🧠 Supervised Learning Pipeline

- **Train/Test Split**: 80/20
- **Model**: `RandomForestClassifier`
- **Metrics**: Accuracy, Precision, Recall, F1-score
- **Performance**:
  - ✅ Accuracy: **97%**
  - ✅ Precision: **98–100%**
  - ✅ Recall: **93–100%**

---

## 📈 Visualizations

- ✅ PCA Projection (with and without labels)
- ✅ t-SNE Embeddings
- ✅ KMeans Clusters
- ✅ Confusion Matrix
- ✅ Feature Importance Bar Plot

---

---

## 🧠 Key Takeaways

- Even basic diagnostic features can effectively separate benign and malignant tumors.
- Unsupervised learning can reveal structure without requiring labels.
- Random Forests provide strong baseline accuracy on medical data.
- Dimensionality reduction aids in interpretability for non-technical stakeholders.

---

## 💬 Future Improvements

- Build a Streamlit dashboard for interactive visualization.
- Compare with Logistic Regression, XGBoost, and Neural Networks.
- Apply SHAP or LIME for model interpretability.

---

## 🔗 Connect With Me

If you're working in ML for healthcare, interested in medical AI applications, or building explainable models — let's connect!

https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/
---


https://www.kaggle.com/code/dilrabonu/breast-cancer-winconsin
