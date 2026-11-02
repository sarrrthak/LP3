import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. Load Dataset
df = pd.read_csv("/content/sales_data_sample.csv", encoding="latin1")

print("Original Dataset:")
print(df.head())

# 2. Select Numerical Features
X = df[["QUANTITYORDERED", "PRICEEACH", "SALES"]]

# Handle missing values
X = X.dropna()

# 3. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# 5. K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)

print("\nK-Means Cluster Labels:")
print(kmeans_labels)

# 6. Hierarchical Clustering
hierarchical = AgglomerativeClustering(n_clusters=3)
hierarchical_labels = hierarchical.fit_predict(X_scaled)

print("\nHierarchical Cluster Labels:")
print(hierarchical_labels)

# 7. Plot Hierarchical Dendrogram
plt.figure(figsize=(10, 5))
Z = linkage(X_scaled[:100], method="ward")
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()

# 8. Display Clustered Data
df = df.loc[X.index].copy()
df["KMeans_Cluster"] = kmeans_labels
df["Hierarchical_Cluster"] = hierarchical_labels

print("\nFinal Clustered Dataset:")
print(df[["QUANTITYORDERED", "PRICEEACH", "SALES",
          "KMeans_Cluster", "Hierarchical_Cluster"]].head())
