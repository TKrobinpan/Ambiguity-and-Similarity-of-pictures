import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf
from itertools import chain


def aHash(img):
    hash_str=[]
    #缩放为8*8
    img=cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
    #转换为灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #s为像素和初值为0，hash_str为hash值初值为''
    s=0

    #遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s=s+gray[i,j]
    #求平均灰度
    avg=s/64
    #灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str.append(1)
            else:
                hash_str.append(0)
    return hash_str

def hanming(inA,inB):
    b=0
    for i in range(len(inA)):
        if inA[i]!=inB[i]:
            b+=1
    return b

# 获取上级目录
# image_dirs='F:/python/codes/gamma-AI/similarity'
# 获取当前目录下所有文件
image_dirs='F:/ph'
image_paths=glob.glob(image_dirs+'/*.jpg')
x=input('similar image:')
similar_url=image_dirs+'/'+x
image2=cv2.imread(similar_url)
diff2=aHash(image2)

for i in range(len(image_paths)):
    image1=cv2.imread(image_paths[i])
    diff1=aHash(image1)
    distance=hanming(diff1,diff2)
    if distance<=10:
        print('distance:%d,name:%s'%(distance,image_paths[i]))
# print(diff1)