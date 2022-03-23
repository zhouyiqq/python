# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/8 11:15
import json
import time
import urllib
import pandas as pd
import urllib.request
# with open("情感分析数据.txt","r",encoding='utf_8') as f:
#     line = f.readline()
#     while line:
#         print(line)
#         line = f.readline()


# def sentiment_classify(text):
#     raw = {"text": "内容"}
#     raw['text'] = text
#     data = json.dumps(raw).encode('utf-8')
#     host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=[B2r5c6Xetc3c9SAH6QjzHpWt]&client_secret=[hyGvFuj8UkD6PS8RMX93YFAPlboiKyTn]'
#     # API Key 和 Secret Key的获取防范见下方博客链接
#     request = urllib.request.Request(url=host, data=data)
#     request.add_header('Content-Type', 'application/json')
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
#     rdata = json.loads(content)
#     return rdata
# def sentiment_classify(text):
#     """
#     获取文本的感情偏向（消极 or 积极 or 中立）
#     参数：
#     text:str 本文
#     """
#     raw = {"text":"内容"}
#     raw['text'] = text
#     data = json.dumps(raw).encode('utf-8')
#     AT = "?grant_type=client_credentials&client_id=[B2r5c6Xetc3c9SAH6QjzHpWt]&client_secret=[hyGvFuj8UkD6PS8RMX93YFAPlboiKyTn]"
#     host = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token="+AT
#     request = urllib.request.Request(url=host,data=data)
#     request.add_header('Content-Type', 'application/json')
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
#     rdata = json.loads(content)
#     return rdata


import requests
import ast
def sentiment_classify(text):
    API_KEY = 'B2r5c6Xetc3c9SAH6QjzHpWt'
    SECRET_KEY = 'hyGvFuj8UkD6PS8RMX93YFAPlboiKyTn'

    response = requests.get(
        url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
            API_KEY, SECRET_KEY
        ), headers={'Content-Type': 'application/json; charset=UTF-8'})
    raw = {"text": "内容"}
    raw['text'] = text
    data = json.dumps(raw).encode('utf-8')
    r = requests.post(
        url='https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={}'.format(
            ast.literal_eval(response.text)['access_token']),
        headers={'Content-Type': 'application/json'},
        data=data
    )
    return r.json()
    # print(r.json())
# # encoding:utf-8
# import requests
#
# # client_id 为官网获取的API Key， client_secret 为官网获取的Secret Key
# host = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token=24.f9ba9c5241b67688bb4adbed8bc91dec.2592000.1485570332.282335-8574074"
# response = requests.get(host)
# if response:
#     print(response.json())
# print(sentiment_classify("你好"))
#
if __name__ == '__main__':
    # file = '情感分析数据.txt'
    # text = pd.read_excel(file)
    # review = text['txt']
    # length = len(review)
    review=[]
    with open("情感分析数据.txt", "r", encoding='utf_8') as f:
        line = f.readline()
        # while line:
        for i in range(30):
            review.append(line)
            # print(line)
            line = f.readline()
    length = len(review)
    # 初始化用来存储情感分析结果的列表
    sentiment = ['blank'] * length
    confidence = ['blank'] * length
    positive_prob = ['blank'] * length
    contents = ['blank'] * length
    time_start = time.time()  # 计时
    i = 0
    for content in review:
        content = content[:512]  # 百度api限制512个字符，过长也会导致出错
        print(content)
        op = True  # 利用循环和输出条件来保证获取到情绪分析的结果
        while op:
            maxTryNum = 50  # 设置最大尝试访问的次数，通过多次访问保证不会因为访问受限制而得不到结果（可修改）
            for tries in range(maxTryNum):
                try:
                    result = sentiment_classify(content)
                    break
                except:
                    if tries < (maxTryNum - 1):
                        continue
                    else:
                        print('尝试了 %d 次都失败了！！！'% maxTryNum)
                        break
            # 因为发现如果能够成功调用api则输出结果长度为3，失败了长度为2，故将其设为控制输出的条件
            if len(result) == 3:
                op = False
            else:
                op = True

        result1 = result.get('items')
        item = result1[0]
        contents[i] = content
        sentiment[i] = item['sentiment']
        confidence[i] = item['confidence']
        positive_prob[i] = item['positive_prob']

        # 方便观察进度
        print('第 ' + str(i + 1) + ' 条评论已分析完成， 一共 ' + str(length) + ' 条评论')
        i = i + 1

    time_end = time.time()
    print('分析评论一共耗时：', time_end - time_start)
    text = pd.DataFrame()
    text["text"] = contents
    text['sentiment'] = sentiment
    text['confidence'] = confidence
    text['positive_prob'] = positive_prob
    # 保存
    text.to_excel('result.xlsx', index=None)
    # print(file + "    result写入成功!")
