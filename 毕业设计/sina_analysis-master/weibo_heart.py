# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/28 10:10
import akshare as ak
from matplotlib import pyplot as plt
title = input("请输入搜索关键词：")
df_index = ak.weibo_index(title)
df_index.plot()
plt.show()
