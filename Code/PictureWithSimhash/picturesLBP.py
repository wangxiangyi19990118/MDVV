from skimage.feature import local_binary_pattern
import cv2
import glob

# settings for LBP
radius = 3 #3×3的图像块
n_points = 8 * radius #中心图像周围8图像

def getLBP(path):
    path_file = glob.glob(path+'/*.png')  # 获取当前文件夹下个数
    path_number = len(path_file)
    print(path_number)

    for i in range(path_number):
        print(path_file[i])
        image = cv2.imread(path_file[i])
        graphname = path_file[i]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#转化为灰度图像
        lbp = local_binary_pattern(image, n_points, radius)#进行LBP特征提取
        cv2.imwrite(graphname, lbp)
        print(graphname)
        cv2.waitKey(0)