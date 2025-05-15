import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as anim

"""
Script Name: Quick_Short_Algorithm_Optimization.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the quicksort algorithm, a divide-and-conquer sorting method that recursively 
    partitions a list around a 'pivot' element. It is efficient for large datasets.

    Time Complexity:
        - Best/Average Case: O(n log n)
        - Worst Case: O(n²) (if the pivot is poorly chosen)
    Space Complexity: O(log n) (due to recursion stack)

Parameters:
    arr (list): The list to be sorted.
    p    (int): Starting index of the sublist to sort (default: 0).
    q    (int): Ending index of the sublist to sort (default: len(arr)-1).

Returns:
    list: The sorted list.

Example:
    algo=quick_Sort(data,0,n-1)
"""

def quick_Sort(arr,p,q):
    if(p>=q):
        return
    piv = arr[q]
    pivindx = p
    for i in range(p,q):
        if(arr[i]<piv):
            arr[i],arr[pivindx]=arr[pivindx],arr[i]
            pivindx+=1
        yield arr
    arr[q],arr[pivindx]=arr[pivindx],arr[q]
    yield arr

    for bar in quick_Sort(arr,p,pivindx-1):
        yield bar
    for bar in quick_Sort(arr,pivindx+1,q):
        yield bar



# Initializing Data
n=10
data = np.random.rand(n)*10

# Select Algorithm
algo=quick_Sort(data,0,n-1)

# Initializinf Figure
fig, ax = plt.subplots()
title = "Quick Sort"
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
