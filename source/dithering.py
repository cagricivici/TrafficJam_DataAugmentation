#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:58:25 2020

@author: CagriCivici
"""
#this script serves converting black and white with dithering 


import PIL
from PIL import Image

def rgb_to_wh (path,image,name):
    path = path
    image = image
    name = name
    
    
    #image.convert('L):grayscale
    #image.convert('P'): RGB
    #image.convert('1'): dither mode
    # https://pillow.readthedocs.io/en/5.1.x/reference/Image.html
    image = image.convert('1') #from rgb to blackwhite with dithering
    
    #saving
    image.save(path+'converted_'+name)
    
    
    
    
