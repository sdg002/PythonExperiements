
'''
Demonstrates how to generate speckle noise
'''

import numpy as np
import matplotlib.pyplot as plt
import os
import skimage

folder_script=os.path.dirname(__file__)
file_input=os.path.join(folder_script,"White.png")
image_blank=skimage.io.imread(file_input)
image_blank_gray=skimage.color.rgb2gray(image_blank)
arr_variances=[0.001 , 0.002, 0.004 , 0.006 , 0.008]
for variance in arr_variances:
    image_noisy_var_001=skimage.util.random_noise(image_blank_gray,mode="speckle",seed=None, clip=True,var=variance)
    file_name="Speckle%0.3f.png" % (variance)
    file_result_2=os.path.join(folder_script,"./../out",file_name)
    skimage.io.imsave(file_result_2,image_noisy_var_001)



