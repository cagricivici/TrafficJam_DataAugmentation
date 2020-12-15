#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:31:56 2020

@author: CagriCivici
"""

import PIL
from PIL import Image

def splitting(path, image, name):
    path = path
    image = image
    name = name
    r,g,b = 0,0,0
    
    #This 'Split' method returns a tuple of individual image bands(r,g,b) from an image.
    r,g,b = image.split() 
    
    #merging: (r,g,b) replace (b,g,r)
    image = Image.merge("RGB",(b,g,r)) 
    #saving
    image.save(path +'splitting_'+name)
    
    

