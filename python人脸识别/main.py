# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/23 19:24
# -*- coding: utf-8 -*-
from tkinter.messagebox import *
# python弹窗
from tkinter import *
# gui编程
import numpy as np
from PIL import Image, ImageTk, ImageDraw, ImageFont
# 图像处理库
import os
# 多种操作系统接口
import win32ui
# 创建菜单，打开文件
import cv2
# 图像处理
import dlib
# 人脸识别模块
from pywin.framework.editor import frame

import face_feature
# 人脸特征点定位
import shibie
import _thread
import time
import face_recognition as fr

p = None
name = None
times = 1


# X = tf.placeholder(tf.float32, [1, 57*47])
# conv = test.convolution(X)
# saver = tf.compat.v1.train.Saver()
# session = tf.Session()
# saver.restore(session, './mod/best.ckpt')
# frame=Tk()
def createForm():  # 登录面板

    Button(frame, text='登陆', command=lambda: start(1)).grid(column=1)
    # Button(label, text='退出', command=_quit).grid(row=3, column=1, stick=E)


def do1():
    print("hello")


def loginCheck():  # 登录检测
    if name == 'zhouyi':
        frame.destroy()  # 销毁页面
        root.title("人脸识别")
        createWidgets()


def createWidgets():
    menu_bar = Menu(root)
    root.config(menu=menu_bar)
    file_menu1 = Menu(menu_bar)
    file_menu1.add_command(label="已录入", command=open_photos)
    file_menu1.add_separator()
    file_menu1.add_command(label="退出", command=_quit)
    file_menu2 = Menu(menu_bar)
    file_menu2.add_command(label="开始检测", command=start)
    file_menu2.add_command(label="停止检测", command=stop)
    file_menu2.add_command(label="录入人像", command=add)
    menu_bar.add_cascade(label="文件", menu=file_menu1)
    menu_bar.add_cascade(label="运行", menu=file_menu2)


def _quit():  # 退出
    root.quit()
    root.destroy()
    exit()


def start(mod=0):  # 开始检测
    if not camera.isOpened():
        camera.open(0)

    panel.pack()
    # print(mod)
    video_loop(mod)


def stop():  # 关闭人脸识别
    if camera.isOpened():
        camera.release()
        cv2.destroyAllWindows()
        panel.pack_forget()


def add():  # 录取人脸特征
    cap = cv2.VideoCapture(0)  # 创建内置摄像头变量
    while cap.isOpened():  # 如果摄像头打开
        try:
            ret, img = cap.read()
            if ret == True:
                cv2.imshow("Image", img)
                k = cv2.waitKey(100)  # 每0.1秒读一次键盘
                if k == ord("z") or k == ord("Z"):  # 如果输入z
                    imgSave = img
                    dlog = win32ui.CreateFileDialog(0)
                    dlog.DoModal()
                    filename = dlog.GetPathName().split("\\")[-1]
                    if '.' not in filename:
                        filename = filename + '.jpg'
                        cv2.imwrite('photos/' + filename, imgSave)
                        cap.release()
                        imgpath = 'photos/' + filename
                        image = cv2.imread(imgpath)
                        f = fr.face_encodings(image, known_face_locations=None)
                        with open('xuehao.txt', 'r') as fp:
                            lines = len(fp.readlines())
                            fp.close()
                        ft = open("图片库/特征库/" + str(lines + 1) + ".txt", "w")
                        ft.write(str(list(f[0])))
                        ft.close()
                        fc = open("xuehao.txt", "a+")
                        mz = input("请输入你的名字\n")
                        fc.write(str(lines + 1) + " " + mz + "\n")
                        fc.close()
        except:
            print("错误")
            continue


def open_photos():  # 打开照片
    dlog = win32ui.CreateFileDialog(1)
    dlog.SetOFNInitialDir(path + '.\\photos')
    dlog.DoModal()
    filename = dlog.GetPathName()


def video_loop(mod=0):  # 摄像头人脸检测
    # print(mod)
    # global img
    # global X
    # global conv
    # global session
    # global name, p
    global names
    global times
    success, img = camera.read()  # 从摄像头读取照片

    if success:  # 如果成功读取到人脸
        faces = detector(img)  # 框出人脸
        # print(faces)
        times += 1  # 时间加一
        i = 0
        if times % 20 == 0:
            names = []  # 创建names列表
        # imgWrite = img
        for d in faces:
            # 使用opencv在原图上画出人脸位置
            left_top = (dlib.rectangle.left(d), dlib.rectangle.top(d))
            right_bottom = (dlib.rectangle.right(d), dlib.rectangle.bottom(d))
            # if mod!=1:
            imgWrite = cv2.rectangle(img, left_top, right_bottom, (0, 255, 0), 2, cv2.LINE_AA)

            location = [0, 0, 0, 0]
            location[0], location[1] = left_top[1], right_bottom[0]
            location[2], location[3] = right_bottom[1], left_top[0]
            location = tuple(location)

            loc = []
            loc.append(location)
            if times % 20 == 0:
                p = face_feature.get_feature(img, loc)
                name = shibie.shibie(p)
                print(name)
                if mod == 1 and name == "zhouyi":
                    # frame.destroy()
                    # print(1111)
                    root.title("人脸识别")
                    camera.release()
                    panel.pack_forget()
                    # imgWrite = img

                    showinfo("", "登录成功！")
                    return createWidgets()  # 功能面板
                names.append(name)

            # t = _thread.start_new_thread(getname,(img,loc))

            if names and len(names) == len(faces) and mod == 0:  # 图像添加文字

                imgWrite = cv2.putText(imgWrite, names[i], left_top, font, 1.0, (0, 255, 0), 2, cv2.LINE_AA)

                # cv2image = cv2.cvtColor(imgWrite, cv2.COLOR_BGR2RGB)  # 转换颜色从BGR到RGB
                # imgWrite = Image.fromarray(cv2image)
                # print(type(imgWrite))
                # #PIL图片上打印汉字
                # draw = ImageDraw.Draw(imgWrite)
                # draw.text((left_top[0], left_top[1]-20), names[i], (255, 0, 0), font=font1)
                # print(type(imgWrite))
                # print(names[i])
                # imgtk = ImageTk.PhotoImage(image=imgWrite)
                # panel.imgtk = imgtk
                # panel.config(image=imgtk)
            i += 1
        if not faces:
            imgWrite = img
            # cv2image = cv2.cvtColor(imgWrite, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
            # imgWrite = Image.fromarray(cv2image)  # 将图像转换成Image对象
            # print(type(imgWrite),'-'*50)
            # imgtk = ImageTk.PhotoImage(image=img)
            # panel.imgtk = imgtk
            # panel.config(image=imgtk)

        # print(type(imgWrite),'-'*50)
        cv2image = cv2.cvtColor(imgWrite, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
        imgWrite = Image.fromarray(cv2image)  # 将图像转换成Image对象
        imgtk = ImageTk.PhotoImage(image=imgWrite)
        panel.imgtk = imgtk
        panel.config(image=imgtk)

        root.after(1, lambda: video_loop(mod))


names = []
root = Tk()
root.title("登录")
width = 600
height = 400
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)  # 居中对齐

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")
camera = cv2.VideoCapture(0)  # 摄像头
camera.release()
path = os.getcwd()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + \
                                     'haarcascade_frontalface_default.xml')

# 使用特征提取器detector
detector = dlib.get_frontal_face_detector()
username = StringVar()
password = StringVar()
# frame = Frame(root, width=600, height=400)
# frame.pack()
panel = Label(root)  # initialize image panel
panel.pack()
start(1)
root.mainloop()