
# 🔍 Google Quest Q&A Answer Quality Prediction (NLP + Multi-Output Regression)

This project focuses on building a complete machine learning pipeline to evaluate the quality of answers in question-answer forums using Natural Language Processing (NLP) techniques.

---

## 📦 Dataset

The dataset comes from the **Google Quest Challenge** on Kaggle and includes:
- Real-world questions and answers
- Metadata (e.g., user, host, category)
- Multiple continuous labels measuring **answer quality dimensions**, such as:
  - `answer_helpful`
  - `answer_satisfaction`
  - `answer_relevance`
  - `answer_well_written`, etc.

---

## 🎯 Objective

To build a model that can **predict multiple quality scores** (multi-label regression) for each answer, enabling platforms to:
- Rank answers by quality
- Surface more useful responses
- Improve user experience on Q&A forums

---

## 🧠 ML Task

- **Type:** Multi-output regression
- **Features:** Cleaned and combined `question_body` + `answer`
- **Targets:** 9 continuous labels (ranging from 0 to 1)
- **Challenges:** Subjectivity in labels, sparse NLP data, semantic understanding

---

## 🛠️ Pipeline Overview

### ✅ 1. Data Cleaning
- Removed HTML, symbols, stopwords
- Combined `question_body` + `answer` into `qa_combined`

### ✅ 2. Feature Extraction
- 🔹 **TF-IDF Vectorizer**: N-gram (1,2), max 5000 features
- 🔹 **BERT Embeddings**: Using `all-MiniLM-L6-v2` via `sentence-transformers`

### ✅ 3. Modeling
- Ridge regression wrapped with `MultiOutputRegressor`
- Trained on both TF-IDF and BERT feature sets
- Evaluated using:
  - RMSE (Root Mean Squared Error)
  - R² Score (coefficient of determination)

---

## 📈 Results Summary

> *The project evaluated both TF-IDF and BERT pipelines. Evaluation and interpretation focused on practical learnings, model robustness, and semantic generalization. Visualizations and insights included.*

---

## 💡 Key Takeaways

- Pretrained embeddings like BERT provide deeper semantic representations but require proper tuning and data volume
- Ridge regression remains strong as a baseline for multi-target NLP tasks
- Visualization and interpretation of individual label predictions is essential for understanding regression behavior
- End-to-end NLP pipelines must be rigorously cleaned, balanced, and evaluated with care

---

## 📚 Tech Stack

- `Python` 🐍
- `Pandas`, `scikit-learn`, `matplotlib`, `seaborn`
- `sentence-transformers` for BERT embeddings
- `Kaggle` + `Jupyter Notebooks` for experimentation

---



https://www.kaggle.com/code/dilrabonu/google-quest-challenge-qa-file-metadata
