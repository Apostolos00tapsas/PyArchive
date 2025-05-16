import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from kmeans import KMeans

"""
Script Name: kmeans_tests.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the kmeans model for machine learning application.

Parameters:
 K         (int): Number of tree layers.
 max_iters (int): Number of iterations.

Returns:
    clf: The kmeans model.

Example:
    clf = KMeans(K=clusters, max_iters=150, plot_steps=True)
    clf.fit(X_train, y_train)
"""

#X, y = make_blobs(centers=4, n_samples=500, n_features=2, shuffle=True, random_state=42)
X, y = make_blobs(centers=3, n_samples=500, n_features=2, shuffle=True, random_state=40)
print(X.shape)
    
clusters = len(np.unique(y))
print(clusters)
k = KMeans(K=clusters, max_iters=150, plot_steps=True)
y_pred = k.predict(X)

k.plot()
