# 🚀 K-Means Clustering Optimization  

## 📌 Project Overview  
This project explores **K-Means clustering** to segment data effectively. The goal is to find the **optimal number of clusters (K)** using different evaluation metrics and visualization techniques.  

## 📊 Key Features  
- **Preprocessing & Feature Scaling** to improve clustering accuracy  
- **Elbow Method & Silhouette Score** to determine the best K  
- **Dimensionality Reduction (PCA)** for better visualization  
- **Cluster Performance Metrics**: Silhouette Score & Davies-Bouldin Score  
- **3D and 2D Visualization** of clustered data  

## 🔬 Techniques & Methodology  
1. **Data Preprocessing:** Standardization & feature scaling  
2. **Finding Optimal K:**  
   - Elbow Method (WCSS)  
   - Silhouette Score Analysis  
3. **Clustering Algorithms Used:**  
   - **K-Means** (main approach)  
   - **Hierarchical Clustering** (for comparison)  
   - **DBSCAN** (alternative method)  
4. **Performance Evaluation:**  
   - Silhouette Score  
   - Davies-Bouldin Score  
5. **Visualization:**  
   - PCA-based 2D & 3D plots  
   - Cluster distribution analysis  

## 📈 Results & Insights  
- **Best K found:** **10**  
- **Silhouette Score for K=10:** **0.4203**  
- **Davies-Bouldin Score for K=10:** **0.8337**  
- PCA visualization helped in **understanding cluster separability**  
- Alternative methods like **DBSCAN and Hierarchical Clustering** were explored  


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


---

## 📌 Conclusion
- K-Means clustering was the most effective at customer segmentation.
- PCA improved visualization and reduced dimensionality.
- DBSCAN struggled due to lack of clear density-based clusters.
- This segmentation can help businesses tailor marketing strategies for different customer groups.

https://www.kaggle.com/code/dilrabonu/mall-customer-segmentation-1
![image](https://github.com/user-attachments/assets/f1127c5a-241e-49fb-8ae0-ad50c8cb1278)





