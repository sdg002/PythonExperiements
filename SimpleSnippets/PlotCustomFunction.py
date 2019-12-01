'''
This example demonstrates how to plot the results of a custom
univariate function. 
Example:
    Conside a function f(x)
    For values of x ranging from x=0 to x=100
    Plot the results of f(x) using Matplot lib
'''


import numpy as np
import matplotlib.pyplot as plt


def MyCustomStraightLing(x):
    m=2
    c=1
    y=m*x+c
    return y

x_start=-3
x_end=3
xvalues = np.linspace(x_start, x_end, 1000)
print(*xvalues,sep="\n")
#
#Use the vectorize method of Numpy to generate outputs over a sequence of inputs
#
vfunc=np.vectorize(MyCustomStraightLing)
yvalues=vfunc(xvalues)
yvalues
#
#plot the function
#
fig = plt.figure()
ax = plt.axes()
xlist=list(xvalues)
#
#Set the same scale on X and Y axis
#
plt.xlim(x_start-3, x_end+3)
plt.ylim(x_start-3, x_end+3)
plt.gca().set_aspect('equal', adjustable='box')
#
#Show a grid
#
ax.grid(True, which='both')
ylist=list(yvalues)
plt.plot(xlist,ylist) 

###you were here, MyFunc is not defined
plt.show()
pass
