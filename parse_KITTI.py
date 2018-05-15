import random
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

classes = ["Car", "Van", "Truck", "Pedestrian", "Person_sitting", "Cyclist", "Tram", "Misc"]
id_num = [2, 80, 7, 0, 0, 1, 87, 86]

lines = open('X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\KITTI\\data_object_label_2\\training\\label_2\\train.txt').read().splitlines()
i = 0

num_lines = sum(1 for line in lines)
while(num_lines):
    num_lines = num_lines-1
    print num_lines
    line = lines[i]
    if not os.path.exists('X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\KITTI\\data_object_image_2\\training\\image_2\\'+line[106:-4]+'.txt'):
        txt_out = open('X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\KITTI\\data_object_image_2\\training\\image_2\\'+line[106:-4]+'.txt', 'a')
        img = Image.open('X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\KITTI\\data_object_image_2\\training\\image_2\\'+line[106:-4]+'.png')
        width, height = img.size
        lines2 = open(line).read().splitlines()
        num_lines2 = sum(1 for line2 in lines2)
        j = 0
        while(num_lines2):
            num_lines2 = num_lines2-1
            line2 = lines2[j]
            data = line2.split(' ')
       
            xmin = float(data[4])
            ymin = float(data[5])
            xmax = float(data[6])
            ymax = float(data[7])

            xcenter = (xmax + xmin)/2
            ycenter = (ymax + ymin)/2

            x = round(float(xcenter)/float(width), 6)
            y = round(float(ycenter)/float(height), 6)

            w = round(float(xmax-xmin)/float(width), 6)
            h = round(float(ymax-ymin)/float(height), 6)

        
    
            a = data[0]
   
            k = 0
            if a == 'DontCare':
                draw = ImageDraw.Draw(img)
                draw.rectangle(((xmin, ymin), (xmax, ymax)), fill="black", outline = "black")
                img.save('X:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\KITTI\\data_object_image_2\\training\\image_2\\'+line[106:-4]+'.png')
            else:
                for cls in classes:
                    if cls == a:
                        txt_out.write(str(id_num[k]) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
                    k = k +1
            j = j+1
        txt_out.close()
        img.close()
    i = i + 1

