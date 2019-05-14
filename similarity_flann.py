import cv2
import os
import numpy as np
from os import walk
from os.path import join


#处理.jpg格式图片
def create_descriptors1(folder1):
    files = []
    for (dirpath1, dirnames1, filenames1) in walk(folder1):
        files.extend(filenames1)
    for f in files:
        if '.jpg' in f:
            save_descriptor1(folder1, f, cv2.xfeatures2d.SIFT_create())

#读取.jpg格式图片数据
def save_descriptor1(folder1, image_path1, feature_detector1):
    # 判断图片是否为npy格式
    if image_path1.endswith("npy"):
        return
    # 读取图片并检查特征
    img = cv2.imread(join(folder1, image_path1), 0)
    keypoints1, descriptors1 = feature_detector1.detectAndCompute(img, None)

    # 设置文件名并将特征数据保存到npy文件
    descriptor_file = image_path1.replace("jpg", "npy")
    np.save(join(folder1, descriptor_file), descriptors1)

#处理.png格式图片
def create_descriptors2(folder2):
    files = []
    for (dirpath2, dirnames2, filenames2) in walk(folder2):
        files.extend(filenames2)
    for f in files:
        if '.png' in f:
            save_descriptor1(folder2, f, cv2.xfeatures2d.SIFT_create())

#读取图片数据
def save_descriptor2(folder2, image_path2, feature_detector2):
    # 判断图片是否为npy格式
    if image_path2.endswith("npy"):
        return
    # 读取图片并检查特征
    img = cv2.imread(join(folder2, image_path2), 0)
    keypoints2, descriptors2 = feature_detector2.detectAndCompute(img, None)
    # 设置文件名并将特征数据保存到npy文件
    descriptor_file = image_path2.replace("png", "npy")
    np.save(join(folder2, descriptor_file), descriptors2)


def run_program(event):
    # str = input('your photo name:')#得是带图片格式的那种
    # std=input('your standard:')
    str=file_name_2.GetValue()
    std=button_4.GetLabelText()
    path='F:/python/codes/gamma-AI/ph/'
    cut1 = str.split('.')
    cut1 = cut1[0]
# your_photo_path = 'F:/python/codes/gamma-AI/ph(new)/'+str

    your_photo_path=path+str
    query = cv2.imread(your_photo_path, 0)
    sift = cv2.xfeatures2d.SIFT_create()
    query_kp, query_ds = sift.detectAndCompute(query, None)

# folder = 'F:/python/codes/gamma-AI/ph(new)/'
#     folder='F:/ph/'
    folder=path
    descriptors = []
# 获取特征数据文件名
    for (dirpath, dirnames, filenames) in walk(folder):
        for f in filenames:
            if f.endswith("npy") and f != cut1[0] + ".npy":
                descriptors.append(f)
                x = descriptors
            #print(descriptors[198])
        for desc in range(len(descriptors)):
            strr = ''.join(descriptors[desc])
            cut2 = strr.split('.')
            cut2 = cut2[0]
            st = folder + strr
            if(cut1 == cut2):
                index_params = dict(algorithm=0, trees=5)
                search_params = dict(checks=50)
                flann = cv2.FlannBasedMatcher(index_params, search_params)

                potential_culprits = {}
                for d in descriptors:
                        # 将图像query与特征数据文件的数据进行匹配
                    matches = flann.knnMatch(np.load(st), np.load(join(folder, d)), k=2)
        # 清除错误匹配
                    good = []
                    for m, n in matches:
                        if m.distance < 0.7 * n.distance:
                            good.append(m)
        # 输出每张图片与目标图片的匹配数目
                    potential_culprits[d] = len(good)

        # 获取最多匹配数目的图片
                max_matches =max(potential_culprits.values())
                potential_suspect = None
                if std == 'moderately':
                    for culprit, matches in potential_culprits.items():
                        matching_ratio = matches / max_matches#if matches > max_matches:
                        if matching_ratio > 0.1 and matching_ratio < 0.5:
                            potential_suspect = culprit
                            print("%s,matching ratio:%d%%" % (potential_suspect.replace("npy", "jpg").upper(), matching_ratio * 100))

                if std == 'highly':
                    for culprit, matches in potential_culprits.items():
                        matching_ratio = matches / max_matches
                        if matching_ratio > 0.5:
                            potential_suspect=culprit
                            print("%s,matching ratio:%d%%" % (potential_suspect.replace("npy", "jpg").upper(),matching_ratio*100))
                if std == 'all':
                    for culprit, matches in potential_culprits.items():
                        matching_ratio = matches / max_matches
                        if matching_ratio > 0.1:
                            potential_suspect=culprit
                            print("%s,matching ratio:%d%%" % (potential_suspect.replace("npy", "jpg").upper(), matching_ratio * 100))





def creat_npy(event):
    path='F:/python/codes/gamma-AI/ph/'
    files = []
    for (dirpath1, dirnames1, filenames1) in walk(path):
        files.extend(filenames1)
    for f in files:
        if '.jpg' or '.png' in f:
            img = cv2.imread(join(path, f), 0)
            keypoints1, descriptors1 = cv2.xfeatures2d.SIFT_create().detectAndCompute(img, None)
            # 设置文件名并将特征数据保存到npy文件
            descriptor_file = f.replace("jpg", "npy")
            descriptor_file = f.replace("png", "npy")
            np.save(join(path, descriptor_file), descriptors1)
