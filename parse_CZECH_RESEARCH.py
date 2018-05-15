import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

with open('C:\\Users\\abibulic\\Desktop\\images\\labels.csv') as f:
    lines = f.readlines()
    num_lines = sum(1 for line in lines)
    i=0
    while(num_lines):
        line = lines[i]
        data = line.split(' ')
        img = Image.open('C:\\Users\\abibulic\\Desktop\\images\\'+data[0])
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

        txt_file = data[0]
        
        txt_out = open('C:\\Users\\abibulic\\Desktop\\images\\'+txt_file[0:-4]+'.txt', 'a')
        txt_out.write(str(0) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
        txt_out.close()
        num_lines = num_lines -1
        i = i+1
        print i
    
    
    
