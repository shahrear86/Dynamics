# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:57:37 2018

@author: shahrear
student.eco86@gmail.com
ref: https://matplotlib.org/examples/mplot3d/lorenz_attractor.html
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lineup(x, y, z, a=10,b=1,c=10,d=1,e=3,f=2,g=3):    
    x_dot = a + b*x 
    y_dot = c + d*x + e*y 
    z_dot = f*y**2 + g*x**2
    return x_dot, y_dot, z_dot


dt = 0.01
n = 10000

# Need one more for the initial values
x = np.empty((n + 1,))
y = np.empty((n + 1,))
z = np.empty((n + 1,))

# Setting initial values
x[0], y[0], z[0] = (1, 1, 2)

# Stepping through "time".
for i in range(n):
    # Derivatives of the X, Y, Z state
    x_dot, y_dot, z_dot = lineup(x[i], y[i], z[i])
    x[i + 1] = x[i] + (x_dot * dt)
    y[i + 1] = y[i] + (y_dot * dt)
    z[i + 1] = z[i] + (z_dot * dt)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z, lw=2.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("")

plt.show()


