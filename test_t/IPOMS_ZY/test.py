# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/15 21:56
import akshare as ak
from matplotlib import pyplot as plt
df_index = ak.weibo_index("冬奥会")
df_index.plot()
plt.show()
