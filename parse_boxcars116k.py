import json
from pprint import pprint
from PIL import Image
import unicodedata
from decimal import Decimal

data = json.load(open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\BOXCARS\\BoxCars116k\\json_data\\dataset.json'))
out_txt = open('Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\BOXCARS\\BoxCars116k\\json_data\\train.txt', 'w')
#starting position
a=0
#end position
b=21249
#intern counter
i=0
#counter
c=0
while c<=116289:
        
   while True:
       try:

           xmin = data["samples"][a]['instances'][i]["2DBB"][0]
           ymin = data["samples"][a]['instances'][i]["2DBB"][1]

           xmax = xmin + data["samples"][a]['instances'][i]["2DBB"][2]
           ymax = ymin + data["samples"][a]['instances'][i]["2DBB"][3]

           img_path = data["samples"][a]['instances'][i]["path"]
           img_path = img_path.replace("/", "\\")
           img_path = img_path.encode('utf8')
           img_path = 'Y:\\02_Deep_Learning_Data_Sets\\Vehicle_Detection_Classification\\BOXCARS\\BoxCars116k\\images\\' + img_path
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

           clasa = data["samples"][a]['annotation']
           clasa = clasa.encode('utf8')
           if clasa == "bus small" or clasa == "trolleybus long":
               out.write(str(1) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) +'\n')
           elif clasa == "van" or clasa == "ford transit van mk6" or clasa == "ford transit van mk7" or clasa == "opel vivaro van mk2" or clasa == "peugeot boxer van mk3" or clasa == "renault master van mk2" or clasa == "renault master van mk3" or clasa == "renault trafic van mk2" or clasa == "volkswagen transporter van mk4" or clasa == "volkswagen transporter van mk5" or clasa == "fiat ducato van" or clasa == "ford transit van" or clasa == "opel vivaro van" or clasa == "peugeot boxer van" or clasa == "renault master van" or clasa == "renault trafic van" or clasa == "volkswagen transporter van":
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




