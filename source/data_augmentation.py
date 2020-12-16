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



#importing environmental methods which help to manipulate and augment images.
import add_noise
import flip_yaxis
import rotation_angular
import dithering
import splitter
import cropper

def main():

    print("data_aug.py executed")

    #path
    path_aug = '/Users/CagriCivici/Desktop/python_ws/data_augmentation/augmented/'#path for augmented images
    #this path contains images without manipulation at the begining of process.

    #get images into array
    imgs = []


    #get all images from path : augmented folder

    #this for loop serves to gather images which are at all format such as jpeg or png
    valid_images = [".jpg",".gif",".jpeg",".png"]
    for f in os.listdir(path_aug):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(path_aug,f)))

        print('loaded ' + str(len(imgs))+ ' images') # how many pictures are gathered

        images_count = len(imgs)


    #image augmentation process
    for i in range(images_count):

        #getting image name
        img_name = imgs[i].filename.split('/')
        img_name = img_name[(len(imgs[i].filename.split('/'))-1)]


        #random selection
        r1 = random.randint(0, 5)

        if (r1==0):
            print(str(i) + "th angular rotaion process")
            rotation_angular.rotating(path_aug,imgs[i],img_name) #angular rotation

        elif (r1==1):
            print(str(i) +"th adding noise process")
            add_noise.noising(path_aug,imgs[i].filename,img_name)         #adding noise on images

        elif(r1==2) :
            print(str(i) +"th horizontal flip")
            flip_yaxis.flipping(path_aug,imgs[i],img_name)      #flipping images

        elif(r1==3):
            print(str(i) + "th RGB to black&white convert")
            dithering.rgb_to_wh(path_aug,imgs[i],img_name)      #converting from RGB to Black&White

        elif(r1==4):
            print(str(i) + "th splitting image")
            splitter.splitting(path_aug,imgs[i].filename,img_name)       #splitting

        else:
            print(str(i) + "th cropped image")
            cropper.cropping(path_aug,imgs[i],img_name)         #croping images


#main block
if __name__ == '__main__':
    print('code executed')
    main()

#run different main source
else:
    print("code executed by other main running progress")










# Open images form working directory
#image = Image.open('/Users/CagriCivici/Desktop/python_ws/data_augmentation/jamtraffic/images.jpeg')
