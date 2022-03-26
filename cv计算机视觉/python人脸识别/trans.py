# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/23 19:36
import face_recognition as fr
import cv2

imgpath = "img/zy.png"
image = cv2.imread(imgpath)
f = fr.face_encodings(image, known_face_locations=None)
ft = open("图片库/特征库/1.txt", "w")
ft.write(str(list(f[0])))
ft.close()