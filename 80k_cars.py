import random
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

cls = "car"

lines = open('classifier_new.txt').read().splitlines()
i = 0
counter = 0
out = open('classifier_80k_cars.txt', 'w')
num_lines = sum(1 for line in lines)
while(num_lines):
    num_lines = num_lines-1
    print num_lines
    line = lines[i]
    img = Image.open(line)
    width, height = img.size
    if width > 32 and height > 32:
        a = line.rpartition('\\')[0];
        b = line.replace(a,'')
        if cls in b and counter < 81154:
            if width <= 608 and height <= 608:
                out.write(line+'\n')
                counter = counter + 1
        elif cls not in b:
            out.write(line+'\n')
    i = i + 1
    img.close()
out.close()

