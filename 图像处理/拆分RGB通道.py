# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/2 22:36

import cv2
import random
import matplotlib.pyplot as plt
import numpy as np


def change_channels(img):
    '''使用opencv-python改变图像通道数'''
    # 分离原来图像的通道
    b,g,r = cv2.split(img)
    #随机打乱顺序
    # channel_list = [r, g, b]
    # random.shuffle(channel_list)
    # 合并通道
    new_image = cv2.merge([r,g,b])

    return new_image
def test():
    img = cv2.imread('./test.jpg')
    channels = cv2.split(img)
    cv2.imshow("img0", channels[0])
    cv2.waitKey()
    cv2.imshow("img1", channels[1])
    cv2.waitKey()
    cv2.imshow("img2", channels[2])
    cv2.waitKey()
    new_img0 = np.zeros(img.shape, dtype='uint8')
    new_img0[:, :, 0] = channels[0]
    cv2.imshow("img0", new_img0)
    cv2.waitKey()

    new_img1 = np.zeros(img.shape, dtype='uint8')
    new_img1[:, :, 1] = channels[1]
    cv2.imshow("img1", new_img1)
    cv2.waitKey()

    new_img2 = np.zeros(img.shape, dtype='uint8')
    new_img2[:, :, 2] = channels[2]
    cv2.imshow("img2", new_img2)
    cv2.waitKey()
if __name__ == '__main__':
    # image = cv2.imread('./test.jpg')
    # # 调用改变通道函数
    # new_image = change_channels(image)
    # # 将新的图片写在本地
    # # cv2.imwrite('new_image6.jpg', new_image)
    #
    # # 也可以在窗口查看效果
    # plt.subplot(121), plt.imshow(image), plt.title('Input')
    # plt.subplot(122), plt.imshow(new_image), plt.title('Output')
    # plt.show()
    test()
