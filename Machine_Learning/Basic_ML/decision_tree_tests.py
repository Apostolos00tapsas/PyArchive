import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from decision_tree import DecisionTree

"""
Script Name: decision_tree_tests.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the decition tree model for machine learning application.

Parameters:
    max_depth (int): Number of tree layers.

Returns:
    clf: The desition tree model.

Example:
    clf = DecisionTree(max_depth=10)
    clf.fit(X_train, y_train)
"""

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

data = datasets.load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

clf = DecisionTree(max_depth=10)
clf.fit(X_train, y_train)
    
y_pred = clf.predict(X_test)
acc = accuracy(y_test, y_pred)

print ("Accuracy:", acc)