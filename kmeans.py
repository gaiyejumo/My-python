import numpy as np
from sklearn.cluster import KMeans

A = np.array([[-1,-1],[1,-1],[-1,1],[1,1]])

kmeans = KMeans(n_clusters=2)

kmeans = kmeans.fit(A)

labels = kmeans.predict(A)
print('labels: ', labels)

centriods = kmeans.cluster_centers_
print('centriods: ', centriods)
