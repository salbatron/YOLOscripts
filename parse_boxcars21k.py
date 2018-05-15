import json
from pprint import pprint
from PIL import Image
import unicodedata
from decimal import Decimal

data = json.load(open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\BOXCARS\\2016-CVPR-BoxCars21k-dataset\\BoxCars21k\\BoxCars.json'))
out_txt = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\BOXCARS\\2016-CVPR-BoxCars21k-dataset\\BoxCars21k\\train.txt', 'w')
#starting position
a=0
#end position
b=21249
#intern counter
i=0
#counter
c=0
while(a<=b):
    
    while True:
        try:

            xmin = data["samples"]['%d'%a]['vehicleSamples'][i]["2DBB"][0]
            ymin = data["samples"]['%d'%a]['vehicleSamples'][i]["2DBB"][1]

            xmax = xmin + data["samples"]['%d'%a]['vehicleSamples'][i]["2DBB"][2]
            ymax = ymin + data["samples"]['%d'%a]['vehicleSamples'][i]["2DBB"][3]

            img_path = data["samples"]['%d'%a]['vehicleSamples'][i]["path"]
            img_path = img_path.replace("/", "\\")
            img_path = img_path.encode('utf8')
            img_path = 'Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\BOXCARS\\2016-CVPR-BoxCars21k-dataset\\BoxCars21k\\' + img_path
            out_txt.write(img_path+'\n')
            img = Image.open(img_path)
            width, height = img.size

            xcenter = (xmax + xmin)/2
            ycenter = (ymax + ymin)/2

            x = round(float(xcenter)/float(width), 6)
            y = round(float(ycenter)/float(height), 6)

            w = round(float(xmax-xmin)/float(width), 6)
            h = round(float(ymax-ymin)/float(height), 6)

            txt_path = img_path[0:-4] + '.txt'
            out = open(txt_path, 'w')

            clasa = data["samples"]['%d'%a]['annot']
            clasa = clasa.encode('utf8')
            
            if clasa == "bus small" or clasa == "trolleybus long":
                out.write(str(1) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
            elif clasa == "renault van":
                out.write(str(2) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
            else:
                out.write(str(0) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
            out.close()
            
            i=i+1
            c=c+1
            print c
        except Exception:
            i=0
            break
    a=a+1


