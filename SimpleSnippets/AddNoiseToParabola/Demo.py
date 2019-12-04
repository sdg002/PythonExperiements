'''
In this example 
    we will plot a parabola with the equation y=x**x + 3
    We will use np.random.normal to generate Gaussian noise for every point of the parabola
    We will also add some Salt and Pepper noise
'''
import numpy as np
import matplotlib.pyplot as plt
import os
import random
import math
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
def MyCustomParabola(x):
    c=1
    y=x*x+c
    return y
#
#Use the vectorize method of Numpy to generate outputs over a sequence of inputs
#
vfunc=np.vectorize(MyCustomParabola)
y_original=vfunc(xvalues)
#
#Create a Numpy array to hold the original X,Y
#
arr_original=np.zeros((len(xvalues), 2))
arr_distorted=np.zeros((len(xvalues), 2))
for index in range(0,len(xvalues)):
    arr_original[index][0]=xvalues[index];
    arr_original[index][1]=y_original[index];
#
#Create normally distributed Gaussian data
#https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
#
stddev=0.3 #this gives a decent amount of noise
mean=0
noise = np.random.normal(mean, stddev, len(xvalues))   
#
#Iterate through all the original x,y values and use the Gaussian noise to shift the original 
#
lst_dist_x=[]
lst_dist_y=[]
for index in range(0,len(xvalues)):
    original_x=arr_original[index][0];
    original_y=arr_original[index][1];
    theta=random.random() * 2 * 3.1415
    noise_radius=noise[index]
    distorted_x = math.cos(theta) * noise_radius
    distorted_y = math.sin(theta) * noise_radius
    new_x=distorted_x+original_x
    new_y=distorted_y+original_y
    arr_distorted[index][0]=new_x
    arr_distorted[index][1]=new_y
    lst_dist_x.append(new_x)
    lst_dist_y.append(new_y)

pass
#
#plot the function
#
fig = plt.figure()
ax = plt.axes()
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
plt.scatter(lst_dist_x,lst_dist_y) 
folder_script=os.path.dirname(__file__)
file_image=os.path.join(folder_script,"../out","Results.png")
plt.savefig(file_image)
plt.show()
pass
