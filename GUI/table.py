from tkinter import *
from string import ascii_lowercase

class data_input:
    def __init__(self):
        self.root = Tk()      
        self.entries = {}
        self.tableheight = 1
        self.tablewidth = 5
        self.counter = 0
        self.frame=Canvas(self.root)
        self.frame.grid(row=0,column=0)
        for self.row in xrange(self.tableheight):
            for self.column in xrange(self.tablewidth):
                self.entries[self.counter] = Entry(self.frame, width=15)
                self.entries[self.counter].grid(row=self.row, column=self.column)
        self.counter += 1
        self.row+=1
        self.column+=1
        self.btn=Button(self.root,text="add new row",command=self.new_row)
        self.btn.grid(row=self.row,column=self.column)
        scrollbar = Scrollbar(self.frame)
        scrollbar.grid(row=self.row,column=self.column)
        scrollbar.config(command = self.frame.yview)
        self.root.bind("<k>", self.new_row)
        self.root.bind("<s>", self.show)
        self.root.mainloop()

    def new_row(self,event=None):
       for self.row in xrange(self.tableheight):
            for self.column in xrange(self.tablewidth):
                self.entries[self.counter] = Entry(self.frame, width=15)
                self.entries[self.counter].grid(row=self.row+self.counter , column=self.column)
       self.counter +=1

    def show(self,event=None):
        print (self.Matrix)
        
data_input()
