import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('/out/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

if len(img_array) == 0:
    print('there are no files provided, exiting...')
    quit()

out = cv2.VideoWriter('/app/project.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 24, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()