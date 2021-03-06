# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:44:32 2018

@author: shahrear
student.eco86@gmail.com
© Md. Shahrear Zaman
Reference Book:
Economic Dynamics
4th Edition
2010
by 
Giancarlo Gandolfo
Ref Link: https://matplotlib.org/examples/mplot3d/lorenz_attractor.html
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def linline(x, y, z, s=0.1, r=0.01):
    x_dot =  y
    y_dot = -(s**2)*x - 2*r*y 
    z_dot = 0
    return x_dot, y_dot, z_dot


dt = 0.01
n = 10000

x = np.empty((n + 1,))
y = np.empty((n + 1,))
z = np.empty((n + 1,))

# Setting initial values
#x[0], y[0], z[0] = (0.1, 0.1, 0.1)
x[0], y[0], z[0] = (0, 1, 0)

# Stepping through "time".
for i in range(n):
    x_dot, y_dot, z_dot = linline(x[i], y[i], z[i])
    x[i + 1] = x[i] + (x_dot * dt)
    y[i + 1] = y[i] + (y_dot * dt)
    z[i + 1] = z[i] + (z_dot * dt)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z, lw=2.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Phase Diagram")

plt.show()

# s=1,r=1
#z_dot = x*y
#z_dot = -0.5*z

#   x_dot =  y
#   y_dot = -(s**2)*x - 2*r*y 
#   z_dot = y

#    x_dot =  y + z
#    y_dot = -(s**2)*x - 2*r*y 
#    z_dot = y

#   x_dot =  y + z
#   y_dot = -(s**2)*x - 2*r*y +z
#   z_dot = y


#   s=10, r=1
#

#    s=1, r=1
#    x[0], y[0], z[0] = (0, 1., 0)
#    x_dot =  z
#    y_dot = -(s**2)*x - 2*r*y 
#    z_dot = y 

#   s=1, r=1
#   x[0], y[0], z[0] = (0, 1., 0)
#   x_dot =  z
#   y_dot = -(s**2)*x - 2*r*y + z
#   z_dot = y
