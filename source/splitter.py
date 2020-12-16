#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:31:56 2020

@author: CagriCivici
"""

#this script serves splitting rgb pixels
#rgb sequence --- rbg sequence

import PIL
from PIL import Image

import cv2 as cv
import numpy as np


def splitting(saving_path,img_path, imgname):  
    
    s_path = saving_path #saving directory
    path = img_path      #fetch image directory        
    name = imgname       #saving image with sutiable prefix name
    
    #init for rgb pixels
    r,g,b = 0,0,0
    
    #read image with opencv
    image = cv.imread(path)

    #splitting pixels
    b,g,r = cv.split(image)
    
    #merging for newImage
    newImg = cv.merge((r,b,g))

    #saving image
    cv.imwrite(s_path+ 'splt_'+name, newImg)
    
    
    
    
    
  