
'''
Demonstrates how to generate Salt and Pepper noise over a blank image. We have varied the parameter salt_vs_pepper to control the black and white
'''

import numpy as np
import matplotlib.pyplot as plt
import os
import skimage

folder_script=os.path.dirname(__file__)
file_input=os.path.join(folder_script,"White.png")
image_blank=skimage.io.imread(file_input)
image_blank_gray=skimage.color.rgb2gray(image_blank)
image_noisy_2=skimage.util.random_noise(image_blank_gray,mode="s&p",seed=None, clip=True,salt_vs_pepper=0.2)
image_noisy_5=skimage.util.random_noise(image_blank_gray,mode="s&p",seed=None, clip=True,salt_vs_pepper=0.5)
image_noisy_8=skimage.util.random_noise(image_blank_gray,mode="s&p",seed=None, clip=True,salt_vs_pepper=0.8)
file_result_2=os.path.join(folder_script,"./../out","Results.2.png")
file_result_5=os.path.join(folder_script,"./../out","Results.5.png")
file_result_8=os.path.join(folder_script,"./../out","Results.8.png")
skimage.io.imsave(file_result_2,image_noisy_2)
skimage.io.imsave(file_result_5,image_noisy_5)
skimage.io.imsave(file_result_8,image_noisy_8)

