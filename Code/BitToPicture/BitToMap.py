import array
import numpy
import os
import scipy.misc
from PIL import Image
import glob
import cv2
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


path_file=glob.glob('E:/baidupan/green/*') #获取当前文件夹下个数
path_number=len(path_file)
print(path_number)

for i in range(path_number):
    filename = path_file[i]
    print(filename,i)
    graphname = 'I:/IM/green/green-' + str(i) + '.png'
    f = open(filename, 'rb')  # 读入文件
    ln = os.path.getsize(filename)  # 文件长度（byte）
    width = 32  # 固定图片宽度
    if ln>10*1024 and ln<30*1024:
        width=64
    if ln>30*1024 and ln<60*1024:
        width=128
    if ln>60*1024 and ln<100*1024:
        width=256
    if ln>100*1024 and ln<200*1024:
        width=384
    if ln>200*1024 and ln<500*1024:
        width=512
    if ln>500*1024 and ln<1000*1024:
        width=768
    if ln>1000*1024:
        width=1024
    print(width)

    rem = ln % width  # 计算余出的字节
    size=rem
    a = array.array("B")  # uint8 数组
    b = array.array("B")
    c = array.array("B")
#    print(length,filename)
   # print(int(ln/2))
   # left=int(ln/2)+size
   # f.seek(ln-1024*10240, 0)
    # print(f.tell())
    #str = f.read(1024*10240)
    #print(str)
    #a.fromfile(f, ln-rem-size)  # 将文件读入数组a中，舍去余出的字节
    #b.fromfile(f, int(ln-rem))
    #c=list(set(b).difference(set(a)))
    #a=str

#    pickle.dump(str, open('G:/picture/b/T/1.txt', 'wb'))
#    f.close()
 #   f1 = open('G:/picture/b/T/1.txt', 'rb')
 #   ln1=os.path.getsize('G:/picture/b/T/1.txt')
 #   rem1 = ln1 % width
    a.fromfile(f, ln-rem)
#    g = numpy.reshape(a, (int(ln/width), width))  # 将数组转为二维
    #b=numpy.array(buffer)
   # b=array.array("B")
    g=numpy.reshape(a,(int(len(a)/width),width))
    g = numpy.uint8(g)
#    resize_2 = tf.image.resize_images(g, (256, 512), method=2)
#    plt.imshow(g)
#    merged = mcolors.to_rgb()
    scipy.misc.imsave(graphname, g)  # 保存图片

    img = Image.open(graphname) # 读取的图像
    img_array=img.load()
#   print(img.size)
 #   plt.show()

'''
#graphname = 'f:/test/'+str(i)+'.jpg'
pe = pefile.PE("f:/test/1900.exe")
#print(filename)
ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint
addr = pe.get_memory_mapped_image()[ep:ep +200]
buffer = binascii.hexlify(addr)
print(buffer)

buffer=bin(int(buffer,base=16))

res=str(buffer)
print(res)
#res = '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'
b=numpy.array(res)
'''