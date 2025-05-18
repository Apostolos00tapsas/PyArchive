from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
import numpy as np
import numpy as geek 

"""
Script Show_Table.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Creates and shows an nxn matrix.

Parameters:
    n (int): number of nxn matrix

Returns:
    

Example:
    
"""

#try:
#   import tktable
#except ImportError as io:
 #   root = Tk()
  #  tkMessageBox.showerror("ImportError",io)
   # MsgBox = tkMessageBox.askquestion ('Install Missing Moduls','Do you want to install tkintertable',icon = 'warning')
    #if MsgBox == 'yes':
     #   os.system("pip install tktable")
      #  tkMessageBox.showinfo("Install","Your Module Installed Successfully. Now you can inspect datasets.")
       # root.destroy()
    #else:
     #   tkMessageBox.showinfo("Install","You must Install Missing Modules.") 
      #  root.destroy()

n = 5
data = np.random.rand(n,n)
root = Tk()
root.geometry('800x500')
height = n
width = n
w = Canvas(root, width=50, height=50)
w.pack()
hbar=Scrollbar(root,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=w.xview)
vbar=Scrollbar(root,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=w.yview)
w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
w.pack(side=LEFT,expand=True,fill=BOTH)
z = Canvas(root, width=200, height=100)
z.pack()
myscroll = ttk.Scrollbar(z, orient='horizontal', command=z.xview)
z.configure(xscrollcommand=myscroll.set)
for i in range(height): #Rows
    for j in range(width): #Columns
        if i % 2 ==0:
            b = Label(w, text=str('%.4f' % data[i][j]),bg='grey')
            b.grid(row=i, column=j)
        else:
            b = Label(w, text=str('%.4f' % data[i][j]),bg='white')
            b.grid(row=i, column=j)

update_btn = ttk.Button(z, text='Update', state=NORMAL, command=root.destroy).grid(row=0, column=1)
exit_btn = ttk.Button(z, text='Close', state=NORMAL, command=root.destroy).grid(row=0, column=2)



mainloop()
