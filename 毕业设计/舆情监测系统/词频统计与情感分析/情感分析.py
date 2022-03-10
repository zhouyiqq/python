# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/8 11:15
with open("情感分析数据.txt","r",encoding='utf_8') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
