import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image
import xml.dom.minidom

wd = getcwd()

names = open(wd+'\\all.names')
line_names = names.readlines()


for filename in os.listdir(wd):
    if not filename.endswith('.txt'): continue
    img_name = filename[0:-4]+'.bmp'
    print img_name
    img = Image.open(img_name)
    width, height = img.size
    img.close()
    with open(filename) as f:
        lines = f.readlines()
        num_lines = sum(1 for line in lines)
        print num_lines
        
        #xml write
        root = ET.Element("annotation", verified="no")
        folder=ET.SubElement(root, "folder").text = os.path.basename(wd)
        filename=ET.SubElement(root, "filename").text = filename[0:-4]+'.bmp'
        path=ET.SubElement(root, "path").text = wd
        source=ET.SubElement(root, "source")
        database=ET.SubElement(source, "database").text = "Unknown"
        size=ET.SubElement(root, "size")
        width=ET.SubElement(size, "width").text = str(width)
        eight=ET.SubElement(size, "height").text = str(height)
        depth=ET.SubElement(size, "depth").text = "3"
        segmented=ET.SubElement(root, "segmented").text = "0"
        i = 0
        while(num_lines):
            line = lines[i]
            data = line.split(' ')

            label = line_names[int(data[0])]

            x_center = float(width)*float(data[1])
            y_center = float(height)*float(data[2])
            w = float(width)*float(data[3])
            h = float(height)*float(data[4])
            x1 = x_center - w/2
            y1 = y_center - h/2
            x2 = x_center + w/2
            y2 = y_center + h/2

            x1 = round(x1,0)
            y1 = round(y1,0)
            x2 = round(x2,0)
            y2 = round(y2,0)
            
             
            object1=ET.SubElement(root, "object")
            name=ET.SubElement(object1, "name").text = label[0:-1]
            pose=ET.SubElement(object1, "pose").text = "Unspecified"
            truncated=ET.SubElement(object1, "truncated").text = "0"
            difficult=ET.SubElement(object1, "difficult").text = "0"
            overlap=ET.SubElement(object1, "overlap").text = "0"
            bndbox=ET.SubElement(object1, "bndbox")
            xmin=ET.SubElement(bndbox, "xmin").text = str(int(x1))
            ymin=ET.SubElement(bndbox, "ymin").text = str(int(y1))
            xmax=ET.SubElement(bndbox, "xmax").text = str(int(x2))
            ymax=ET.SubElement(bndbox, "ymax").text = str(int(y2))
            num_lines = num_lines - 1
            i = i + 1
    tree = ET.ElementTree(root)
    xml_name = filename[0:-4]+'.xml'
    tree.write(xml_name, xml_declaration=True, encoding='utf-8')   
    f.close()


             
             
