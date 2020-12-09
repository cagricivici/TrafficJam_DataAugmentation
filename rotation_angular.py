#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:20:38 2020

@author: CagriCivici
"""
#this script provides image to rotate in spesific angle

import random

def rotating(path,image,name):
    path = path
    image = image
    name = name
    #rotate angular between 75' on the left and 75' on the right
    random_value = random.uniform(-75,75)
    rotated_pic     = image.rotate(random_value)
    rotated_pic.save(path+'rotation_'+name)
    #rotated_pic.show()

