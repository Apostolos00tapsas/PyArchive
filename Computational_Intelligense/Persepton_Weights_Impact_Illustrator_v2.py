from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from sklearn.datasets import make_circles
import numpy as np

"""
Script Name: Persepton_Weights_Impact_Illustrator_v2.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements and illustrates the way that persepton drows a line accoring to AND logical gate problem.

Parameters:
     
    
Returns:
    

Example:
    Persepton_Weights_Impact_Illustrator()
"""

class PSO:
    def __init__(self,num = 50):
        # create create Bull's Eye Dataset as
        self.particles, y = make_circles(n_samples=num ,noise=2.5)
        # Define window
        self.root = Tk()
        self.root.title("PSO")
        self.root.geometry('800x500')

        # Define figure
        self.f = Figure(figsize=(10,6), dpi=100)
        self.ax = self.f.add_subplot(111)
        self.ax.clear()

        # Defibe axis names and plot tiltle
        self.ax.title.set_text("PSO Illustration")
        self.ax.set_xlabel(" x ")
        self.ax.set_ylabel(" y ")

        # Define x y limits
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)
        
        # Define canvas
        self.canvas = FigureCanvasTkAgg(self.f, self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        # Detect canvas x and y 
        self.canvas.mpl_connect('button_press_event',self.illustrate_pso)
        self.root.mainloop()
        
    def illustrate_pso(self, event):
        self.ax.plot(event.xdata, event.ydata,'rX')
        self.ax.plot(self.particles[:,0],self.particles[:,1],'b1')
        self.canvas.draw()

        #Define Current Velocity
        self.cv = self.particles

        #Define Personal Best
        self.pb = np.empty(self.cv.shape)

        #Define Global Best
        self.gb = np.empty(self.cv.shape)

        #Define Velocity
        self.v = np.zeros(self.cv.shape)

        #Define Current Velocity Impact
        self.VI = 0.2
        
        #Define Personal Impact
        self.PI = 0.8

        
        #Define Global Impact
        self.GI = 0.1

        
        # Start Algorith
        for i in range(0,10): 
            # Update Velocity
            self.v[0] = (self.VI*(np.random.randn()) * self.cv[0]) + (self.PI*(np.random.randn() * (self.pb[0] - self.cv[0]))) + (self.GI*(np.random.randn() * (self.gb[0] - self.cv[0])))
            # Ypdate Position
            self.cv[0] += self.v[0]

            # Updata personal best
            if self.fun(self.cv[0][0],self.cv[0][0]) < self.fun(self.pb[0][0],self.pb[0][0]):
                self.pb = self.cv
            
            self.ax.clear()
            self.ax.title.set_text("PSO Illustration")
            self.ax.set_xlabel(" x ")
            self.ax.set_ylabel(" y ")
            self.ax.set_xlim(-20, 20)
            self.ax.set_ylim(-20, 20)
            self.ax.plot(event.xdata, event.ydata,'rX')
            self.ax.plot(self.v[0][0],self.v[0][1],'b1')
            import time 
            time.sleep(1)
            self.canvas.draw()

    def fun(self,x,y):
        return 100 * ((y - (x**2))**2) + ((1 - (x**2))**2)

        
                                                                                                            
                                                                                                                 
        
        
        

PSO()
