import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from logistic_regression import LogisticRegression
#from regression import LogisticRegression

"""
Script Name: logistic_regression_tests.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the logistic_regression model for machine learning application.

Parameters:
    learning_rate (float): Number of learning rate.
    n_iters         (int): Number of iterations.
Returns:
    regressor: The regration model.

Example:
    regressor = LogisticRegression(learning_rate=0.01, n_iters=1000)
    regressor.fit(X_train, y_train)
"""

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

regressor = LogisticRegression(learning_rate=0.0001, n_iters=1000)
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)

print("LR classification accuracy:", accuracy(y_test, predictions))