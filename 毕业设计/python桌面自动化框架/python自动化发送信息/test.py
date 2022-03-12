# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/11 20:54
# import win32gui
# import win32con
# import win32clipboard as w
# # https://blog.csdn.net/wjb123sw99/article/details/83475516
# # 发送的消息
# msg = "测试代码"
# # 窗口名字
# name = "不知"
# # 将测试消息复制到剪切板中
# w.OpenClipboard()
# w.EmptyClipboard()
# w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
# w.CloseClipboard()
# # 获取窗口句柄
# handle = win32gui.FindWindow("Tim", name)
# # while 1==1:
# if 1 == 1:
#     # 填充消息
#     win32gui.SendMessage(handle, 770, 0, 0)
#     # 回车发送消息
#     win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

# https: // www.cnblogs.com / TD1900 / p / 12468842.html
# import pyautogui as gui
# gui.hotkey('ctrl','alt','z')
# #模拟组合键 打开QQ快捷键
# for i in range(1,10):
#     gui.typewrite(message='!',)
#     gui.hotkey('ctrl','enter') #模拟组合键 发送消息


# from tkinter import *
# import win32gui
# import win32con
# import win32clipboard as w
# LOG_LINE_NUM = 0
# class Play():
#     def __init__(self, init_window_name):
#         self.init_window_name = init_window_name
#     def set_init_window(self):              #构建框架
#         self.init_window_name.title("qq消息发送器")
#         self.init_window_name.geometry("730x120+10+10")
#         self.init_window_name.attributes("-alpha", 1)  # 虚化 值越小虚化程度越高
#         # 标签
#         self.init_data_label = Label(self.init_window_name, text="输入要发送消息者")
#         self.init_data_label.grid(row=0, column=0)
#         self.name_data_label = Label(self.init_window_name, text="要发送内容")
#         self.name_data_label.grid(row=0, column=12)
#         self.log_label = Label(self.init_window_name, text="@ 2020版权所有       https://blog.51cto.com/982439641")
#         self.log_label.grid(row=12, column=0)
#     # 文本框
#         self.init_data_Text = Text(self.init_window_name, width=45, height=5)  # 原始数据录入框
#         self.init_data_Text.grid(row=1, column=0, rowspan=1, columnspan=1)
#         self.log_data_Text = Text(self.init_window_name, width=45, height=5)  # 日志框
#         self.log_data_Text.grid(row=1, column=8, columnspan=10)
#         self.str_command = Button(self.init_window_name, text="发送100次", bg="lightblue", width=10,
# command=self.Send)  # 调用内部方法  加()为直接调用
#         self.str_command.grid(row=1, column=6)
#     def Send(self):
#         for i in range(0,10):
#             a=self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
#             b = self.log_data_Text.get(1.0, END).strip().replace("\n", "").encode()
#             receiver=str(a,encoding="utf-8")
#             msg=str(b,encoding="utf-8")
# ###############################发送qq消息使用下面几行#########
#             w.OpenClipboard()
#             w.EmptyClipboard()
#             w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
#             w.CloseClipboard()
#             qq = win32gui.FindWindow(None, receiver)
#             win32gui.SendMessage(qq, win32con.WM_PASTE, 0, 0)
#             win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
# ###############################done#########################
# if __name__=="__main__":
#     init_window = Tk()
#     Play(init_window).set_init_window()
#     init_window.mainloop()
#
# import win32gui
# import win32con
# import win32clipboard as w
#
# class sendMsg():
#     def __init__(self,receiver,msg):
#         self.receiver=receiver
#         self.msg=msg
#         self.setText()
#     #设置剪贴版内容
#     def setText(self):
#         w.OpenClipboard()
#         w.EmptyClipboard()
#         w.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
#         w.CloseClipboard()
#     #发送消息
#     def sendmsg(self):
#         qq=win32gui.FindWindow(None,self.receiver)
#         win32gui.SendMessage(qq,win32con.WM_PASTE , 0, 0) #win32on 见site-packages\win32\lib\win32con.py,有的博文里出现的770对用的就是win32con.WM_PASTE
#         win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
#
#
# if __name__ == '__main__':
#     receiver='大兄弟'
#     msg="测试"
#     qq=sendMsg(receiver,msg)
#     qq.sendmsg()
import pprint
# 722416qq
import pyautogui as gui
import time
# a = gui.getAllWindows()
# print(2)
# print(pyautogui.getActiveWindowTitle())
# print(gui.getAllTitles())
# print(gui.getInfo())
# for a,b in zip(pyautogui.getAllTitles(),pyautogui.getAllWindows()):
#     print(a,b)
#     print("#"*30)
# print(len(pyautogui.getAllTitles()),len(pyautogui.getAllWindows()))
# getWindows获取所有活动窗体程序句柄对象的字典，key为窗体程序title，value为hwnd对象
# gui.Window(gui.getWindows().get('周刚')).set_foreground()
# print(gui.Window(395420).activate())
# print(gui.getActiveWindowTitle())
# for i in range(10):
#     gui.write("123")
#     gui.hotkey('ctrl', 'enter')
# gui.hscroll(1)
# gui.write("12")
# # Window使用hwnd对象创建window对象，对窗体程序进行控制
# # 这一部分在提供的官方api文档里并没有提到，这是作者故意没有提及的窗体程序句柄处理，才对win api封装了几个功能
# for i in range(10):
#  gui.typewrite(time.asctime()+' : '+str(i)) # typewrite可以参考文档，实际是模拟键盘输入，所以当这里的内容换成中文时，是无效的
#  gui.hotkey('ctrl','enter') # hotkey模拟组合键
#  time.sleep(10)



# import pyautogui
#
# pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
# pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
#
# # 判断(x,y)是否在屏幕上
# x, y = 122, 244
# pyautogui.onScreen(x, y)  # 结果为true
#
# width, height = pyautogui.size()  # 屏幕的宽度和高度
# print(width, height)


# import pyautogui
#
# currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
# print(currentMouseX, currentMouseY)
#
# # 控制鼠标移动,duration为持续时间
# for i in range(2):
#     pyautogui.moveTo(100, 100, duration=0.25)  # 移动到 (100,100)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)
#
# for i in range(2):
#     pyautogui.moveRel(50, 0, duration=0.25)  # 从当前位置右移100像素
#     pyautogui.moveRel(0, 50, duration=0.25)  # 向下
#     pyautogui.moveRel(-50, 0, duration=0.25)  # 向左
#     pyautogui.moveRel(0, -50, duration=0.25)  # 向上
#
# # 按住鼠标左键，把鼠标拖拽到(100, 200)位置
# pyautogui.dragTo(100, 200, button='left')
# # 按住鼠标左键，用2秒钟把鼠标拖拽到(300, 400)位置
# pyautogui.dragTo(300, 400, 2, button='left')
# # 按住鼠标左键，用0.2秒钟把鼠标向上拖拽
# pyautogui.dragRel(0, -60, duration=0.2)
#
# # pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# # 其中，button属性可以设置成left，middle和right。
# pyautogui.click(10, 20, 2, 0.25, button='left')
# pyautogui.click(x=100, y=200, duration=2)  # 先移动到(100, 200)再单击
# pyautogui.click()  # 鼠标当前位置点击一下
# pyautogui.doubleClick()  # 鼠标当前位置左击两下
# pyautogui.doubleClick(x=100, y=150, button="left")  # 鼠标在（100，150）位置左击两下
# pyautogui.tripleClick()  # 鼠标当前位置左击三下
#
# pyautogui.mouseDown()  # 鼠标左键按下再松开
# pyautogui.mouseUp()
# pyautogui.mouseDown(button='right')  # 按下鼠标右键
# pyautogui.mouseUp(button='right', x=100, y=200)  # 移动到(100, 200)位置，然后松开鼠标右键
#
# # scroll函数控制鼠标滚轮的滚动，amount_to_scroll参数表示滚动的格数。正数则页面向上滚动，负数则向下滚动
# # pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
# pyautogui.scroll(5, 20, 2)
# pyautogui.scroll(10)  # 向上滚动10格
# pyautogui.scroll(-10)  # 向下滚动10格
# pyautogui.scroll(10, x=100, y=100)  # 移动到(100, 100)位置再向上滚动10格
#
# # 缓动/渐变函数可以改变光标移动过程的速度和方向。通常鼠标是匀速直线运动，这就是线性缓动/渐变函数。
# # PyAutoGUI有30种缓动/渐变函数，可以通过pyautogui.ease*?查看。
# # 开始很慢，不断加速
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
# # 开始很快，不断减速
# pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
# # 开始和结束都快，中间比较慢
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)
# # 一步一徘徊前进
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)
# # 徘徊幅度更大，甚至超过起点和终点
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)


# # 案例获取鼠标的位置，方便复制我们定位的鼠标坐标点到代码中
# import pyautogui
# import time
#
#
# # 获取鼠标位置
# def get_mouse_positon():
#     time.sleep(5)  # 准备时间
#     print('开始获取鼠标位置')
#     try:
#         for i in range(10):
#             # Get and print the mouse coordinates.
#             x, y = pyautogui.position()
#             positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
#             pix = pyautogui.screenshot().getpixel((x, y))  # 获取鼠标所在屏幕点的RGB颜色
#             positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
#                 3) + ')'
#             print(positionStr)
#             time.sleep(0.5)  # 停顿时间
#     except:
#         print('获取鼠标位置失败')
#
#
# if __name__ == "__main__":
#     get_mouse_positon()
# import pyautogui
# pyautogui.moveTo(200, 0, duration=0.25)
# pyautogui.mouseDown(button='left')
# #  移动到(100, 200)位置，然后松开鼠标右键
# pyautogui.mouseUp(button='left', x=100, y=200)
# pyautogui.screenshot('foo.png') #截图
import win32gui
FrameClass = "WeChatMainWndForPC"
FrameTitle = "微信"
wrHd = win32gui.FindWindow(FrameClass, FrameTitle)
print(win32gui.SetForegroundWindow(wrHd))
from PIL import ImageGrab
bbox = (0, 0, 1160, 500)
im = ImageGrab.grab(bbox)
im.save('demo.png')