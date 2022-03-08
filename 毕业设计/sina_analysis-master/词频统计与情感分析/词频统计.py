# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/8 11:15
import jieba
article = open(r'../data/cut_copy.txt','rb').read()
dele = {'。','！','？','的','“','”','（','）',' ','》','《','，'}
jieba.add_word('大数据')
words = list(jieba.cut(article))
articleDict = {}
articleSet = set(words)-dele
for w in articleSet:
    if len(w)>1:
        articleDict[w] = words.count(w)
articlelist = sorted(articleDict.items(),key = lambda x:x[1], reverse = True)

for i in range(10):
    print(articlelist[i])