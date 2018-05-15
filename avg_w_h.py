#calculate average width and height of all images in training dataset
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image
          
with open('E:\\WORK\\projects\\YOLO_train\\obj_detector.txt') as f:
    lines = f.readlines()
    num_lines = sum(1 for line in lines)
    print num_lines
    i=0
    w=0
    h=0
    while(num_lines):
        line = lines[i]
        line = "X" + line[1:-1]
        #print line
        img = Image.open(line)
        width, height = img.size
        w=w+width
        h=h+height
        img.close()
        num_lines = num_lines - 1
        #print i
        print w/(i+1), h/(i+1)
        i = i + 1
    f.close()
print w/(i+1), h/(i+1)
