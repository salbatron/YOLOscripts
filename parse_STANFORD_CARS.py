import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

a=1     

for filename in os.listdir("Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\STANFORD CARS\\cars_train\\cars_train"):
    if not filename.endswith('.txt'): continue
    img_path = 'Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\STANFORD CARS\\cars_train\\cars_train\\' + filename[0:-4] + '.jpg'
    txt_file = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\STANFORD CARS\\cars_train\\cars_train\\'+filename)
    lines = txt_file.read()
    txt_file.close()
    data = lines.split(' ')
    
    img = Image.open(img_path)
    width, height = img.size
    img.close()
    xmin = float(data[1])
    ymin = float(data[2])
    xmax = float(data[3])
    ymax = float(data[4])

    xcenter = (xmax + xmin)/2
    ycenter = (ymax + ymin)/2

    x = round(float(xcenter)/float(width), 6)
    y = round(float(ycenter)/float(height), 6)

    w = round(float(xmax-xmin)/float(width), 6)
    h = round(float(ymax-ymin)/float(height), 6)
    
    txt_file = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\STANFORD CARS\\cars_train\\cars_train\\'+filename, 'w')
    txt_file.write(str(0) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
    txt_file.close()
    print a
    a = a+1

    
    

    
