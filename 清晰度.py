import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf

# 获取上级目录
image_dirs='F:\python\codes\gamma-AI\\pictures for assessment'

# 获取当前目录下所有文件
image_paths=glob.glob(image_dirs+'\*')

# 给定阈值范围
threshold=300
for image_path in image_paths:
    image=cv2.imread(image_path)
    # height,width,_=image.shape
    # if height>=500 & width>=500:
    # image1=cv2.resize(image,(100,100))
    # elif height>=500 & width<500:
    #     image1=cv2.resize(image,(500,width))
    # elif height<500 & width>=500:
    #     image1=cv2.resize(image,(height,500))
    # else: image1=cv2.resize(image,(height,width))
#     # 将图像转为灰度图像
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     # 拉普拉斯mask模糊度判断
    fm=cv2.Laplacian(gray,cv2.CV_64F).var()
    text='high'

    if fm <= threshold:
        text='blurry'
#     # 图片上标注文字
    if 1000>=fm>threshold:
        text='normal'
    cv2.putText(image,'{}:{:.2f}'.format(text,fm),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3)
    # cv2.namedWindow('Image',0)
    cv2.imshow(image_path,image)
    key=cv2.waitKey(0)
