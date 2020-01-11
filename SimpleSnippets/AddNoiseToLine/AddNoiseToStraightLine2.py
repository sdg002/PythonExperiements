'''
In this example we will plot a straight line with the equation y=mx+x
and also add some Gaussian noise to the result
We will use np.random.normal to generate Gaussian noise
'''
import numpy as np
import matplotlib.pyplot as plt
import os
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
#Generate a normally distributed random cluster of points around x,y
#
def GenerateClusterOfRandomPointsAroundXY(x,y):
    angleStart=0
    angleEnd=2*3.1415
    angleStepDegrees=10
    angleStepRadians=2*3.1415/360 * angleStepDegrees
    total_angular_movements=12
    angles=np.linspace(angleStart,angleEnd,total_angular_movements)
    mean=0
    stddev=1
    random_radii=np.random.normal(mean, stddev, len(angles)) 
    np_results=np.zeros((len(angles),2))
    for idx in range(0,len(angles)):
        theta=angles[idx]
        radii=abs(random_radii[idx])
        random_x=radii* math.cos(theta)  +x
        random_y=radii* math.sin(theta)  +y
        print("angle=%f,x,y=%f,%f" % (theta,random_x,random_y))
        np_results[idx][0]=random_x
        np_results[idx][1]=random_y

    return np_results

#
#Loop through all points and generate clusters around each x,y
#
list_x=list()
list_y=list()
for index in range(0,len(xvalues)):
    x=xvalues[index]
    y=y_original[index]
    print("x,y  %f,%f" % (x,y))
    arr_cluster=GenerateClusterOfRandomPointsAroundXY(x,y)
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
