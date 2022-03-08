# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/8 12:57
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 指定默认字体
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
def show(df,kind,title):
    df.plot(kind=kind, title=title)
    plt.show()