import glob
import os,sys

from Include.PictureWithSimhash.opSimhash import getPicture


def getSimhash(path):
    print(path)
    path_file=glob.glob(path+'/*.mm')
    print(path_file)
    path_number=len(path_file)
    print(path_number)

    for i in range(path_number): #针对每一个提取出的text文件，进行simhash图片，并保存到文件夹中
        filename = path_file[i]
        print(filename)
        graphname = './dataset' +'/'+str(i+1) + '.png'
        getPicture(filename,graphname)

    return path_number