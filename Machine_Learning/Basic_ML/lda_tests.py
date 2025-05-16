from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

from lda import LDA

"""
Script Name: lda_tests.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the lda model for machine learning application.

Parameters:
    n_com (int): Number of componenets.

Returns:
    lda: The ida model.

Example:
    lda = LDA(n_com)
    lda.fit(X_train, y_train)
"""

data = datasets.load_iris()
X = data.data
y = data.target
n_com = 2

# Project the data onto the 2 primary linear discriminants
lda = LDA(n_com)
lda.fit(X, y)
X_projected = lda.transform(X)

print('Shape of X:', X.shape)
print('Shape of transformed X:', X_projected.shape)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

plt.scatter(x1, x2,
        c=y, edgecolor='none', alpha=0.8,
        cmap=plt.cm.get_cmap('viridis', 3))

plt.xlabel('Linear Discriminant 1')
plt.ylabel('Linear Discriminant 2')
plt.colorbar()
plt.show()
