import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as anim

"""
Script Name: Selection_Short_Algorithm_Optimaization.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the selection sort algorithm, which repeatedly selects the smallest (or largest) 
    element from the unsorted portion of the list and swaps it with the first unsorted element.
    
    Time Complexity: O(n²) (inefficient for large datasets)
    Space Complexity: O(1) (in-place sorting)

Parameters:
    arr (list): The list to be sorted.

Returns:
    list: The sorted list.

Example:
    algo=selection_sort(data)
"""


def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min=j
            yield arr
        if(min!=i):
            arr[i],arr[min]=arr[min],arr[i]
            yield arr

# Initializing Data
n=20
data = np.random.rand(n)*10
# Select Algorithm
algo=selection_sort(data)

# Initializinf Figure
fig, ax = plt.subplots()
title = "Selection Sort"
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

