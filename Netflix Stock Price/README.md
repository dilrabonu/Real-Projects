# 📈 Netflix Stock Price Analysis & Prediction (2002–2023)

This project performs professional-level data analysis and machine learning on Netflix Inc. (NFLX) stock price data from 2002 to 2023. It includes data cleaning, exploratory data analysis (EDA), feature engineering, and predictive modeling using multiple algorithms — all structured for real-world Data Science applications.

---

## 📦 Dataset

- **Source**: [Kaggle: Netflix Inc. (NFLX) Stock Price 2002–2023](https://www.kaggle.com/datasets)
- **Columns**: Date, Open, High, Low, Close, Adj Close, Volume
- **Period**: 2002 to early 2023
- **Size**: ~5700 daily entries

---

## 🔍 Project Goals

- Explore and visualize historical Netflix stock trends
- Engineer features for time-series prediction
- Train and compare multiple ML models
- Build a predictive model for future stock price estimation
- Showcase Data Science and ML workflow for portfolio

---

## 📊 Exploratory Data Analysis (EDA)

- Missing value analysis and cleaning
- Data type correction and datetime parsing
- Visualizations:
  - Closing price over time
  - 30-day moving averages
  - Volume trends
  - Correlation heatmaps
  - Monthly average trends
  - Volatility over time

---

## 🧠 Feature Engineering

- `HL_PCT`: High-Low percentage
- `PCT_change`: Percentage change from Open to Close
- `Rolling_Mean_7`, `Rolling_Std_7`: 7-day rolling statistics
- `Volatility_14`: 14-day rolling standard deviation of returns
- Lag features: Previous day’s close and volume

---

## 🧪 Machine Learning Models

| Model               | R² Score | RMSE   |
|--------------------|----------|--------|
| Linear Regression   | -0.1869  | 1.42   |
| Random Forest       | 0.6806   | 0.74   |
| LSTM Neural Network | N/A      | 53.89* |

> ✅ **Best Performer**: Random Forest  
> ⚠️ *LSTM needs further tuning (epochs, architecture, sequence input design)*

---

## 🧬 LSTM Model (Deep Learning)

- Features scaled using `MinMaxScaler`
- Reshaped to 3D tensors for sequence learning
- Model architecture:
  - LSTM(50 units)
  - Dense(1 output)
- Trained for 10 epochs (test RMSE ~53.89)

---

## 📌 Tools & Technologies

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- TensorFlow / Keras

---

## 📈 Future Improvements

- Improve LSTM performance with:
  - More training epochs
  - Better sequence windowing
  - Dropout layers & tuning
- Try other models: XGBoost, LightGBM
- Integrate technical indicators (MACD, RSI, Bollinger Bands)
- Create a Streamlit or Flask web app for interactive forecasting

---





