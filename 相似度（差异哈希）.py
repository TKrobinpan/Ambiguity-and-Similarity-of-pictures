import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf

def dhash_feature(image_initial):
    # 将图片变为9*8的大小尺寸
    res_image=cv2.resize(image_initial,(9,8))
    # 将彩色图片灰度化
    gray=cv2.cvtColor(res_image,cv2.COLOR_BGR2GRAY)
    # 比较相邻像素
    difference=[]
    for row in range(8):
        for col in range(8):
            # 每个元素与之后一列的元素比较，用0，1记录大小
            if gray[row][col]>gray[row][col+1]:
                a=1
            else:a=0
            # 用列表生成01序列，便于后面计算汉明距离
            difference.append(a)
    return difference
# 汉明距离，一般小于5认为是同一张图片
def hanming(inA,inB):
    b=0
    for i in range(len(inA)):
        if inA[i]!=inB[i]:
            b+=1
    return b

# 获取上级目录
# image_dirs='F:/python/codes/gamma-AI/similarity'
image_dirs='F:/ph'
# 获取当前目录下所有文件
image_paths=glob.glob(image_dirs+'/*.jpg')
x=input('similar image:')
similar_url=image_dirs+'/'+x
image2=cv2.imread(similar_url)
diff2=dhash_feature(image2)

for i in range(len(image_paths)):
    image1=cv2.imread(image_paths[i])
    diff1=dhash_feature(image1)
    distance=hanming(diff1,diff2)
    if distance<=20:
        print('distance:%d,name:%s'%(distance,image_paths[i]))
        # image_recover=cv2.cvtColor(image2,cv2.COLOR_GRAY2BGR)
        # cv2.namedWindow('image1',0)
        # cv2.imshow('image1',image1)
        # cv2.waitKey(0)


