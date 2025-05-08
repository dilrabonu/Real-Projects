
## 📌 Project Overview

This project applies **Natural Language Processing (NLP)** techniques to classify **Twitter airline reviews** into **positive**, **neutral**, or **negative** sentiments. The goal was to build a **modular, real-time ready sentiment classifier** and benchmark models using a clean machine learning pipeline.

> ✅ This project is designed with **real-world deployment in mind** — the entire pipeline can be easily integrated into a **Streamlit or Flask** app.

---

## 🧠 Objectives

- Clean and preprocess raw tweet text using NLP techniques
- Extract features using **TF-IDF vectorization**
- Train and evaluate multiple ML models:
  - Logistic Regression (baseline)
  - Support Vector Machine (LinearSVC)
  - XGBoost (gradient boosting classifier)
- Visualize and compare confusion matrices
- Build a modular pipeline for future deployment (Streamlit/Flask)

---

## 📂 Dataset

- **Source**: Kaggle – [Twitter US Airline Sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
- **Rows**: 14,640
- **Key Columns Used**:  
  - `text` → raw tweet  
  - `airline_sentiment` → target label (`positive`, `neutral`, `negative`)

---

## 🧼 Data Preprocessing

- Lowercased and cleaned tweets
- Removed URLs, HTML tags, punctuation
- Removed stop words using NLTK
- Tokenized using `word_tokenize`
- Applied `TfidfVectorizer` with `max_features=3000`

---

## ⚙️ Models Trained & Evaluated

| Model               | Accuracy | Comments                                      |
|---------------------|----------|-----------------------------------------------|
| Logistic Regression | 80%      | Best on **negative** sentiment (F1: 0.88)     |
| SVM (LinearSVC)     | 79%      | Balanced overall, weaker on **neutral**       |
| XGBoost             | 77%      | Slower to train, consistent F1 across classes |

---

## 📊 Confusion Matrix Comparison

Confusion matrices were visualized **side-by-side** for each model to analyze misclassification patterns.

<img src="sentiment_model_comparison.png" alt="Confusion Matrix Comparison" width="100%"/>

> The visual helps assess where models confuse sentiment types, particularly between **neutral** and **positive** classes.

---

## ✅ Key Results & Learnings

- **TF-IDF** is highly effective for sparse, short text like tweets.
- **Logistic Regression** remains a powerful and fast baseline.
- **SVM** excels with high-dimensional data but needs tuning for class imbalance.
- **XGBoost** offers good generalization but slower performance.
- Modular design ensures this model is ready for real-time API or dashboard deployment.

---

## 🚀 Future Work

- Deploy to **Streamlit** or **Flask** for real-time tweet sentiment analysis
- Fine-tune using **SMOTE** or **class weights** to handle imbalance
- Try **BERT / Hugging Face Transformers** for deeper NLP performance
- Integrate with **Twitter API** for live sentiment tracking

---

---

## 📣 Acknowledgements

- Dataset https://www.kaggle.com/code/dilrabonu/us-airlines-twitter
- Inspiration from Kaggle & FAANG-style ML pipelines
- Libraries: `nltk`, `scikit-learn`, `xgboost`, `seaborn`, `matplotlib`, `pandas`

---

## 👩‍💻 Author

**Dilrabo Khidirova**  
🎓 Master's Student in Software Engineering & AI  
💡 Passionate about NLP, Explainable AI, and Real-World Machine Learning  


---

> If you found this project helpful, feel free to ⭐ star the repo and follow for more real-world ML projects!

https://www.kaggle.com/code/dilrabonu/us-airlines-twitter
