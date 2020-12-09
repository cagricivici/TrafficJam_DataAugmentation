#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:19:30 2020

@author: CagriCivici
"""
#this script provides image to add noise 


import numpy as np
import skimage as sk
from skimage import util

import PIL
from PIL import Image

# skimage.util.random_noise(image[, mode, …])
# Function to add random noise of various types to a floating-point image.
#https://scikit-image.org/docs/dev/api/skimage.util.html  
def noising (path,image,name): # image_array: ndarray
    #adding random noise on image
    path = path
    name = name
    img = np.array(image)
    # print(img)
    # print('added')
    noise_salt_img = util.random_noise(img,mode = 'salt')
    
    # print(noise_salt_img)
    
    noise_img = np.array(255*noise_salt_img, dtype = 'uint8')

    imgk = Image.fromarray(noise_img, 'RGB')
    imgk.save(path+'noise_'+name)
