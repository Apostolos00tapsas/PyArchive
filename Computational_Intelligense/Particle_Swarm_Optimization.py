from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from sklearn.datasets import make_circles
import random as rand
from tkinter import messagebox


"""
Script Name: Particle_Swarm_Optimization.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements and illustrates the way that particle swarm optimization algorith works.

Parameters:
    swarm (int): The number of swarm. 
    
Returns:
    

Example:
    PSO(swarm)
"""

def fitness(x, y):
            return 100 * ((y - (x**2))**2) + ((1 - (x**2))**2)
      
class PSO:
      def __init__(self,num=30):
          # create create Bull's Eye Dataset as
          self.particles, y = make_circles(n_samples=num ,noise=2.5)
          # Define window
          self.root = Tk()
          self.root.title("PSO")
          self.root.geometry('800x500')

          self.num =num 

          #ToDo objects on right site of canvas
          right_f = Frame(self.root,background='#ff4d4d')
          right_f.pack(side=RIGHT)

          self.l1 = Label(right_f,font=('times new roman',12),text="Define Velocity Impact c1",bg='#ff4d4d')
          self.l1.pack()

          #Define Current Velocity Impact
          self.PI = DoubleVar()
          scale = Scale(right_f, variable = self.PI, from_=0.1, to=1,resolution = 0.1, orient=HORIZONTAL)
          scale.pack(anchor=CENTER)
        
          self.l3 = Label(right_f,font=('times new roman',12),text="Define Global Impact c2",bg='#ff4d4d')
          self.l3.pack()
          
          #Define Current Velocity Impact
          self.GI = DoubleVar()
          scale = Scale(right_f, variable = self.GI, from_=0.1, to=1,resolution = 0.1, orient=HORIZONTAL)
          scale.pack(anchor=CENTER)

          infobtn = Button(right_f, text ="Info", command = self.infomsg)
          infobtn.pack()
          
          # Define figure
          self.f = Figure(figsize=(10,6), dpi=100)
          self.ax = self.f.add_subplot(111)
          self.ax.clear()

          # Defibe axis names and plot tiltle
          self.ax.title.set_text("PSO Illustration")
          self.ax.set_xlabel(" x ")
          self.ax.set_ylabel(" y ")

          # Define x y limits
          self.ax.set_xlim(-200, 200)
          self.ax.set_ylim(-200, 200)
        
          # Define canvas
          self.canvas = FigureCanvasTkAgg(self.f, self.root)
          self.canvas.draw()
          self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

          # Detect canvas x and y 
          self.canvas.mpl_connect('button_press_event',self.illustrate_pso)
          self.root.mainloop()

      def infomsg(self):
          messagebox.showinfo.showinfo("Info", "Define algorithm's parameteres and click to the canvas to start PSO procedure.")
          
      def illustrate_pso(self,event):
            self.x=event.xdata
            self.y=event.ydata
            self.ax.plot(event.xdata, event.ydata,'rX')
            self.ax.plot(self.particles[:,0],self.particles[:,1],'b1')
            self.canvas.draw()

            
            #Variables
            self.n = self.num
            self.num_variables = 2

            #Crear arreglos
            self.a = np.empty((self.num_variables, self.n))
            self.v = np.empty((self.num_variables, self.n))
            self.Pbest = np.empty((self.num_variables, self.n))
            self.Gbest = np.empty((1, 2))
            self.r = np.empty((self.n))

            
            #Llenar arreglos
            for i in range(0, self.num_variables):
                  for j in range(0, self.n):
                        self.Pbest[i][j] = rand.randint(-20, 20)
                        self.a[i][j] = self.Pbest[i][j]
                        self.v[i][j] = 0


            #Llenar r
            for i in range(0, self.n):
                  self.r[i] = fitness(self.a[0][i], self.a[1][i])


            #Ordenar elementos de Pbest
            for i in range(1, self.n):
                  for j in range(0, self.n - 1):
                        if self.r[j] > self.r[j + 1]:
                              #Ordenar el fitness
                              self.tempRes = self.r[j]
                              self.r[j] = self.r[j + 1]
                              self.r[j + 1] = self.tempRes
                              #Ordenar las X, Y
                              self.tempX = self.Pbest[0][j]
                              self.Pbest[0][j] = self.Pbest[0][j + 1]
                              self.Pbest[0][j + 1] = self.tempX

                              self.tempY = self.Pbest[1][j]
                              self.Pbest[1][j] = self.Pbest[1][j + 1]
                              self.Pbest[1][j + 1] = self.tempY
            
            self.Gbest[0][0] = self.x
            self.Gbest[0][1] = self.y

            #Define Current Velocity Impact
            #self.vi = self.VI.get()
        
            #Define Personal Impact
            #self.PI.get() c1      # Exploration   0.1
 
            #Define Global Impact
            #self.GI.get() c2      # Exploitation  0.8
                  
            self.w = 0.5
            epsilon = 0.1
            for i in range (0,50):
                  for i in range(self.n):
                        #Obtener Pbest
                        if(fitness(self.a[0][i], self.a[1][i]) < fitness(self.Pbest[0][i], self.Pbest[1][i])):
                              self.Pbest[0][i] = self.a[0][i]
                              self.Pbest[1][i] = self.a[1][i]
                       
                       #Calculate Velocity
                        for i in range(self.n):
                              #Velocity X
                              self.v[0][i] = self.w * self.v[0][i] + (self.Pbest[0][i] - self.a[0][i]) * rand.random() * self.PI.get() + (self.Gbest[0][0] - self.a[0][i]) * rand.random() * self.GI.get()
                              self.a[0][i] = self.a[0][i] + self.v[0][i]
                              #Velocity Y
                              self.v[1][i] = self.w * self.v[1][i] + (self.Pbest[1][i] - self.a[1][i]) * rand.random() * self.PI.get() + (self.Gbest[0][1] - self.a[1][i]) * rand.random() * self.GI.get()
                              self.a[1][i] = self.a[1][i] + self.v[1][i]
        
                  # Plot Swarm
                  self.ax.clear()
                  self.ax.title.set_text("PSO Illustration")
                  self.ax.set_xlabel(" x ")
                  self.ax.set_ylabel(" y ")
                  self.ax.set_xlim(-200, 200)
                  self.ax.set_ylim(-200, 200)
                  self.ax.plot(event.xdata, event.ydata,'rX')
                  self.ax.plot(self.a[0],self.a[1],'b1')
                  import time 
                  time.sleep(0.2)
                  self.canvas.draw()
                  
                   
swarm = 10
PSO(swarm)
