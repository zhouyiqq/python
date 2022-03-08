# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/5 18:43
import re

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 指定默认字体
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
df = pd.read_excel(r"./tophub2022-03-08.xlsx")
###############################################################################################
"""
# plt.xlabel(name)
# plt.ylabel("数量")
# df.set_index('标签', inplace=True)
# df["source"].value_counts().sort_values().plot.pie(figsize=(8, 8),autopct='%.2f%%',counterclock=False)
df["source"].value_counts().sort_values().plot.bar(figsize=(20,10))
plt.show()"""
##############################################################################
choice = ["微博","知乎","微信","百度","哔哩哔哩","知乎","微信读书","抖音"]
index = 3
i=1
data =[]
for source,contect,heat in zip(df.source,df.content,df.heat):
    if source==choice[index]:
        print(choice[index])
        print(f"{i}."+contect)
        print(heat)
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        heat = re.sub(pattern, "", heat)
        try:
            if float(heat)>10000:
                heat = float(heat)/10000
            else:
                heat = float(heat)
            data.append([contect,heat])
        except Exception as e:
            print(e)
        i+=1
# print(data)
df1=pd.DataFrame(data,columns=["标号","热度/万"],index=[_[0] for _ in data])
df1 = df1.sort_values("热度/万")
print(df1)
df1[["热度/万"]].plot(kind ="barh",title=choice[index])
plt.show()