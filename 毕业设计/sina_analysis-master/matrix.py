# coding:utf-8


import jieba
import pandas as pd
import codecs
import string
import re

# 清洗文本
def clearTxt(line:str):
    if(line != ''):
        line = line.strip()
        # 去除文本中的英文和数字
        line = re.sub("[a-zA-Z0-9]", "", line)
        # 去除文本中的中文符号和英文符号
        line = re.sub("[\s+\.\!\/_,$%^*(+\"\'；：“”．]+|[+——！，。？?、~@#￥%……&*（）]+", "", line)
        return line
    return None

#文本切割
def sent2word(line,stopword):
    segList = jieba.cut(line,cut_all=False)
    segSentence = ''
    for word in segList:
        if word not in stopword:
            segSentence += word + " "
    return segSentence.strip()#移除字符串头尾的空格和换行符

if __name__ == '__main__':
    df = pd.read_csv('data/女神节.csv')
    target = codecs.open('data/cut.txt', 'w', encoding='utf-8')
    stopword = ['\t',"的","了","是","大","上","和","去","人","我","你","还","在","也","有","又","不","被","或","像"]
    stop = open('data/stopword', 'r', encoding='utf-8')
    line = stop.readline()  # 调用文件的 readline()方法
    while line:
        # print(line, end = '')　      # 在 Python 3 中使用
        line = stop.readline()
        stopword.append(line.strip())
    stop.close()
    # print(stopword)
    for i in df['text']:
        line = clearTxt(i)
        seg_line = sent2word(line,stopword)
        target.writelines(seg_line + '\n')

