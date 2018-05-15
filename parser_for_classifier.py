import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

names = open('E:\\WORK\\projects\\YOLO_train\\all.names')
line_names = names.readlines()
          
with open('E:\\WORK\\projects\\YOLO_train\\test_dwg_ube.txt') as f:
    lines = f.readlines()
    num_lines = sum(1 for line in lines)
    i=0
    while(num_lines):
        line = lines[i]
        line = line[0:-1]
        print line
        img = Image.open(line)
        width, height = img.size
        
        txt_file = line[0:-4]+'.txt'
        with open(txt_file) as f1:
            lines1 = f1.readlines()
            num_lines1 = sum(1 for line in lines1)
            j = 0
            while(num_lines1):
                
                line1 = lines1[j]
                data = line1.split(' ')

                label = line_names[int(data[0])]

                x_center = float(width)*float(data[1])
                y_center = float(height)*float(data[2])
                w = float(width)*float(data[3])
                h = float(height)*float(data[4])
                x1 = x_center - w/2
                y1 = y_center - h/2
                x2 = x_center + w/2
                y2 = y_center + h/2

                crop_img = img.crop((x1, y1, x2, y2))
                save_name = 'X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\TEST_CLASSIFIER\\DETRAC_TRAIN_PART\\' + str(i) +'_' + str(j) +'_'+ label[0:-1] + '.jpg'
                
                crop_img.save(save_name)
                j = j + 1
                num_lines1 = num_lines1 - 1 
        f1.close()
        img.close()
        num_lines = num_lines - 1
        print i
        i = i + 1
    f.close()
