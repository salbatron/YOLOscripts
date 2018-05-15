import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join


classes = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush", "van", "trailer", "pickup", "night vehicle"]


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(filename):
    
    in_file = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\DETRAC\\DETRAC-Train-Annotations-XML\\%s'%(filename))
    tree=ET.parse(in_file)
    root = tree.getroot()
    
    width = 960
    height = 540
    
    for frame in root.iter('frame'):
        name = frame.get('num')
        out_file = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\DETRAC\\DETRAC\\Insight-MVT_Annotation_Train/%s/img%05d.txt'%(filename[0:-4], int(name)), 'w')
        for target in frame.iter('target'):
            for attribute in target.iter('attribute'):
                cls = attribute.get('vehicle_type')
                if cls not in classes:
                    continue
                cls_id = classes.index(cls)
            for box in target.iter('box'):
                x = box.get('left')
                y = box.get('top')
                w = box.get('width')
                h = box.get('height')
                b = (float(x), float(w)+float(x), float(y), float(h)+float(y))
                bb = convert((width,height),b)
                out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()
for filename in os.listdir(wd+"\DETRAC-Train-Annotations-XML"):
    if not filename.endswith('.xml'): continue
    convert_annotation(filename)
    

