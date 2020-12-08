#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:50:38 2020

@author: CagriCivici
"""

# this script provides to gather pictures which be generated or is original into one graph

import matplotlib.pyplot as plt
import numpy as np
import os 

import PIL
from PIL import Image


def gathering(path):
    path = path
    imgsr= []

    
    valid_images = [".jpg",".gif",".jpeg",".tga"]
    
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgsr.append(Image.open(os.path.join(path,f)))
    
    print("aç")
  
   
    column = 10
    row = (len(imgsr)/10) 
    ax = []
    fig = plt.figure(figsize=(160, 240))
    print(len(imgsr))
    imgsr.show
        
    
    
    

    
    
    
    

    
    

