from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from pca import PCA


#data = datasets.load_digits()
data = datasets.load_iris()
X = data.data
y = data.target

"""
Script Name: pca_tests.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the Principal Componenets Analisys for machine learning application or dimenction dedaction.

Parameters:
    n_com (int): Number of components    
    
Returns:
    PCA: The bayesian model.

Example:
    pca = PCA(com)
    pca.fit(X_train, y_train)
"""

# Project the data onto the 2 primary principal components
n_com = 2
pca = PCA(n_com)
pca.fit(X)
X_projected = pca.transform(X)

print('Shape of X:', X.shape)
print('Shape of transformed X:', X_projected.shape)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

plt.scatter(x1, x2,
        c=y, edgecolor='none', alpha=0.8,
        cmap=plt.cm.get_cmap('viridis', 3))

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()
plt.show()
