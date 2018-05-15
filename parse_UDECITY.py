import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

with open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\UDACITY SELF-DRIVING\\object-detection-crowdai\\labels.csv') as f:
    lines = f.readlines()
    num_lines = sum(1 for line in lines)
    i=1
    while(num_lines):
        line = lines[i]
        data = line.split(',')
        img = Image.open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\UDACITY SELF-DRIVING\\object-detection-crowdai\\'+data[4])
        width, height = img.size
        img.close()
        xmin = float(data[0])
        ymin = float(data[1])
        xmax = float(data[2])
        ymax = float(data[3])

        xcenter = (xmax + xmin)/2
        ycenter = (ymax + ymin)/2

        x = round(float(xcenter)/float(width), 6)
        y = round(float(ycenter)/float(height), 6)

        w = round(float(xmax-xmin)/float(width), 6)
        h = round(float(ymax-ymin)/float(height), 6)

        txt_file = data[4]
        a = data[5]
        txt_out = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\UDACITY SELF-DRIVING\\object-detection-crowdai\\'+txt_file[0:-4]+'.txt', 'a')
        if a == 'Car':
            txt_out.write(str(0) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
        if a == 'Truck':
            txt_out.write(str(1) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
        if a == 'Pedestrian':
            txt_out.write(str(2) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
        txt_out.close()
        num_lines = num_lines -1
        i = i+1
        print i
    
    
    
