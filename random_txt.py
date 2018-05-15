#randomize training list
import random
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

lines = open('test_dwg_ube_6classes.txt').read().splitlines()
i = 1
out = open('test_dwg_ube_6classes_rand.txt', 'w')
num_lines = sum(1 for line in lines)
while(lines):
    num_lines = num_lines-1
    print num_lines
    myline =random.choice(lines)
    lines.remove(myline)
    out.write(myline+'\n')
out.close()

