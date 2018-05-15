#separate dataset by classes
import os
from os import listdir, getcwd
from os.path import join

lines = open('obj_detector_6classes.txt').read().splitlines()
save_file1 = open('only_person_class.txt', 'w')
save_file2 = open('only_cyclist_class.txt', 'w')
save_file3 = open('only_car_class.txt', 'w')
save_file4 = open('only_bus_class.txt', 'w')
save_file5 = open('only_truck_class.txt', 'w')
save_file6 = open('only_van_class.txt', 'w')
i = 0

num_lines = sum(1 for line in lines)
while(num_lines):
    num_lines = num_lines-1
    print num_lines
    line = lines[i]
    lines2 = open(line[0:-4]+'.6classes').read().splitlines()
    num_lines2 = sum(1 for line2 in lines2)
    if num_lines2 == 1:
        line2 = lines2[0]
        data = line2.split(' ')
        #save class
        if int(data[0]) == 0:
            save_file1.write(line+'\n')
        if int(data[0]) == 1:
            save_file2.write(line+'\n')
        if int(data[0]) == 2:
            save_file3.write(line+'\n')
        if int(data[0]) == 3:
            save_file4.write(line+'\n')
        if int(data[0]) == 4:
            save_file5.write(line+'\n')
        if int(data[0]) == 5:
            save_file6.write(line+'\n')
    i = i +1
save_file1.close()
save_file2.close()
save_file3.close()
save_file4.close()
save_file5.close()
save_file6.close()
