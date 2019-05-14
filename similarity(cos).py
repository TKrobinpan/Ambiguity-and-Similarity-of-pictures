# import cv2
# from numpy import average, linalg, dot
# import numpy as np
#
# def get_thumbnail(image_url, size=(1200, 750)):
#     image=cv2.imread(image_url)
#     image = cv2.resize(image,size)
#     image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     return image
#
#
# def image_similarity_vectors_via_numpy(image1, image2):
#     image1 = get_thumbnail(image1)
#     image2 = get_thumbnail(image2)
#     images = [image1, image2]
#     vectors = []
#     norms = []
#     for image in images:
#         vector = []
#         for pixel_tuple in image.():
#             vector.append(average(pixel_tuple))
#             vectors.append(vector)
#             norms.append(linalg.norm(vector, 2))
#         a, b = vectors
#         a_norm, b_norm = norms
#         res = dot(a / a_norm, b / b_norm)
#         return res
#
# img_url='F:\python\codes\gamma-AI\similarity'
# image1 = img_url+'\\'+'001.jpg'
# image2 = img_url+'\\'+'002.jpg'
# cosin = image_similarity_vectors_via_numpy(image1, image2)
#
#
# print(cosin)

from PIL import Image
from numpy import average, linalg, dot
import glob
import os
# os.environ['CUDA_VISIBLE_DEVICES']='2,3'

def get_thumbnail(image, size=(1200, 750), greyscale=False):
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        image = image.convert('L')
    return image


def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thumbnail(image1)
    image2 = get_thumbnail(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    res = dot(a / a_norm, b / b_norm)
    return res
img_input=input('similar image:')
img_url='F:\python\codes\gamma-AI\similarity'
img_paths=glob.glob(img_url+'/*')
# image1 = img_url+'\\'+'001.jpg'
# image2 = img_url+'\\'+'002.jpg'
image1 = Image.open(img_url+'\\'+img_input)
for i in range(len(img_paths)):
    image2 = Image.open(img_paths[i])
    cosin = image_similarity_vectors_via_numpy(image1, image2)
    if cosin>60:
        print(cosin)
