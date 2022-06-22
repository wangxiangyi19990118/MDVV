import os, string, shutil,re
from simhash import Simhash
import jieba
import cv2
import numpy as np
import array
import os



def draw(x,y,img):#根据横纵坐标，该点亮度调高16
    #print(x,y)
    #print(y)
    if(img[x,y]+16>=255):
        img[x, y] =255
    else:
        img[x,y]+=16

def show(graphname,img):#图片保存
    #cv2.imshow('img',img)
    cv2.imwrite(graphname, img)
    print(graphname)
    cv2.waitKey(0)

def get_features(s):
    width = 8
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

def sim(st,img):#结巴分词，dict是自己做的字典，直接调用simhash库
    if(st!=''):
        #print(st)
        #jieba.load_userdict("./dict.txt")
        a =jieba.cut(st,cut_all=True,HMM=False)
        #print(a)
        #print(chardet.detect(st))
        #en=chardet.detect(st)
        st = st.decode('utf-8', 'ignore')
        #st=str(st, encoding = str(en))
        s=get_features(st)
        #print(s)
        #print(jieba.lcut(st))
        b=hex(Simhash(a).value)
        b=b[2:18]
        #print(b)
        c=''
        for i in range(len(b)):#simhash值切割为2个8进制数，如不够16位数则末位0补齐
            if(b[i]>'7'):
                c+='1'
            else:
                c+='0'
        if(len(b)<16):
                c+='0'
        #print(c)
        if(len(c)==16):
            d=int(c[0:8],2)
            e=int(c[8:16],2)
            #print(d,e)
            draw(d,e,img)


def is_number(s): #判断是否是纯数字
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def getPicture(filename,graphname):#输入是反汇编后的.text文件操作码，输出为新的图片
    #filename='G:/mm/F/2F.mm'
    img = np.ones((256, 256), dtype=np.uint8)#新图片固定长宽，默认是全黑图像
    str=''
    f = open(filename, 'rb')  # 读入文件
    ln = os.path.getsize(filename)  # 文件长度（byte）
    width = 1024  # 固定每次读取byte
    rem = ln % width  # 计算余出的字节
    a = array.array("B")  # uint8 数组
   # print(ln,filename)
    #print(int(ln/width))
    #f.seek(0, 2)
    #print(f.tell())
    #f.seek(f.seek(0, 2) - 10240 * 1025, 0)
    #print(f.tell())
    leaaa=int(ln/2)
    #print(leaaa)
    for b in range(1024*10):
       # print(b)
        f.seek(width*b,0)
       # print(f.tell())
        str=f.read(width)#每次读取的串
        sim(str,img) #串映射到图片上
    show(graphname,img)
    f.close()