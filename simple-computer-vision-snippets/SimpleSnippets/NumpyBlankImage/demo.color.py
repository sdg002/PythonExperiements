import numpy as np
import skimage
import os

width=120
height=60
arr=np.zeros([height,width,3], dtype='float')
color_red=255
color_green=255
color_blue=0
for y in range(0,height):
    for x in range(0,width):
        arr[y][x][0]=color_red
        arr[y][x][1]=color_green
        arr[y][x][2]=color_blue
file_script=__file__
folder_script=os.path.dirname(file_script)
filename_result="Numpy.ColorImage.%d.%d.%d.png" % (color_red, color_green,color_blue)
file_result=os.path.join(folder_script,"../out/",filename_result)
skimage.io.imsave(file_result,arr)
pass
