import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

with open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\CZECH RESEARCH\\2015-DICTA-VehiclesGrouping-dataset\\dataset\\images\\list.txt') as f:
    lines = f.readlines()
    num_lines = sum(1 for line in lines)
    i=0
    while(num_lines):
        line = lines[i]
        txt_in = open(line[0:-1])
        first_line = txt_in.readlines()
        txt_in.close()
        num_lines2 = sum(1 for line in first_line)
        if num_lines2 > 1:
            first_line = first_line[0]
            data = first_line.split(' ')
            img = Image.open(line[0:-5]+'.png')
            width, height = img.size
            img.close()
            xmin = float(data[0])
            ymin = float(data[1])
            xmax = float(data[2])+xmin
            ymax = float(data[3])+ymin
            xcenter = (xmax + xmin)/2
            ycenter = (ymax + ymin)/2

            x = round(float(xcenter)/float(width), 6)
            y = round(float(ycenter)/float(height), 6)

            w = round(float(xmax-xmin)/float(width), 6)
            h = round(float(ymax-ymin)/float(height), 6)

            txt_out = open(line[0:-1], 'w')
            txt_out.write(str(0) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
            txt_out.close()
        num_lines = num_lines -1
        i = i+1
        print i
    
    
    
