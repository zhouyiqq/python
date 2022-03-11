# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/11 19:47
import time
import pyttsx3
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+150)
f = open("./情感分析数据.txt", 'r',encoding='utf-8')
line = f.readline()
while line:
    line = f.readline()
    print(line)
    engine.say(line)
engine.runAndWait()
f.close()