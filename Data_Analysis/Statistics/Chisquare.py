from scipy.stats import chi2_contingency
from tkinter import *
from tkinter import ttk
import numpy as np

"""
Script Name: Chisquare.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    A class that implements chisquare statistic method via GUI.

Parameters:
     
    
Returns:
    

Example:
    Chisquare()
"""

class Chisquare:
    def __init__(self):
        self.root= Tk()
        self.root.title('Chisquare')
        self.q1 = Entry(self.root)
        self.q1.grid(row=0,column=0)
        self.q2 = Entry(self.root)
        self.q2.grid(row=1,column=0)
        self.q3 = Entry(self.root)
        self.q3.grid(row=0,column=1)
        self.q4 = Entry(self.root)
        self.q4.grid(row=1,column=1)
        self.t1 = Label(self.root,text='None')
        self.t1.grid(row=0,column=2)
        self.t2 = Label(self.root,text='None')
        self.t2.grid(row=1,column=2)
        self.t3 = Label(self.root,text='None')
        self.t3.grid(row=2,column=0)
        self.t4 = Label(self.root,text='None')
        self.t4.grid(row=2,column=1)
        self.t5 = Label(self.root,text='None')
        self.t5.grid(row=2,column=2)
        self.t6 = Label(self.root,text='Chisquare val = None')
        self.t6.grid(row=3,column=0)
        self.t7 = Label(self.root,text='p Value = None')
        self.t7.grid(row=3,column=1)

        

        
        ttk.Button(self.root,text='Submit',command=self.chi).grid(row=4,column=0)
        ttk.Button(self.root,text='Close',command=self.root.destroy).grid(row=4,column=1)
        self.root.mainloop()


    def chi(self):
        a = [int(self.q1.get()),int(self.q3.get())]
        b = [int(self.q2.get()),int(self.q4.get())]
        data = np.array([a, b]) 
        self.t1.configure(text= str(int(self.q1.get()) + int(self.q3.get())))
        self.t2.configure(text= str(int(self.q2.get()) + int(self.q4.get())))
        self.t3.configure(text= str(int(self.q1.get()) + int(self.q2.get())))
        self.t4.configure(text= str(int(self.q3.get()) + int(self.q4.get())))
        self.t5.configure(text= str(int(self.q1.get()) + int(self.q2.get()) + int(self.q3.get()) + int(self.q4.get())))
        chisq, p_val, dof, ex = chi2_contingency(data)
        self.t6.configure(text='Chisquare val = ' + str(chisq))
        self.t7.configure(text='p Value = ' + str(p_val))
        
    

Chisquare()
