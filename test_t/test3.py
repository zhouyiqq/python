# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/14 21:58
# !/usr/bin/env python
# coding:utf-8
import akshare as ak
from matplotlib import pyplot as plt
df_index = ak.weibo_index("美国","3month")
print(df_index)
df_index.plot()
plt.show()