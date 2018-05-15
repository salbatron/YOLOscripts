#count number of every class in training dataset
lines = open('E:\\WORK\\builds\\git\\darknet_win\\build\\darknet\\x64\\data\\dwg_ube\\dev_dwg_ube.txt').read().splitlines()
i = 0
count = [0]*6

num_lines = sum(1 for line in lines)
while(num_lines):
    num_lines = num_lines-1
    print num_lines
    line = lines[i]
    lines2 = open(line[0:-4]+'.6classes').read().splitlines()
    num_lines2 = sum(1 for line2 in lines2)
    j = 0
    while(num_lines2):
        num_lines2 = num_lines2 - 1
        line2 = lines2[j]
        data = line2.split(' ')
        count[int(data[0])] = count[int(data[0])] + 1
        j = j +1
    i = i +1
lines3 = open('E:\\WORK\\builds\\git\\darknet_win\\build\\darknet\\x64\\data\\6classes.names').read().splitlines()
k = 0
for line3 in lines3:
    print line3+':'+str(count[k])+'\n'
    k = k + 1

