import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as anim

"""
Script Name: Buble_Short_Algorithm_Optimaization
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the bubble sort algorithm to sort a list of integers in ascending order and creates a Optimization.
    Time Complexity: O(n²) in worst case.

Parameters:
    arr (list): A list of integers to be sorted.

Returns:
    list: The sorted list.

Example:
    algo=buble_sort(data)
"""

def buble_sort(arr):
    if (len(arr) == 1):
        return
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if (arr[j] > arr[j + 1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            yield arr



# Initializing Data
n=20
data = np.random.rand(n)*10

# Select Algorithm
algo=buble_sort(data)

# Initializinf Figure
fig, ax = plt.subplots()
title = "Bubble Sort"
ax.set_title(title)
text = ax.text(0.02, -4.35, "", transform=ax.transAxes)

# Create Graph
anim_pix = ax.imshow([data],cmap='plasma')
fig.colorbar(anim_pix, orientation='vertical')
epochs = [0]
def update_figure(array,pix,epochs):
    plt.imshow([data],cmap='plasma')
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))

# Animating the Graph
anima = anim.FuncAnimation(fig, func=update_figure, fargs=(anim_pix, epochs), frames=algo, interval=1, repeat=False)
plt.show()

