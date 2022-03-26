# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/26 21:09
"""定义：图像的二值化，就是将图像上的像素点的灰度值设置为0或255，也就是将整个图像呈现出明显的只有黑和白的视觉效果。
一幅图像包括目标物体、背景还有噪声，要想从多值的数字图像中直接提取出目标物体，常用的方法就是设定一个阈值T，
用T将图像的数据分成两部分：大于T的像素群和小于T的像素群。这是研究灰度变换的最特殊的方法，称为图像的二值化（Binarization）。"""
# https://blog.csdn.net/what_lei/article/details/49159655#
import cv2
import numpy as np
from matplotlib import pyplot as plt
# img=cv2.imread('IMG_0502.png')#读取图片
# GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#将图像从一个颜色空间转换为另一个颜色空间。
# ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)#设定阈值，高于阈值的图像赋予新值
# """第一个参数       src            指原图像，原图像应该是灰度图。
# 第二个参数         x              指用来对像素值进行分类的阈值。
# 第三个参数         y              指当像素值高于（有时是小于）阈值时应该被赋予的新的像素值
# 第四个参数     Methods     指，不同的不同的阈值方法，这些方法包括："""
# ret,thresh2=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3=cv2.threshold(GrayImage,127,255,cv2.THRESH_TRUNC)
# ret,thresh4=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO)
# ret,thresh5=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO_INV)
# titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
# plt.show()
######################################################################################
#自适应阈值
img = cv2.imread('IMG_0502.png')
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 中值滤波
GrayImage= cv2.medianBlur(GrayImage,5)
ret,th1 = cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
#3 为Block size, 5为param1值
th2 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                    cv2.THRESH_BINARY,3,5)
# cv2.adaptiveThreshold（）
# 函数：第一个参数src
# 指原图像，原图像应该是灰度图。
# 第二个参数x
# 指当像素值高于（有时是小于）阈值时应该被赋予的新的像素值
# 第三个参数adaptive_method指： CV_ADAPTIVE_THRESH_MEAN_C或CV_ADAPTIVE_THRESH_GAUSSIAN_C
# 第四个参数threshold_typ指取阈值类型：必须是下者之一CV_THRESH_BINARY_INV
# 第五个参数 block_size指用来计算阈值的象素邻域大小: 3, 5, 7, ...
# 第六个参数param1 指与方法有关的参数。对方法CV_ADAPTIVE_THRESH_MEAN_C和CV_ADAPTIVE_THRESH_GAUSSIAN_C， 它是一个从均值或加权均值提取的常数, 尽管它可以是负数。
th3 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv2.THRESH_BINARY,3,5)
titles = ['Gray Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [GrayImage, th1, th2, th3]
for i in range(4):
   plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()
