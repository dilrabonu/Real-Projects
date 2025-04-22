# 🐦 Twitter Sentiment Classification (Traditional ML Approach)

This project focuses on building a **multi-class sentiment classification model** using traditional Machine Learning techniques on a large-scale Twitter dataset. The goal is to classify tweets into four sentiment categories: `Irrelevant`, `Negative`, `Neutral`, and `Positive`.

---

## 📁 Dataset

- Source: Kaggle Dataset [Twitter Entity Sentiment Analysis]
- Total Rows: **74,681**
- Format: CSV
- Columns:
  - `id`: Tweet ID
  - `entity`: Brand or topic mentioned
  - `sentiment`: Target label (`Positive`, `Negative`, `Neutral`, `Irrelevant`)
  - `text`: Raw tweet content

---

## 📌 Problem Statement

> Given a tweet, predict its sentiment class among four categories.

We aim to:
- Build a classification model using traditional ML
- Clean and preprocess raw tweet text
- Evaluate performance using accuracy, F1-score, and confusion matrix

---

## 🧠 Project Pipeline

### 1. **Data Preprocessing**
- Removed nulls and 2.7K+ duplicate entries
- Cleaned tweets (removed URLs, mentions, hashtags, special chars)
- Lowercased, removed stopwords, applied lemmatization

### 2. **Feature Engineering**
- Converted tweets to TF-IDF features (word-level)
- Used `TfidfVectorizer(max_features=5000)`

### 3. **Modeling**
- Trained and compared:
  - `LogisticRegression`
  - `RandomForestClassifier`
  - `XGBoostClassifier`
- Used `train_test_split` (80/20)

### 4. **Evaluation**
- Metrics: Accuracy, Macro F1-score
- Visualized confusion matrix using `seaborn`

---

## 📊 Results

| Model               | Accuracy | Macro F1 Score | Notes                                   |
|--------------------|----------|----------------|-----------------------------------------|
| Logistic Regression| 68%      | 66%            | Fast baseline, interpretable            |
| Random Forest       | **88%**  | **87%**        | Most balanced across all classes        |
| XGBoost             | **88%**  | **87%**        | Best for production use, very robust    |

---

## 🔍 Key Takeaways

- Preprocessing is **crucial** — quality text in = quality predictions out
- Traditional ML with TF-IDF still **performs strongly** for NLP
- Evaluation should include **F1-score + confusion matrix**, not just accuracy
- Interpretability of models (e.g., Random Forest) adds explainability for business use

---

## 🛠️ Tech Stack

- Python 3.9
- Pandas, Numpy
- scikit-learn
- XGBoost
- nltk (for text cleaning)
- seaborn / matplotlib

---

## 🚀 Future Work

- Deploy model with Streamlit for interactive demo
- Test Word2Vec or FastText embeddings
- Compare results with fine-tuned BERT or DistilBERT
- Add hyperparameter tuning (GridSearchCV or Optuna)

---

## 📎 Author

👩‍💻 **Dilrabo Khidirova**  
_Data Scientist | ML Engineer | Women in Tech Advocate_
---


https://www.kaggle.com/code/dilrabonu/twitter-sentiment-analysis
