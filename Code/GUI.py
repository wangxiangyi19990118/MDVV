import tkinter

from Include.PictureWithSimhash.harrLike import getHaar
from Include.PictureWithSimhash.hog import getHog
from Include.PictureWithSimhash.opPictures import getSimhash
from Include.PictureWithSimhash.picturesLBP import *
from Include.TrainAndTest.perdition import *
from Include.TrainAndTest.create_labels_files import *
from Include.TrainAndTest.create_tf_record import *


class FindLocation(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("恶意软件检测")
        self.lable = tkinter.Label(self.root, text="请选择图像特征提取方式").pack()
        # 创建一个输入框,并设置尺寸
        self.input = tkinter.Entry(self.root, width=50)
        self.input.insert(0, "请输入所检测文件所在目录：")
        self.method=1
        self.deeplearning=4
        self.v = tkinter.IntVar()
        self.v1 = tkinter.IntVar()
        # set函数是设置单选框中的初始值，set的参数和Radiobutton组件中的value比较，如果存在相同的情况，则为初始值
        self.v.set(0)
        self.v1.set(4)
        # 三个单选框中都有相同的回调函数callRadiobutton，点击单选框后调用callRadiobutton，重新设置三个单选框的数值
        tkinter.Radiobutton(self.root, variable=self.v, text="Orgin", value=0, command=self.set_method).pack()
        tkinter.Radiobutton(self.root, variable=self.v, text="LBP", value=1, command=self.set_method).pack()
        tkinter.Radiobutton(self.root, variable=self.v, text="HOG", value=2, command=self.set_method).pack()
        tkinter.Radiobutton(self.root, variable=self.v, text="Haar-like", value=3, command=self.set_method).pack()
        self.lable = tkinter.Label(self.root, text="请选择使用的深度学习模型").pack()
        tkinter.Radiobutton(self.root, variable=self.v1, text="Inception V3", value=4, command=self.set_method).pack()
        tkinter.Radiobutton(self.root, variable=self.v1, text="Inception V1", value=5, command=self.set_method).pack()


        # 创建一个回显列表
        self.display_info = tkinter.Listbox(self.root, width=50)

        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command=self.get_result, text="检测")


    # 完成布局
    def gui_arrang(self):
        self.input.pack()
        self.display_info.pack()
        self.result_button.pack()

    def set_method(self):# 确认特征提取方式
        self.method=self.v.get()
        print(self.method)

    def set_deeplearning(self):# 确认深度学习模型
        self.deeplearning=self.v1.get()
        print(self.deeplearning)

    #点击后开始执行
    def get_result(self):
        # 获取输入信息
        self.addr = self.input.get()
        self.number=getSimhash(self.addr)

        create_lable('./dataset')
        result=[]
        for i in range(self.number):

            result=0
            # 判断使用何种深度学习模型
            if self.deeplearning==4:
                # 判断使用何种特征提取方式
                if self.method==0:
                    create_lable('./dataset', i)
                    create_tf_record('./dataset')
                    result[i] = predict_Origin_V3()
                if self.method==1:
                    getLBP('./dataset')
                    create_lable('./dataset',i)
                    create_tf_record('./dataset')
                    result[i]=predict_LBP_V3()
                if self.method==2:
                    getHog('./dataset')
                    create_lable('./dataset', i)
                    create_tf_record('./dataset')
                    result[i]=predict_Hog_V3()
                if self.method==3:
                    getHaar('./dataset')
                    create_lable('./dataset', i)
                    create_tf_record('./dataset')
                    result[i]=predict_Harr_V3()
            # 判断使用何种深度学习模型
            if self.deeplearning==5:
                # 判断使用何种特征提取方式
                if self.method==0:
                    create_lable('./dataset', i)
                    create_tf_record('./dataset')
                    result[i] = predict_Origin_V1()
                if self.method==1:
                    getLBP('./dataset')
                    create_lable('./dataset',i)
                    create_tf_record('./dataset')
                    result[i]=predict_LBP_V1()
                if self.method==2:
                    getHog('./dataset')
                    create_lable('./dataset', i)
                    create_tf_record('./dataset')
                    result[i]=predict_Hog_V1()
                if self.method==3:
                    getHaar('./dataset')
                    create_lable('./dataset', i)
                    create_tf_record('./dataset')
                    result[i]=predict_Harr_V1()
        # 清空回显列表可见部分,类似clear命令
        for item in range(10):
            self.display_info.insert(0, "")
        # 为回显列表赋值
        for i in range(self.number):
            if result[i] == 0:
                self.display_info.insert(0, "Normal!")
            if result[i] == 1:
                self.display_info.insert(0, "Malware!")
        # 这里的返回值,没啥用,就是为了好看
        return result


def main():
    # 初始化对象
    FL = FindLocation()
    # 进行布局
    FL.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()
