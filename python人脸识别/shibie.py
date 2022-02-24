# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/23 19:36
import os
import test

# path="测试/"  #待读取的文件夹

# X = tf.placeholder(tf.float32, [1, 57*47])
# conv = test_t.convolution(X)
# saver = tf.compat.v1.train.Saver()
# session = tf.Session()
# saver.restore(session, './mod/best.ckpt')
# p = test_t.get('a.jpg', X, conv, session, 0)

# path_list=os.listdir(path)
# path_list.sort() #对读取的路径进行排序
b = []
# 学号列表
g = open('xuehao.txt', 'r')
# 读取xuehao.txt
with open('xuehao.txt', 'r') as fp:
    lines = len(fp.readlines())
    fp.close()
for i in range(lines):
    # 循环索引列表
    e = g.readline()
    # 读取g的数据，以字符串的形式返回
    e = e.split()
    # 把字符串分割成字符数组
    # ex = []
    # ex.append(e[0])
    # ex.append(''.join(e[1:]))
    b.append(e)
    # 将字符数组加入b列表中
path1 = "图片库/特征库/"
# 特征库地址
path_list1 = os.listdir(path1)
# 返回脸部特征向量列表
d = []
# 人脸特征列表
for fname in path_list1:
    # 当fname在脸部特征列表
    print(fname)
    c = open(path1 + fname, "r")
    # 读取这个脸部特征向量

    ff = c.read()
    ff = ff.rstrip(']')
    # 删除 string 字符串末尾的']'
    ff = ff.lstrip('[')
    # 删除 string 字符串开头的'['
    ff = ff.split(', ')
    # 以“，”分割字符串
    d.append(ff)
    # 将字符串数组加入d列表
c.close()
# 关闭学号文件
g.close()


# 关闭特征库文件
def shibie(file):
    # 识别图片人脸
    x = 0

    # print('真实:',i+1)
    min = 9000000000000000000000000000000000000
    # 参数
    # a=open(path+filename,"r")
    # f=a.read()
    # f=f.rstrip(']')
    # f=f.lstrip('[')
    # f=f.split(',')
    # print(f)

    # for i in range(len(f)):
    # b.append(float(f[i]))
    for i in range(len(d)):
        # KNN（K- Nearest Neighbor）法即K最邻近法，如果一个样本在特征空间中的K个最相似（即特征空间中最邻近）的样本中的大多数属于某一个类别，则该样本也属于这个类别
        # print(len(ff))
        # return
        s = 0
        for j in range(len(d[i])):
            # print(file[j],j)
            # print(d[i][j],i)
            s += (float(file[j]) - float(d[i][j])) ** 2
        if s < min:
            min = s
            y = i + 1
    # if int(y)==i+1:
    #     x+=1
    # if int(y)==i+1:
    #	x+=1
    y = int(y)
    # print('-'*50)
    for item in b:
        if y == int(item[0]):
            # print(item[1])
            return item[1]
        # 返回匹配的名字

    # print('正确率:',str(x/38*100)+'%')
# if __name__=='__main__':
#     shibie(path_list)
# shibie(p)