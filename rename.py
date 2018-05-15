#rename classes in dataset
import glob
import os

for f in glob.glob('*.jpg'):
    if f[-13:] == 'big truck.jpg':
        new_filename = f[0:-13] + "truck.jpg"
        os.rename(f,new_filename)
