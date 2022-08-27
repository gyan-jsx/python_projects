from importlib.resources import path
from itertools import count
import cv2;
import random;
import os;

path = "../Frames"

images=[]

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    print(file)
    if ext in ['.gif', '.jpg', '.jpeg', '.png', '.jfif']:
        file_name = path+'/'+file
        print(file_name)
        images.append(file_name)
    count = len(images)
    print(count)