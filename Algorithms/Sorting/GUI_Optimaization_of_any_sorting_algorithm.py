import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.colors as mcolors
import numpy as np
from tkinter import *
from tkinter import ttk

"""
Script Name: GUI_Optimaization_of_any_sorting_algorithm.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the visualization of any sorting algorithm.

Parameters:
   

Returns:
    

Example:
    Sorting_Algorithms_Optimization()
"""


class Sorting_Algorithms_Optimization:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x200")
        self.root.title("Short Algorithms Optimaization")
        self.n=30
        self.n = DoubleVar()
        scale = ttk.Scale(self.root, from_=1, to_=40, length=300,command=lambda s:self.n.set('%d' % float(s))).grid(column=0, row=0, columnspan=5)
        self.descriptions = {"Bubble Sort":"1","Insertion Sort":"2","Quick Sort":"3","Selecton Sort":"4","Merge Sort":"5","Heapify Sort":"6","Shell Sort":"7","Count Sort":"8"}
        self.v = StringVar(self.root)
        ttk.OptionMenu(self.root, self.v, *self.descriptions.keys()).grid(row=1, column=2,ipady=5, ipadx=5)
        ttk.Label(self.root, text="N= ").grid(column=3, row=1, columnspan=5)
        ttk.Label(self.root, textvariable=self.n).grid(column=4, row=1, columnspan=5)
        self.barbtn=ttk.Button(self.root,text="Submit",command=self.gui)
        self.barbtn.grid(row=3, column=0,ipady=5, ipadx=5)
        self.root.mainloop()

    def gui(self):
        GUI(int(self.descriptions[self.v.get()]),int(self.n.get()))
       
class GUI:
    def __init__(self,descriptions,n):
        self.k = descriptions
        if n==0:
            self.n=1
        else:
            self.n = n 
        self.array = [i + 1 for i in range(self.n)]
        random.shuffle(self.array)
        if(self.k==1):
            self.title = "Bubble Sort"
            self.algo = self.sort_buble(self.array)
        elif(self.k==2):
            self.title = "Insertion Sort"
            self.algo = self.insertion_sort(self.array)
        elif(self.k==3):
            self.title = "Quick Sort"
            self.algo = self.quick_Sort(self.array,0,self.n-1)
        elif(self.k==4):
            self.title="Selection Sort"
            self.algo = self.selection_sort(self.array)
        elif (self.k == 5):
            self.title = "Merge Sort"
            self.algo=self.merge_sort(self.array,0,self.n-1)
        elif (self.k == 6):
            self.title = "Heap Sort"
            self.algo = self.heap_sort(self.array)
        elif (self.k == 7):
            self.title = "Shell Sort"
            self.algo = self.shell_sort(self.array)
        elif (self.k == 8):
            self.title = "Count Sort"
            self.algo = self.count_sort(self.array)
        # Initialize fig
        fig, ax = plt.subplots()
        ax.set_title(self.title)

        clist = [(0, "crimson"), (0.125, "pink"), (0.25, "lightblue"), (0.5, "skyblue"), (0.7, "aqua"), (0.75, "mediumaquamarine"), (1, "green")]
        rvb = mcolors.LinearSegmentedColormap.from_list("", clist)
        x = np.arange(self.n).astype(float)
        self.bar_rec = ax.bar(range(len(self.array)), self.array, align='edge',color=rvb(x /self.n))

        ax.set_xlim(0, self.n)
        ax.set_ylim(0, int(self.n * 1.1))

        self.text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

        self.epochs = [0]

        anima = anim.FuncAnimation(fig, func=self.update_plot, fargs=(self.bar_rec, self.epochs), frames=self.algo, interval=1, repeat=False)
        plt.show()

        


    def update_plot(self,array,rec,epochs):
        for rec, val in zip(rec, self.array):
            rec.set_height(val)
        self.epochs[0]+= 1
        self.text.set_text("No.of operations :{}".format(self.epochs[0]))

    @staticmethod
    def sort_buble(arr):
        if (len(arr) == 1):
            return
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if (arr[j] > arr[j + 1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                yield arr

    @staticmethod 
    def insertion_sort(arr):
        if(len(arr)==1):
            return
        for i in range(1,len(arr)):
            j = i
            while(j>0 and arr[j-1]>arr[j]):
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1
                yield arr

    @staticmethod
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

        for bar in GUI.quick_Sort(arr,p,pivindx-1):
            yield bar
        for i in GUI.quick_Sort(arr,pivindx+1,q):
            yield i

    @staticmethod
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
                
    @staticmethod
    def merge_sort(arr,lb,ub):
        if(ub<=lb):
            return
        elif(lb<ub):
            mid =(lb+ub)//2
            for i in GUI.merge_sort(arr,lb,mid):
                yield i
            for j in GUI.merge_sort(arr,mid+1,ub):
                yield j
            for k in GUI.merge(arr,lb,mid,ub):
                yield k
            yield arr

    @staticmethod   
    def merge(arr,lb,mid,ub):
        new = []
        i = lb
        j = mid+1
        while(i<=mid and j<=ub):
            if(arr[i]<arr[j]):
                new.append(arr[i])
                i+=1
            else:
                new.append(arr[j])
                j+=1
        if(i>mid):
            while(j<=ub):
                new.append(arr[j])
                j+=1
        else:
            while(i<=mid):
                new.append(arr[i])
                i+=1
        for i,val in enumerate(new):
            arr[lb+i] = val
            yield arr

    @staticmethod
    def heapify(arr,n,i):
        largest = i
        l = i*2+1
        r = i*2+2
        while(l<n and arr[l]>arr[largest]):
            largest = l
        while(r<n and arr[r]>arr[largest]):
            largest = r
        if(largest!=i):
            arr[i],arr[largest]=arr[largest],arr[i]
            yield arr
            for i in GUI.heapify(arr,n,largest):
                yield i

    @staticmethod
    def heap_sort(arr):
        n = len(arr)
        for i in range(n,-1,-1):
            for i in GUI.heapify(arr,n,i):
                yield i
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            yield  arr
            for i in GUI.heapify(arr,i,0):
                yield i
                
    @staticmethod
    def shell_sort(arr):
        sublistcount = len(arr) // 2
        while sublistcount > 0:
          for start_position in range(sublistcount):
              for i in GUI.gap_InsertionSort(arr, start_position, sublistcount):
                  yield i
          sublistcount = sublistcount // 2
          
    @staticmethod
    def gap_InsertionSort(nlist,start,gap):
        for i in range(start+gap,len(nlist),gap):

            current_value = nlist[i]
            position = i

            while position>=gap and nlist[position-gap]>current_value:
                nlist[position]=nlist[position-gap]
                position = position-gap
                yield nlist

            nlist[position]=current_value
            yield nlist

    @staticmethod
    def count_sort(arr):
        max_val = max(arr)
        m = max_val + 1
        count = [0] * m

        for a in arr:
            count[a] += 1
            yield arr
        i = 0
        for a in range(m):
            for c in range(count[a]):
                arr[i] = a
                i += 1
                yield arr
            yield  arr


Sorting_Algorithms_Optimization()
