#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:19:30 2020

@author: CagriCivici
"""
#this script serves adding random noise on images

#importing libs
import numpy as np
import skimage as sk
from skimage import util

import PIL
from PIL import Image


# skimage.util.random_noise(image[, mode, …])
# Function to add random noise of various types to a floating-point image.
#https://scikit-image.org/docs/dev/api/skimage.util.html  


def noising (path,image,name): 
    
    path = path
    name = name
    img = np.array(image)

    #adding random noise with skimage
    #mode: salt!
    noise_salt_img = util.random_noise(img,mode = 'salt')
    
    #converting images to visualable with mulplying by 255
    #
    noise_img = np.array(255*noise_salt_img, dtype = 'uint8')
    
    #from piloow lib: 
    #saving an RGB image using PIL. Now we can use fromarray to create a PIL image from the numpy array
    #https://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/
    #Image.fromarray(noised_image, "RGB): transform to pillow image from numpy array
    imgk = Image.fromarray(noise_img, "RGB")
    
    #saving image
    imgk.save(path+'noise_'+name)
