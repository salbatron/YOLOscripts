#put mask for ignored regions in images as gray rectangle
import cv2
import numpy as np
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join


classes = ["car", "van", "bus", "others"]

def convert_annotation(filename):

    in_file = open('Annotations/DETRAC-Train-Annotations-XML/%s'%(filename))
    tree=ET.parse(in_file)
    root = tree.getroot()

    width = 960
    height = 540

    for ignored_region in root.iter('ignored_region'):
         for files in os.listdir('Insight-MVT_Annotation_Train/%s'%(filename[0:-4])):
            if files.endswith('.jpg'):
                img = cv2.imread('Insight-MVT_Annotation_Train/%s/%s'%(filename[0:-4], files))
                for box in ignored_region.iter('box'):
                    x = round(float(box.get('left')))
                    y = round(float(box.get('top')))
                    w = round(float(box.get('width')))
                    h = round(float(box.get('height')))

                    img[int(y):int(y)+int(h),int(x):int(x)+int(w)] = [120,120,120]
                cv2.imwrite('Insight-MVT_Annotation_Train/%s/%s'%(filename[0:-4], files),img)



wd = getcwd()
for filename in os.listdir(wd+"\Annotations\DETRAC-Train-Annotations-XML"):
    if not filename.endswith('.xml'): continue
    convert_annotation(filename)


