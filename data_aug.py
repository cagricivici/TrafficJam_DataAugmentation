#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:35:28 2020

@author: CagriCivici
"""
#image augmentation basic example

import random
import os
import PIL
from PIL import Image
#out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)


import add_noise
import flip_yaxis
import rotation_angular
import dithering
import splitter
import cropper


print('code executed!') 


#image augmentations: angular_rotation, adding_noise, horizontal_flip
#thanks to scikit image, we can use transform mode! (sk.transform.xxxx) 
#https://scikit-image.org/docs/dev/api/skimage.transform.html


# Open the image form working directory
#image = Image.open('/Users/CagriCivici/Desktop/python_ws/data_augmentation/jamtraffic/images.jpeg')
# summarize some details about the image


path_aug = '/Users/CagriCivici/Desktop/python_ws/data_augmentation/augmented/'#path for augmented images


imgs = []


#get all images from path : original_pic
valid_images = [".jpg",".gif",".jpeg",".tga"]
for f in os.listdir(path_aug):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(Image.open(os.path.join(path_aug,f)))
    
print('loaded ' + str(len(imgs))+ ' images')


images_count = len(imgs)


for i in range(images_count):
    img_name = imgs[i].filename.split('/')
    img_name = img_name[(len(imgs[i].filename.split('/'))-1)]
    r1 = random.randint(0, 5)
    #pic_name = imgs[i].filename[len(imgs[i].filename.split('/'))-1]
    
    
    if (r1==0): 
        print(str(i) + "th angular rotaion process")
        rotation_angular.rotating(path_aug,imgs[i],img_name) #point to augmented file 
        
    elif (r1==1):        
        print(str(i) +"th adding noise process")
        add_noise.noising(path_aug,imgs[i],img_name)         #point to augmented file 
       
    elif(r1==2) : 
        print(str(i) +"th horizontal flip")
        flip_yaxis.flipping(path_aug,imgs[i],img_name)      #point to augmented file 
    elif(r1==3):
        print(str(i) + "th RGB to black&white convert")
        dithering.rgb_to_wh(path_aug,imgs[i],img_name)
    elif(r1==4):
        print(str(i) + "th splitting image")
        splitter.splitting(path_aug,imgs[i],img_name)
    else:
        print(str(i) + "th cropped image")
        cropper.cropping(path_aug,imgs[i],img_name)
        
    
    
    
              
        
        





    

