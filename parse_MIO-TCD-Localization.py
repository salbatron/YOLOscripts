import random
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

classes = ["articulated_truck", "bicycle", "bus", "car", "motorcycle", "motorized_vehicle", "non-motorized_vehicle", "pedestrian", "pickup_truck", "single_unit_truck", "work_van"]
id_num = [7, 1, 5, 2, 3, 84, 85, 0, 82, 7, 80]

lines = open('X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\MIO-TCD\\MIO-TCD-Localization\\gt_train.csv').read().splitlines()
i = 0
flag = '0'
#out = open('classifier_new_12class2.txt', 'w')
num_lines = sum(1 for line in lines)
while(num_lines):
    num_lines = num_lines-1
    print num_lines
    line = lines[i]
    data = line.split(',')
    img = Image.open(data[0]+'.jpg')
    width, height = img.size
    img.close()
    xmin = float(data[2])
    ymin = float(data[3])
    xmax = float(data[4])
    ymax = float(data[5])

    xcenter = (xmax + xmin)/2
    ycenter = (ymax + ymin)/2

    x = round(float(xcenter)/float(width), 6)
    y = round(float(ycenter)/float(height), 6)

    w = round(float(xmax-xmin)/float(width), 6)
    h = round(float(ymax-ymin)/float(height), 6)

    txt_file = data[0]
    if flag == '0':
        flag = txt_file
        txt_out = open(txt_file+'.txt', 'a')
    
    a = data[1]
    j=0
    for cls in classes:
        if cls == a:
            if flag != txt_file:
                txt_out.close()
                flag = txt_file
                txt_out = open(txt_file+'.txt', 'a')
            txt_out.write(str(id_num[j]) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
        j = j+1
    i = i + 1

