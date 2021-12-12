# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/11/7 17:57
#数字分割符
a = 100_00_00_00
print(a)
#交换变量值
a =10
b = 20
a,b = b,a
print(a,b)
#连接比较式
a = 20
if 10<=a<=30:
    print(a)
#字符串乘法
print("_"*20)
#列表拼接
a = [1,2,3,4,5]
b = [6,7,8,9]
c=a+b
print(c)
#列表切片
print(c[:-1])
#打包解包
c = [1,2]
a,b = c
print(a,b)
#witch语法
with open("C:/Users/zy/Desktop/新建文本文档.txt","r",encoding='utf-8' ,errors='ignore') as f:
    data = f.read()
    print(data)
#列表解析式
a = [1,2,3,4]
b = [e+200 for e in a]
print(b)