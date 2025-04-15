
🧠 Thyroid Cancer Recurrence Prediction using Machine Learning
📊 Project Overview
This project focuses on building a supervised machine learning model to predict thyroid cancer recurrence using clinical and pathological data. Accurate prediction of recurrence helps in early diagnosis and personalized treatment planning, supporting healthcare professionals in decision-making.

🎯 Business Objective
The main goal is to identify patients at higher risk of recurrence based on features such as age, pathology, treatment response, and tumor stage. This aids doctors in:

Prioritizing follow-up procedures

Reducing treatment delays

Improving patient outcomes

🧾 Dataset Details
Source: Kaggle (Filtered Thyroid Cancer Dataset)

Records: 383 patients

Features:

Demographics: Age, Gender

Clinical: Pathology, Risk, Stage, Response, Focality

Outcome: Recurred (Target)

🧪 Workflow
1. Data Preprocessing
Removed duplicates

Normalized column names

Created new feature: age_group (using list comprehension)

Categorical encoding with pd.get_dummies

Label encoded the target (Recurred: Yes/No → 1/0)

2. Exploratory Data Analysis (EDA)
Age distribution by recurrence (Boxplot)

Risk level vs recurrence (Countplot)

Target class distribution

Feature importance visualizations

3. Modeling
Model: RandomForestClassifier

Evaluation:

Accuracy: 94%

Precision: 96%

Recall: 88%

F1-Score: 92%

Used ConfusionMatrixDisplay and classification_report from scikit-learn

4. Feature Importance
Top predictors:

response_Structural Incomplete

response_Excellent

adenopathy_No

age

risk_Low

💡 Key Takeaways
Applied comprehensions for efficient data transformations

Learned how to build a complete classification pipeline

Identified clinical indicators most linked to recurrence

Practiced model evaluation with healthcare metrics in mind

Presented model outputs with clean, insightful visualizations


🛠️ Tech Stack
Python 🐍

Pandas, NumPy

Seaborn, Matplotlib

Scikit-learn

Jupyter Notebooks

Kaggle

📎 How to Run
Clone the repo
git clone https://github.com/your-username/thyroid-cancer-recurrence.git
cd thyroid-cancer-recurrence

Author
Dilrabo Khidirova

https://www.kaggle.com/code/dilrabonu/thyroid-cancer-recurrence
