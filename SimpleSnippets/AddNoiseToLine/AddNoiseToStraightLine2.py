'''
In this example we will plot a straight line with the equation y=mx+x
and also add some Gaussian noise to the result
We will use np.random.normal to generate Gaussian noise
'''
import numpy as np
import matplotlib.pyplot as plt
import os
import math
import GenerateGaussianNoiseAtPoint as gaussianxy
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
#Loop through all points and generate clusters around each x,y
#
list_x=list()
list_y=list()
for index in range(0,len(xvalues)):
    x=xvalues[index]
    y=y_original[index]
    print("x,y  %f,%f" % (x,y))
    stddev=1
    arr_cluster=gaussianxy.GenerateClusterOfRandomPointsAroundXY(x,y,stddev,20)
    print(arr_cluster)
    cluster_shape=arr_cluster.shape
    list_x.append(x)
    list_y.append(y)
    for idx in range(0,cluster_shape[0]):
        x_cluster=arr_cluster[idx][0]; 
        y_cluster=arr_cluster[idx][1];
        list_x.append(x_cluster)
        list_y.append(y_cluster)
pass
#
#plot the function
#
fig = plt.figure()
ax = plt.axes()
#xlist=list(xvalues)
#ylist=list(y_distorted)
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
plt.scatter(list_x,list_y) 
folder_script=os.path.dirname(__file__)
file_image=os.path.join(folder_script,"./../out","Results.png")
plt.savefig(file_image)
plt.show()
pass
