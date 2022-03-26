# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/23 19:27
import numpy as np
import face_recognition as fr
#人脸识别
import cv2
#人脸识别
import os
#系统接口
def get_features():
    ld = 'pic/pics/'
    ldr = '图片库/特征库/'
    dr = os.listdir(ld)
    num = len(dr)
    i = 0
    for file in range(num):
        filename = ld+str(file+1)+'.jpg'
        image = cv2.imread(filename)
        f = fr.face_encodings(image,known_face_locations=None)
        if i<9:
            ff = open(ldr+'0'+str(i+1)+'.txt','w')
        else:
            ff = open(ldr+str(i+1)+'.txt', 'w')
        print(str(file+1)+'.jpg')
        ff.write(str(list(f[0])))
        ff.close()
        i += 1
# get_features()
def get_feature(img,location):
    ft = fr.face_encodings(img,known_face_locations=location)
    if not ft:
        return False
    return list(ft[0])
#提取图片的特征向量并写入特征库