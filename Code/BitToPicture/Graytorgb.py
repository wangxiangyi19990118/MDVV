import array
import numpy
import os
import scipy.misc
from PIL import Image
import glob
import cv2
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


path_file=glob.glob('I:/IM/Locker/*') #获取当前文件夹下个数
path_number=len(path_file)
print(path_number)

for i in range(path_number):
    filename = path_file[i]
    print(filename,i)
    graphname = 'I:/IM/Locker/' + 'Locker'+str(i) + '.png'
    im_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
    cv2.imwrite(graphname,im_color)
