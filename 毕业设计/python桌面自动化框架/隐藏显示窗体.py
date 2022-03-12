# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/12 20:36
import win32con
import win32gui
import time

# 找出窗体编号
# QQWin = win32gui.FindWindow("TXGuiFoundation", "我的iPhone")  # 类名，标题
QQWin = win32gui.FindWindow("TXGuiFoundation", "周刚")  # 类名，标题
CmdWin = win32gui.FindWindow("ConsoleWindowClass", "管理员: C:\windows\system32\cmd.exe")  # 控制CMD窗体

while True:
    # 隐藏窗体
    win32gui.ShowWindow(QQWin, win32con.SW_HIDE)
    time.sleep(2)
    # 显示窗体
    win32gui.ShowWindow(QQWin, win32con.SW_SHOW)