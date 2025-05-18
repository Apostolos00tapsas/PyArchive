from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x=[0,0,1,1]
y=[0,1,0,1]
z=[1,0,0,1]
t = [1,0,0,1]

ax.scatter(x, y, z, c=t, cmap='rainbow')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
