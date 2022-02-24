# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/24 20:57
import os
# logo1="""
# ┏━━━━━━━━━━━━━━━━━━━━┒
# ┃                                     ┃
# ┃ 监视器 3.0     作者 bianchengxueseng ┃
# ┃                                     ┃
# ┖━━━━━━━━━━━━━━━━━━━━┛
# """
# logo2="""
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# """
# print(logo1)
# print("欢迎使用监视器3.0")
# host=input("请输入目标IP：")
# flies=input("请输入保存文件名：")
# print("数据将保存至C盘 "+flies+".txt")
# print("正在连接中...")
# print("请稍等...")
# print(logo2)
# print("结果：")
# print(logo2)
# flies = "data"
# host = "192.168.160.16"
# os.system("CSCRIPT monitor.vbs "+host+" user password C:/"+flies)
# os.system("CSCRIPT monitor.vbs ")
# #system函数可以将字符串转化成命令在服务器上运行；其原理是每一条system函数执行时，其会创建一个子进程在系统上执行命令行，子进程的执行结果无法影响主进程；
# Cscript.exe是脚本运行引擎
# 在cscript.exe来寻找和连接脚本的运行库，最常见的有VBScript和JavaScript。
# 该进程在服务器当中起到了至关重要的作用，如服务器应用程序的运行和CGI的运行等……
# 由于运行脚本时该进程就会启动，所以当此进程感染病毒之后，将会成为极度危险的“病毒运行宿主”。需要小心
os.system("CSCRIPT hellow.vbs")
input("按下Enter键退出")
