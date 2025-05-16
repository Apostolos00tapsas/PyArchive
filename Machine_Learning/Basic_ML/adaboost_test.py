import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from adaboost import Adaboost

"""
Script Name: adaboost_test.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the adaboost model for machine learning application.

Parameters:
    n_clf (int): Number of classifiers.

Returns:
    clf: The adaboost model.

Example:
    clf = Adaboost(n_clf=5)
    clf.fit(X_train, y_train)
"""


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

data = datasets.load_breast_cancer()
X = data.data
y = data.target

y[y == 0] = -1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# Adaboost classification with 5 weak classifiers
clf = Adaboost(n_clf=5)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

acc = accuracy(y_test, y_pred)
print ("Accuracy:", acc)
