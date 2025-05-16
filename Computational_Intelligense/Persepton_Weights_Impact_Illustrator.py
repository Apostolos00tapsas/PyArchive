from tkinter import *
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

"""
Script Name: Persepton_Weights_Impact_Illustrator.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements and illustrates the way that persepton drows a line accoring to AND logical gate problem.

Parameters:
     
    
Returns:
    

Example:
    Persepton_Weights_Impact_Illustrator()
"""

class Persepton_Weights_Impact_Illustrator:
    def __init__(self):
          self.perline = False
          self.weights = np.zeros(2)
          # Define window
          self.root = Tk()
          self.root.title("Persepton Weights Impact Illustration")
          self.root.geometry('800x500')

          #ToDo objects on right site of canvas
          right_f = Frame(self.root,background='#ff4d4d')
          right_f.pack(side=RIGHT)

          self.l0 = Label(right_f,font=('times new roman',12),text="Line Lenght",bg='#ff4d4d')
          self.l0.pack()

          #Define Current Velocity Impact
          self.linelen = DoubleVar()
          
          scale = Scale(right_f, variable = self.linelen, from_=0.1, to=1.5,resolution = 0.1, orient=HORIZONTAL, command = self.getxy)
          scale.pack(anchor=CENTER)
          
          self.l1 = Label(right_f,font=('times new roman',12),text="W0",bg='#ff4d4d')
          self.l1.pack()

          #Define Current Velocity Impact
          self.w0 = DoubleVar()
          
          scale = Scale(right_f, variable = self.w0, from_=0.001, to=0.01,resolution = 0.0001, orient=HORIZONTAL, command = self.getxy)
          scale.pack(anchor=CENTER)

          self.l2 = Label(right_f,font=('times new roman',12),text="W1",bg='#ff4d4d')
          self.l2.pack()

          #Define Current Velocity Impact
          self.w1 = DoubleVar()
          scale = Scale(right_f, variable = self.w1, from_=0.001, to=0.01,resolution = 0.0001, orient=HORIZONTAL, command = self.getxy)
          scale.pack(anchor=CENTER)
        
          self.l3 = Label(right_f,font=('times new roman',12),text="W2",bg='#ff4d4d')
          self.l3.pack()
          
          #Define Current Velocity Impact
          self.w2 = DoubleVar()
          scale = Scale(right_f, variable = self.w2, from_=0.001, to=0.01,resolution = 0.0001, orient=HORIZONTAL, command = self.getxy)
          scale.pack(anchor=CENTER)

          # Define figure
          self.f = Figure(figsize=(10,6), dpi=100)
          self.ax = self.f.add_subplot(111)
          self.ax.clear()

          # Defibe axis names and plot tiltle
          self.ax.title.set_text("Persepton Weights Impact Illustration")
          self.ax.set_xlabel(" x ")
          self.ax.set_ylabel(" y ")

          # Define x y limits
          self.ax.set_xlim(-2, 3)
          self.ax.set_ylim(-2, 3)

          self.X=np.array([[0,0],[0,1],[1,0],[1,1]])
          self.t = [0,0,0,1]
          
          self.ax.scatter(self.X[:,0],self.X[:,1], c = self.t , s=50, cmap='rainbow')
          
          perbtn = Button(self.root,text='Run Perseptron Algorithm', command = self.perseptron)
          perbtn.pack(side=BOTTOM)
          # Define canvas
          self.canvas = FigureCanvasTkAgg(self.f, self.root)
          self.canvas.draw()
          self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

          # Detect canvas x and y 
          self.canvas.mpl_connect('button_press_event',self.draw_class)
          self.root.mainloop()

    def getxy(self, event):
        self.perline = False
        self.ax.clear()
        self.ax.title.set_text("Persepton Weights Impact Illustration")
        self.ax.set_xlabel(" x ")
        self.ax.set_ylabel(" y ")
        self.ax.set_xlim(-2, 3)
        self.ax.set_ylim(-2, 3)
        xx = np.linspace(min(self.X[:,1]-self.linelen.get()), max(self.X[:,1])+self.linelen.get())
        self.ax.scatter(self.X[:,0],self.X[:,1], c = self.t , s=50, cmap='rainbow')
        yy = -1*(self.w1.get() * xx + (self.w0.get()*(-1))) / self.w2.get()
        self.ax.plot(xx, yy, label = 'Perseptron Line')
        self.ax.legend(loc="best")
        self.canvas.draw()

    def perseptron(self):
        self.perline = True
        self.lr = 0.0001
        self.wbias = 0
        e=0
        while e< 10:            
            for i, x_i in enumerate(self.X):
                u = np.dot(x_i, self.weights) + self.wbias
                Y = self.step(u)
                # Update weights
                update = self.lr * (self.t[i] - Y)
                self.weights += update * x_i
                self.wbias += update
                
                self.ax.clear()
                self.ax.title.set_text("Persepton Weights Impact Illustration")
                self.ax.set_xlabel(" x ")
                self.ax.set_ylabel(" y ")
                self.ax.set_xlim(-2, 3)
                self.ax.set_ylim(-2, 3)
                self.ax.scatter(self.X[:,0],self.X[:,1], c = self.t , s=50, cmap='rainbow')
                xx = np.linspace(min(self.X[:,1]), max(self.X[:,1]))
                try:
                    yy = -1*(self.weights[0] * xx + self.wbias) / self.weights[1]
                except ZeroDivisionError:
                    yy = -1*(self.weights[0] * xx + self.wbias) / 0.1
                self.ax.plot(xx, yy, label = 'Perseptron Line')
                self.ax.legend(loc="best")
                import time
                time.sleep(0.2)
                self.canvas.draw()
            e+=1

            print(self.weights[0],self.weights[1],self.wbias)

    def draw_class(self,event):
        if self.perline:
            linear_output = np.dot([event.xdata,event.ydata], self.weights) + self.wbias
        else:
            linear_output = np.dot([event.xdata,event.ydata], [self.w1.get(),self.w2.get()]) + self.w0.get()*(-1)
        y_predicted = self.step(linear_output)
        if y_predicted==1:
            self.ax.plot(event.xdata,event.ydata,'rX')
        else:
            self.ax.plot(event.xdata,event.ydata,'bX')

        self.canvas.draw()

    # step function
    @staticmethod
    def step(x):
        return np.where(x>=0, 1, 0)
            

Persepton_Weights_Impact_Illustrator()
