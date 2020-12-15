#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:21:05 2020

@author: CagriCivici
"""
#this script serves flipping images on specific axis 


import PIL
from PIL import Image


#using Pillow, image could be flipped with a few lines

def flipping (path,image,name):
    path = path
    image = image
    name = name
    
    #image transpose means flipping on axes 
    #method – One of PIL.Image.FLIP_LEFT_RIGHT, PIL.Image.FLIP_TOP_BOTTOM, PIL.Image.ROTATE_90 ...
    #PIL.Image.ROTATE_180, PIL.Image.ROTATE_270, PIL.Image.TRANSPOSE or PIL.Image.TRANSVERSE.
    #https://pillow.readthedocs.io/en/stable/reference/Image.html

    out = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)

    #saving
    out.save(path+'transpose_'+name)

    


