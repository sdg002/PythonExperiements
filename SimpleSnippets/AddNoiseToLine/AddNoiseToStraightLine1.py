'''
In this example we will plot a straight line with the equation y=mx+x
and also add some Gaussian noise to the result
We will use np.random.normal to generate Gaussian noise
'''
import numpy as np
import matplotlib.pyplot as plt
import os

#
#Generate X values
#
x_start=-3
x_end=3
xvalues = np.linspace(x_start, x_end, 20)
print(*xvalues,sep="\n")
#
#Define the straight line function
#
def MyCustomStraightLing(x):
    m=2
    c=1
    y=m*x+c
    return y
#
#Use the vectorize method of Numpy to generate outputs over a sequence of inputs
#
vfunc=np.vectorize(MyCustomStraightLing)
y_original=vfunc(xvalues)
y_original
#
#Create normally distributed Gaussian data
#https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
#
stddev=0.5
mean=0
noise = np.random.normal(mean, stddev, len(xvalues))   
y_distorted = y_original + noise
pass
#
#plot the function
#
fig = plt.figure()
ax = plt.axes()
xlist=list(xvalues)
ylist=list(y_distorted)
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
plt.scatter(xlist,ylist) 
folder_script=os.path.dirname(__file__)
file_image=os.path.join(folder_script,"./../out","Results.png")
plt.savefig(file_image)
plt.show()
pass
