#download classes that you need from openimage and make annotations for yolo
import csv
import os
from PIL import Image

CLASS_LIST = ('/m/01g317','/m/04yx4','/m/03bt1vf','/m/05r655','/m/0k4j','/m/01bl7v','/m/02p0tk3','/m/0199g','/m/01bjv','/m/07r04','/m/04_sv','/m/0h2r6','/m/012n7d','/m/01lcw4','/m/0pg52','/m/01jfm_')
img_name = "111111111111"

with open('E:\\WORK\\projects\\YOLO_train\\train-annotations-bbox.csv', newline='') as csvfile:
    bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for bbox in bboxs:
        if bbox[2] in CLASS_LIST:
            if img_name != bbox[0]:
                os.system("gsutil cp gs://open-images-dataset/train/%s.jpg X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\OpenImage\\train"%bbox[0])
                out_file = open("X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\OpenImage\\train\\%s.txt"%bbox[0], 'w')
                img_name = bbox[0]
            if img_name == bbox[0]:
                out_file.write(bbox[2] + " " + str(float(bbox[4])+(float(bbox[5])-float(bbox[4]))/2) + " " + str(float(bbox[6])+(float(bbox[7])-float(bbox[6]))/2)+ " " + str(float(bbox[5])-float(bbox[4])) + " " + str(float(bbox[7])-float(bbox[6])) + '\n')
