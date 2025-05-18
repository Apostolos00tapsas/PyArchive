import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df =  pd.read_excel('kdata.xlsx')

plt.plot(df['x'],df['y'],'ro')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


kmeans = KMeans(n_clusters = 3, init= 'k-means++')
kmeans.fit(df.values)
yk = kmeans.predict(df.values)
        
# Get centroids
plt.figure(figsize=(8,6))
cent = kmeans.cluster_centers_
        
plt.scatter(df['x'],df['y'], c = yk , s=50, cmap='rainbow', label = 'Values')
plt.scatter(cent[:,0], cent[:,1], c='black', s=100, alpha=0.5, label = 'Centroids')
plt.legend(loc="best")
plt.show()
