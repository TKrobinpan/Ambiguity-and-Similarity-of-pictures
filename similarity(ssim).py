from skimage.measure import compare_ssim
import cv2
import numpy as np
import glob

img_input=input('similar image:')
img_url='F:\python\codes\gamma-AI\similarity'
img_paths=glob.glob(img_url+'/*')
img2 = cv2.imread(img_url+'\\'+img_input)
# img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
for i in range(len(img_paths)):
    img1 = cv2.imread(img_paths[i])
    # img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2 = cv2.resize(img2, (img1.shape[0],img1.shape[1],img1.shape[2]))
    ssim = compare_ssim(img1, img2, multichannel=False)
    # if ssim>=0.6:
    print('ssim:%.2f,name:%s' % (ssim,img_paths[i]))




# print(img2.shape)
# print(img1.shape)


