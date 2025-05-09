
# 🧠 Sentiment Analysis with Naive Bayes – Sentiment140 Dataset

This project is part of my **30-Day Python & Machine Learning Mastery** journey – **Day 27** focuses on building a real-world **Sentiment Analysis pipeline** using the classic **Naive Bayes classifier** on the **Sentiment140 dataset**, which contains 1.6 million labeled tweets.

## 📌 Project Objective

Build an end-to-end Natural Language Processing (NLP) pipeline to:
- Clean and preprocess tweet data
- Convert text into TF-IDF features
- Train a Naive Bayes classifier
- Evaluate performance using classification metrics
- Visualize insights using Word Clouds and Confusion Matrix

---

## 📁 Dataset

- **Source**: [Sentiment140 on Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)
- **Size**: 1.6M tweets
- **Columns**: 
  - `target` (0 = Negative, 4 = Positive)
  - `text` (Tweet content)

---

## 🧪 Techniques & Tools Used

| Task                        | Technique / Library       |
|-----------------------------|---------------------------|
| Text Preprocessing          | Regex, NLTK               |
| Vectorization               | `TfidfVectorizer`         |
| Model Training              | `MultinomialNB` (Naive Bayes) |
| Evaluation                  | Accuracy, Precision, Recall, F1, Confusion Matrix |
| Visualization               | Matplotlib, Seaborn, WordCloud |
| Model Saving                | `joblib`                  |

---

## ✅ Results

- **Accuracy**: `76.3%`
- **Precision & Recall**: Balanced at `~76%`
- **Confusion Matrix**: Model handles both positive and negative classes well.
- **Model + Vectorizer**: Exported as `.pkl` files for deployment or further tuning.

---

## 📊 Key Visuals

- ✅ **Confusion Matrix**: Performance summary of true vs. predicted labels.
- ☁️ **Word Clouds**: High-frequency words per sentiment class.
- 📈 **Classification Report**: Precision, Recall, F1-Score for each class.

---

👩‍💻 Author
Dilrabo Khidirova
Master's Student | Data Scientist | AI Researcher
![image](https://github.com/user-attachments/assets/8517b9c8-e651-4a64-841e-a9a208f59a69)



https://www.kaggle.com/code/dilrabonu/sentiment-140-dataset
