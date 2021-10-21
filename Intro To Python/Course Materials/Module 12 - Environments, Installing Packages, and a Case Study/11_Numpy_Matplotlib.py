# -*- coding: utf-8 -*-
"""
Quick Introduction of numpy and matplotlib packages
Introduction to Python Workshop
"""

#Numpy is part of the scipy package that comes along with your Anaconda Distribution
# It works with its main object - arrays

import numpy as np

# Create a 2x2 matrix - outer brackets define the matrix, inner brackets define the rows
A = np.array([[1,2],[3,4]])
print (A)
B = np.array([[10,20],[30,40]])
print (B)

# Can run basic matrix algebra operations from this point
print (A + B)
print (A - B)
print (A * B)
# Look at the third operation output again...
print (np.dot(A,B))
# This is the "dot product" of rows and columns
# [(1*10)+(2*30)],[(1*20)+(2*40)]
# ((3*10)+(4*30)],[(3*20)+(4*40)])

C = np.array([[1],[2],[3]])
print (A + C)
# Error message above because matrices above must be in same dimension
# Try adding a row (or column) with a similar dimension
D = np.array([[1],[2]])
E = np.array([1,2])


## You often do use numpy and matplotlib together
# matplotlib is a good library for scientific data visualization

# These first few examples can be found at the link below, along with some documentation
# https://matplotlib.org/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel('y axis values')
plt.xlabel('x axis values')
plt.show()
# First list above = x values, second list = y values

# Second plot - the 'ro' combination means 'red points', respectively
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0,6,0,20])
plt.ylabel('y axis values')
plt.xlabel('x axis values')
plt.show()

# Use numpy and matplotlib together now
t = np.arange(0, 5, 0.2)
print (t)
plt.plot(t, t*2, 'g--')
plt.show()
# in the plot above, 'g' is for green, and the two dashes indicate a dashed line

# Multiple series in one graph
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'go')
plt.title('Cool title goes here')
plt.show()
# New above - the 'b' for blue and 's' for square, plus the title function


