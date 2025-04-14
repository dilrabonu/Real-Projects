# 🎬 Netflix Movies & TV Shows Classification – Machine Learning Project

Welcome to my end-to-end machine learning project where I analyze and predict whether a Netflix title is a **Movie** or a **TV Show** using its metadata. This project was part of my 30-Day Python Mastery Marathon and showcases a full professional ML pipeline with EDA, feature engineering, and model comparison.

---

## 📌 Project Objective

**Business Goal:**  
Classify content type (`Movie` or `TV Show`) using metadata such as:
- Release year
- Country of production
- Rating
- Duration

**Real-World Use Case:**  
Automating metadata classification helps platforms like Netflix improve recommendation systems, content tagging, and strategic content decisions.

---

## 🗂️ Dataset

- 📁 Source: [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- 📊 Rows: ~8,800
- 📌 Columns: `title`, `type`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`

---

## 🔧 Tools & Libraries

- `Python`
- `Pandas`, `NumPy`
- `Matplotlib`, `Seaborn`
- `Scikit-learn`
- `Counter`, `Datetime`

---

## 📊 Exploratory Data Analysis (EDA)

Key Visualizations:
- 📈 Type Distribution (Movie vs TV Show)
- 🌍 Top 10 Countries Producing Content
- 🎭 Most Common Genres
- 📆 Content Trends by Year & Month
- ⏱️ Movie Duration Distribution
- 🔥 Feature Correlation Heatmap

All insights helped guide effective feature selection for modeling.

---

## 🧠 Feature Engineering

✅ Converted date fields to `year_added`, `month_added`  
✅ Cleaned and extracted duration in minutes  
✅ Encoded categorical features (`country`, `rating`, `type`)  
✅ Handled missing values using contextual and mode-based imputation

### 🎯 Target Variable
- `type` → Binary: Movie = 0, TV Show = 1

### 🧩 Selected Features
- `release_year`  
- `country`  
- `rating`  
- `duration_mins`

---

## 🤖 Machine Learning Models

### Models Compared:
- ✅ Random Forest Classifier
- Logistic Regression
- K-Nearest Neighbors (KNN)

### 📈 Accuracy Results:

| Model                | Accuracy     |
|----------------------|--------------|
| ✅ Random Forest       | **99.77%**    |
| Logistic Regression   | 99.70%       |
| KNN                   | 99.65%       |

✅ **Random Forest** was the best performer, showing strong predictive power on both classes.

---

## 📉 Evaluation Metrics

- **Precision**: 0.99+
- **Recall**: 1.00
- **F1-Score**: 1.00
- **Macro Average**: 1.00

The model generalizes well and is production-ready.

---

## 🧠 Key Takeaways

- Clean feature engineering leads to extremely strong classification performance.
- Even simple models perform well on well-prepared data.
- Visualization drives better decisions before modeling.
- Understanding the data is **as important** as training the model.

---

## 💡 Future Improvements

- Add content-based filtering or clustering
- Create a recommender system using genres, country, or ratings
- Try NLP on `description` to improve predictions

---





https://www.kaggle.com/code/dilrabonu/netflix-movies-and-tv-shows
