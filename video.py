import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('/out/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('/app/project.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()