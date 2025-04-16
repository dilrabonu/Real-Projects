# 🎧 Predicting YouTube Virality from Spotify Audio Features

This project explores whether we can predict the **virality of a song on YouTube** using its **audio features from Spotify**. Using a dataset of 20,000+ tracks, we perform full **data preprocessing, EDA, feature engineering, and machine learning modeling** to classify whether a track is likely to go viral (≥ 1 million views).

---




---

## 🎯 Business Objective

> **Goal:** Predict whether a song will become *viral on YouTube* using its audio characteristics from Spotify.  
This can support **music marketers, content strategists, and streaming platforms** in optimizing campaigns for high-performing tracks.

---

## 📊 Dataset Overview

- **Source:** Kaggle `Spotify and YouTube` dataset  
- **Rows:** 20,000+ songs  
- **Features:**  
  - Spotify: `Danceability`, `Energy`, `Valence`, `Tempo`, `Loudness`, etc.  
  - YouTube: `Views`, `Likes`, `Comments`, `Stream`, `Title`, `Channel`

---

## 🧪 ML Pipeline

### ✅ 1. Preprocessing
- Handled missing values with strategy-based imputation
- Removed unnecessary features (`Url`, `Description`, `Uri`, etc.)
- Handled class imbalance

### ✅ 2. Feature Engineering
- Created target column: `is_viral = 1 if Views ≥ 1M else 0`

### ✅ 3. Modeling
- Models used:
  - `RandomForestClassifier` (accuracy: 83%)
  - `XGBoostClassifier` (accuracy: 74%)
- Evaluation:
  - `Precision`, `Recall`, `F1-Score`, `Confusion Matrix`
  - `Feature Importance` plots

---

## 🔍 Key Findings

- `Danceability`, `Energy`, and `Valence` showed higher correlation with viral tracks
- Random Forest had better performance in detecting viral content
- XGBoost performed better in handling class 0 (non-viral) detection

---

## 🧠 Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **Scikit-learn**
- **XGBoost**
- **Joblib**

---

## 💾 How to Use

```bash
# Clone the repo
git clone https://github.com/yourusername/spotify-viral-prediction.git

# Run the notebooks
cd notebooks/
jupyter notebook

# Load model in Python
import joblib
model = joblib.load('spotify_viral_predictor.pkl')
scaler = joblib.load('spotify_scaler.pkl')


https://www.kaggle.com/code/dilrabonu/spotify-and-youtube
