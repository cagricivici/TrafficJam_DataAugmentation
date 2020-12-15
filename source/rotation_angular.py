#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:20:38 2020

@author: CagriCivici
"""
#this script serves rotating images by specific angle 

import random

def rotating(path,image,name):
    path = path
    image = image
    name = name
    
    
    #rotate angular between 75' on the left and 75' on the right
    random_value = random.uniform(-75,75)
    #random rotate
    rotated_pic     = image.rotate(random_value)
    
    #saving
    rotated_pic.save(path+'rotation_'+name)


