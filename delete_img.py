import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
      

wd = getcwd()
for filename in os.listdir(wd+"\DETRAC-Train-Annotations-XML"):
    if not filename.endswith('.xml'): continue
    count = 1
    for files in os.listdir('DETRAC-train-data/Insight-MVT_Annotation_Train/%s'%(filename[0:-4])):
        if not files.endswith('.jpg'): continue
        if not(os.path.isfile('DETRAC-train-data/Insight-MVT_Annotation_Train/%s/img%05d.jpg'%(filename[0:-4], count)) and os.path.isfile('DETRAC-train-data/Insight-MVT_Annotation_Train/%s/img%05d.txt'%(filename[0:-4], count))):
            os.remove('DETRAC-train-data/Insight-MVT_Annotation_Train/%s/img%05d.jpg'%(filename[0:-4], count))
        count += 1

    
