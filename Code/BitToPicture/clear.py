import array
import numpy
import os
import scipy.misc
from PIL import Image
import glob
import cv2
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


path_file=glob.glob('/home/wxy/analyses/Hades/*') #获取当前文件夹下个数
path_number=len(path_file)
print(path_number)

for i in range(path_number):
    filename = path_file[i]+'/reports/report.json'
    graphname = path_file[i]+'/reports/'+ str(i) + '.json'
    os.rename(filename, graphname)
