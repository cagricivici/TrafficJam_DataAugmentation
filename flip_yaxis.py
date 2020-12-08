#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:21:05 2020

@author: CagriCivici
"""
#this script provides image to flip in horizontal axis 


import PIL
from PIL import Image


#using Pillow, image will be fliped with a few lines
def flipping (path,image,name):
    path = path
    image = image
    name = name
    
    out = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    # image.show()
    out.save(path+'transpose_'+name)
    # print("horizontal")
    


