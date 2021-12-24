import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 指定默认字体
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
df = pd.read_excel("服务器运行情况表.xlsx",sheet_name="主机信息",index_col=0)
name = "最近两周内存使用率峰值(%)"
print(df[name].value_counts().to_string())
plt.title(name+"分布情况")
# plt.xlabel(name)
# plt.ylabel("数量")
# df.set_index('标签', inplace=True)
df[name].value_counts().sort_values().plot.pie(figsize=(8, 8),autopct='%.2f%%',counterclock=False)
# df[["CPU核数"]].plot(kind='line',stacked = True,rot=0)
# df[["CPU平均使用量"]].plot(kind='line',stacked = True,rot=0)
# df[["内存大小"]].plot(kind='line',stacked = True,rot=0)
# df[["内存平均使用量"]].plot(kind='line',stacked = True,rot=0)
# df[["空闲内存"]].plot(kind='line',stacked = True,rot=0)
# df[["磁盘大小"]].plot(kind='line',stacked = True,rot=0)
# df[["磁盘平均使用量"]].plot(kind='line',stacked = True,rot=0)
# df[["主机年费(元)"]].plot(kind='line',stacked = True,rot=0)
# df[["CPU核数","CPU平均使用量","内存大小","内存平均使用量","空闲内存","磁盘大小","磁盘平均使用量","主机年费(元)",]].plot(kind='line',stacked = True,rot=0)
# df[["最近两周内存使用率峰值(%)"]].plot(kind='line',stacked = True,rot=0)
# print(df.to_string())
# print(df)
# print(df.info())
# print(df.describe())
# name = "当前日费用（元）"
# df2 = pd.read_excel("服务器运行情况表.xlsx",sheet_name="RDS计费统计",index_col=0)
# df2[name].value_counts().sort_values().plot.pie(figsize=(8, 8),autopct='%.2f%%',counterclock=False)
# print(df2.to_string())
# print(df2.info())
# print(df2.loc[0])
# print(df2[["应用系统","当前日费用（元）"]])

# df2[["CPU"]].plot(kind='barh',stacked = True,rot=0)
# df2[["内存(GB)"]].plot(kind='barh',stacked = True,rot=0)
# df2[["磁盘(GB)"]].plot(kind='barh',stacked = True,rot=0)
# df2[["当前日费用（元）"]].plot(kind='barh',stacked = True,rot=0)
# df2[["最近7天费用（元）"]].plot(kind='barh',stacked = True,rot=0)
# df2[["CPU"]].plot(kind='line',stacked = True,rot=0)
# df2[["内存(GB)"]].plot(kind='line',stacked = True,rot=0)
# df2[["磁盘(GB)"]].plot(kind='line',stacked = True,rot=0)
# df2[["当前日费用（元）"]].plot(kind='line',stacked = True,rot=0)
# df2[["最近7天费用（元）"]].plot(kind='line',stacked = True,rot=0)
plt.show()
# print(df2.describe())