from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

"""
Script Name: Take_xydata_from_Canvas.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Creates a canvas that the user can select(via clicking on canvas) a point on Canvas.
    This GUI is usefull for some computationals algorithms illustration such as PSO. Or xor, and 
    lofical gates problems used in perseptron presentation. 

Parameters: 
    
Returns:
    

Example:
    create_and_take_canvas_xy()
"""


class create_and_take_canvas_xy:
    def __init__(self):
        #Define x,y
        self.x = 0
        self.y = 0

        # Define window
        self.root = Tk()
        self.root.title("Create And Take Canvas xy")
        self.root.geometry('800x500')

        # Define figure
        self.f = Figure(figsize=(10,6), dpi=100)
        self.ax = self.f.add_subplot(111)
        self.ax.clear()

        # Defibe axis names and plot tiltle
        self.ax.title.set_text("Illustration")
        self.ax.set_xlabel(" x ")
        self.ax.set_ylabel(" y ")

        # Define x y limits
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        
        # Define canvas
        self.canvas = FigureCanvasTkAgg(self.f, self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        # Detect canvas x and y 
        self.canvas.mpl_connect('button_press_event',self.drowxy)
        self.root.mainloop()

    def getxy(self):
        return self.x, self.y
    
    def drowxy(self,event):
        self.x, self.y = event.xdata, event.ydata
        print(self.getxy())
        self.ax.plot(event.xdata, event.ydata,'ro')
        self.canvas.draw()
        
        
        
        

create_and_take_canvas_xy()

