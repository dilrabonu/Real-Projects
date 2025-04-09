

# 🧠 Customer Segmentation with KMeans Clustering

This project analyzes and segments users of a **membership-based grocery platform** using **unsupervised learning techniques**. The goal is to identify different types of customers for better **personalization**, **loyalty marketing**, and **business decision-making**.

---

## 📂 Dataset

**Source:** Kaggle (Private CSV file)  
**File:** `membership_groceries_userprofile.csv`  
**Rows:** 858 users  
**Columns:** 15 features including:

- `gender`, `membership_tier`, `shared_account`
- `app_engagement_score`, `use_count`, `reward_points_used`
- `membership_start_date` → transformed into `membership_duration_days`

---

## 🔧 Project Pipeline

### 1. **Data Cleaning & Feature Engineering**
- Converted date columns to datetime
- Engineered `membership_duration_days` feature
- Encoded categorical variables (`gender`, `membership_tier`)
- Scaled numerical features using `StandardScaler`

### 2. **Clustering with KMeans**
- Used **Elbow Method** to determine optimal `k=4`
- Applied **KMeans** clustering to behavioral features
- Created a new column `user_cluster` to store segment labels

### 3. **Segment Interpretation**
Labeled the clusters as:
- 💎 **High Spenders**: Premium, active, and loyal
- 👥 **Regular Members**: Balanced engagement and usage
- 🧾 **Value Seekers**: Low spenders and low activity
- 💤 **Low Engagement**: Rare usage, large baskets

### 4. **Data Visualization**
- 📊 Pie Chart – Segment Distribution
- 📈 Bar Chart – Feature Averages by Segment
- 🧬 PCA 2D Plot – Cluster Visualization

---

## 📦 Tools & Technologies

- **Python 3.10**
- `pandas`, `matplotlib`, `seaborn`, `scikit-learn`
- Unsupervised ML (KMeans Clustering)
- PCA for dimensionality reduction

---

## 🧠 Key Learnings

- Importance of preprocessing and feature engineering
- Visual storytelling with PCA and pie charts
- Real-world application of clustering in retail & marketing
- How to translate ML output into business insights

---

## 📁 Outputs

- `user_cluster` column added to dataset
- `user_segment` (readable labels)
- Visuals for LinkedIn and stakeholder reporting
- Export-ready CSV and PDF reports

---

## 📌 Author

**Dilrabo Khidirova**  
Aspiring Machine Learning Engineer & Data Scientist  
📍 Open to opportunities | 💬 Let's connect on https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/

---

## 📬 Get in Touch

If you're interested in collaboration, mentoring, or hiring, feel free to reach out! I'm actively growing my skills through real-world projects like this.

https://www.kaggle.com/code/dilrabonu/membership-groceries-store-user-profile
