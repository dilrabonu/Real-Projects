# Mall Customers Segmentation using Clustering Techniques

## 📌 Project Overview
This project applies **unsupervised learning** techniques to segment customers based on their annual income and spending score using the **Mall Customers Segmentation Dataset**. We explore and compare various clustering algorithms:

- **K-Means Clustering**
- **Hierarchical Clustering**
- **DBSCAN Clustering**
- **PCA for Dimensionality Reduction**

The goal is to find distinct customer groups that can help businesses target specific demographics for marketing strategies.

---

## 📂 Dataset Description
**Dataset Name:** Mall_Customers.csv

The dataset contains **200 observations** with the following features:
- `CustomerID` - Unique customer identifier (removed for clustering)
- `Gender` - Male/Female (encoded to numerical)
- `Age` - Age of the customer
- `Annual Income (k$)` - Income in thousands of dollars
- `Spending Score (1-100)` - Score assigned by the mall based on customer behavior



## 📊 Exploratory Data Analysis (EDA)
We performed an in-depth **EDA** to visualize relationships between variables using:
- **Gender Distribution:** Countplots
- **Age Distribution:** Histograms
- **Annual Income vs Spending Score:** Scatter Plots
- **Correlation Analysis**

**Example Visualization:**
```python
sns.scatterplot(x=df['Annual Income (k$)'], y=df['Spending Score (1-100)'], hue=df['Gender'], palette='viridis')
```

---

## 🔍 Clustering Methodology
### 1️⃣ Data Preprocessing
- Encoded categorical variables (Gender)
- Scaled features using `StandardScaler`
- Applied **PCA** to reduce dimensions for visualization

### 2️⃣ K-Means Clustering
- Used the **Elbow Method** to determine the optimal number of clusters
- Implemented K-Means clustering with **k=5**

```python
kmeans = KMeans(n_clusters=5, random_state=42)
df['KMeans_Cluster'] = kmeans.fit_predict(df_scaled)
```

### 3️⃣ Hierarchical Clustering
- Used **Dendrograms** to determine the number of clusters
- Applied **Agglomerative Clustering**

```python
hierarchical = AgglomerativeClustering(n_clusters=5)
df['Hierarchical_Cluster'] = hierarchical.fit_predict(df_scaled)
```

### 4️⃣ DBSCAN Clustering
- Applied **Density-Based Clustering** with `eps=1.5, min_samples=5`
- Suitable for finding noise/outliers

```python
dbscan = DBSCAN(eps=1.5, min_samples=5)
df['DBSCAN_Cluster'] = dbscan.fit_predict(df_scaled)
```

---

## 📈 Model Evaluation
We evaluated clustering performance using:

✔ **Silhouette Score** (Higher is better)
```python
silhouette_score(df_scaled, df['KMeans_Cluster'])
```
✔ **Davies-Bouldin Score** (Lower is better)
```python
davies_bouldin_score(df_scaled, df['KMeans_Cluster'])
```

### **Results Summary:**
| Model              | Silhouette Score | Davies-Bouldin Score |
|-------------------|----------------|------------------|
| K-Means          | **0.55**        | **0.80**        |
| Hierarchical     | 0.52            | 0.85            |
| DBSCAN           | Low (no clear clusters) | - |

🔹 **K-Means performed best**, identifying five meaningful customer segments.

---

## 📌 Conclusion
- K-Means clustering was the most effective at customer segmentation.
- PCA improved visualization and reduced dimensionality.
- DBSCAN struggled due to lack of clear density-based clusters.
- This segmentation can help businesses tailor marketing strategies for different customer groups.
![image](https://github.com/user-attachments/assets/f1127c5a-241e-49fb-8ae0-ad50c8cb1278)





