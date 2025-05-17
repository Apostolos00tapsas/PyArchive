import matplotlib.pyplot as plt

"""
Script Name: Simple+plot.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    A script that plots two diferend lines.

"""

x = [6,10,14,15,17,19,21,23,24,28,38,45]
y = [1,0.98,1,0.9,0.8,0.75,0.7,0.65,0.6,0.5,0.05,0]
z = [1,1,1,1,1,1,1,1,1,0.73,0.13,0.1]
k= [30,35,40,45,50,55,60,65]
A= [0,0,0,0.33,0.66,1,1,1]
B= [1,1,1,1,1,0.027,0.02,0.01]
plt.plot(k,A)
plt.plot(k,B)
plt.show()
