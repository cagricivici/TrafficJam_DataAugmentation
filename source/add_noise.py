#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:19:30 2020

@author: CagriCivici
"""
#this script serves adding random noise on images
#opencv for noising

#importing libs
import numpy as np
import skimage as sk
from skimage import util

import PIL
from PIL import Image

import cv2 as cv

#adding noise on image with the help of OpenCV module
#Gaussian Noise selected...


def noising (path,img_path,imgname): 
    
    s_path = path        #saving directory
    path = img_path      #fetch image directory
    name = imgname       #saving image with sutiable prefix name
    
    
    image = cv.imread(path)     #get image with opencv
    
    #Generate Gaussian Noise 
    gauss = np.random.normal(0,1,image.size)
    gauss = gauss.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
    
    #adding noise on image
    image_noise = cv.add(image, gauss)
    #saving image
    cv.imwrite(s_path+ 'ns_'+name, image_noise)
    
    
    
    
    
    
    
    
    
    

