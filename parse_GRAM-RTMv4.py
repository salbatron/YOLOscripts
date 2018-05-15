import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["car", "truck", "van", "big-truck"]


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(a):
    in_file = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\GRAM-RTM\\xml\\%d.xml'%(a))
    out_file = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\GRAM-RTM\\GRAM-RTMv4\\Annotations\\Urban1\\labels\\image%06d.txt'%(a+1), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('class').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

a = 0
while a<=23434:
    if not os.path.exists('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\GRAM-RTM\\GRAM-RTMv4\\Annotations\\Urban1\\labels'):
        os.makedirs('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\GRAM-RTM\\GRAM-RTMv4\\Annotations\\Urban1\\labels')
    convert_annotation(a)
    print a
    a = a + 1
