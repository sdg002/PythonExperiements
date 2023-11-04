'''
In this example we will plot a circle with points scatterred around 
the circumfrence with a Gaussian distribution
'''
import matplotlib.pyplot as plt
import math
import numpy as np
from  Common import Util

list_x=list()
list_y=list()
radius=10
center_x=0
center_y=0
num_points=100
angles=np.linspace(0,2.0*3.141,num_points)
for angle in angles:
    x=math.sin(angle)*radius
    y=math.cos(angle)*radius
    list_x.append(x)
    list_y.append(y)
    stddev=1
    arr_cluster=Util.GenerateClusterOfRandomPointsAroundXY(x,y,stddev,20)
    cluster_shape=arr_cluster.shape
    for idx in range(0,cluster_shape[0]):
        x_cluster=arr_cluster[idx][0]; 
        y_cluster=arr_cluster[idx][1];
        list_x.append(x_cluster)
        list_y.append(y_cluster)



#
#plot the function
#
fig = plt.figure()
ax = plt.axes()
#
#Set the same scale on X and Y axis
#
lst_limits=[min(list_x),max(list_x),min(list_y),max(list_y)]
plt.xlim(min(lst_limits)-3, max(lst_limits)+3)
plt.ylim(min(lst_limits)-3, max(lst_limits)+3)
plt.gca().set_aspect('equal', adjustable='box')
#
#Show a grid
#
ax.grid(True, which='both')
plt.scatter(list_x,list_y,s=1) 
plt.show()
pass
