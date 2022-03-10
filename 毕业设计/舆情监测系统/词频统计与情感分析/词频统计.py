# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/8 11:15
import jieba
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 指定默认字体
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
def show(df,kind,title):
    df.plot(kind=kind, title=title)
    plt.show()
article = open(r'情感分析数据.txt','rb').read()
dele = {'。','！','？','的','“','”','（','）',' ','》','《','，',"\r\n"}
jieba.add_word('大数据')
words = list(jieba.cut(article))
articleDict = {}
articleSet = set(words)-dele
for w in articleSet:
    if len(w)>1:
        articleDict[w] = words.count(w)
articlelist = sorted(articleDict.items(),key = lambda x:x[1], reverse = True)
data = []
for i in range(50):
    data.append(list(articlelist[i]))
    # print(articlelist[i][0],articlelist[i][1])
df = pd.DataFrame(data,columns=["关键词","数量"],index=[_[0] for _ in data])
df = df.sort_values("数量")
print(df)
show(df,"barh","词频统计")