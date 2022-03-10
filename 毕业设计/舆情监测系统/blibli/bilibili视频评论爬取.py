# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/9 15:30
from logger import logger as log
# log.info("测试")
import re
import urllib.request
import time
table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608
def dec(x):
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58 ** i
    return (r - add) ^ xor
def enc(x):#这个代码是oid转bv
    x = (x ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[x // 58 ** i % 58]
    return ''.join(r)
# 其中参数 pn 是评论的页数 ； oid 就是视频网址后面的 av那一串数字；sort一看就清楚是排序方式，0是按时间排序，2是按热度
comment_list = []  # 创建空列表
bv = "BV1pR4y1G7UC"#身后
oid = dec(bv)
for i in range(5):  # 动态下面的评论总共有115页
    sort = 2
    # oid = "378081993930152813"
    url = f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={str(i)}&type=1&oid={oid}&sort={sort}'  # 动态评论的接口（请大家不要恶意攻击造成负荷）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}  # 代理用户进行浏览器伪装
    html = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(html).read().decode('utf-8')
    comment = re.findall(r'"content":{"message":"(.*?)"', data, re.S)  # 用正则表达式扒所需要的评论内容获取，只爬了评论内容
    print(len(comment))  # 输出每页有多少个回复
    # for com in comment:
    #     print(com)
    comment_list.extend(comment)  # 将评论内容一个个添加进空列表
    time.sleep(2)
print('评论已经爬取完成')
for r in comment_list:
    # print(r)  # 写
    comment_txt = open(r'{}.txt'.format(bv), 'w', encoding='utf-8')  # 创建txt文本
    for r in comment_list:
        comment_txt.write(r+"\n")  # 写入txt文本
        # comment_txt.write('-' * 10+"\n")
    comment_txt.close()