#get only 6 classes from coco dataset
import os
from os import listdir, getcwd
from os.path import join

lines = open('test_dwg_ube.txt').read().splitlines()
save_file = open('test_dwg_ube_6classes.txt', 'w')
i = 0

classes = [0, 1, 2, 3, 5, 7, 80, 82]

num_lines = sum(1 for line in lines)
while(num_lines):
    num_lines = num_lines-1
    #print num_lines
    line = lines[i]
    lines2 = open(line[0:-4]+'.txt').read().splitlines()
    num_lines2 = sum(1 for line2 in lines2)
    j = 0
    out = open(line[0:-4]+'.6classes', 'w')
    while(num_lines2):
        num_lines2 = num_lines2 - 1
        line2 = lines2[j]
        data = line2.split(' ')
        if int(data[0]) in classes:
            if int(data[0]) == 3:
                data[0] = 1
            elif int(data[0]) == 5:
                data[0] = 3
            elif int(data[0]) == 7:
                data[0] = 4
            elif int(data[0]) == 80:
                data[0] = 5
            elif int(data[0]) == 82:
                data[0] = 2
            out.write(str(data[0])+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+'\n')
            
 
        
        j = j +1
    out.close()   
    if os.path.getsize(line[0:-4]+'.6classes') == 0:
         os.remove(line[0:-4]+'.6classes')
    else:
        save_file.write(line+'\n')
    i = i +1
save_file.close()
