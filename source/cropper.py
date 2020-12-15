#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:44:59 2020

@author: CagriCivici
"""
#this script serves cropping images on x and y axes.


import PIL
from PIL import Image


def cropping(path,image,name):
    path = path
    image = image
    name = name
    
    
    #gets its size
    width, height = image.size 
      
    # set coordinates when cropping an image with PIL
    left = width * (0.14)
    top = height / 4
    right = width - left
    bottom = height
    
    # Cropped image of above dimension 
    # (It will not change orginal image) 
    

    #box – The crop rectangle, as a (left, upper, right, lower)-tuple.
    im1 = image.crop((left, top, right, bottom))
    
    #resize as its orginal picture
    im1 = im1.resize((width,height), Image.ANTIALIAS)
    
    im1.save(path+"cropped_"+name)
  
    
    













#im1.show() 

#(left, top, right, bottom) - https://pillow.readthedocs.io/en/stable/reference/Image.html
#img.crop((box)) ----- box:left, top, right, bottom   (x1,y2,x2,y1)








