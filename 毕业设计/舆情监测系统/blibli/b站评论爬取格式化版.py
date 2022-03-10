# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/10 14:24
import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'XXX'
}
# 视频bv
bv = 'BV1xa411h7aM'
# 评论页数
pn = 1
# 排序种类 0是按时间排序 2是按热度排序
sort = 2

i = 1
panduan = 0

# bv，av互换算法
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


def enc(x):
    x = (x ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[x // 58 ** i % 58]
    return ''.join(r)


# bv转换成oid
oid = dec(bv)

fp = open('comment.txt', "w", encoding="UTF-8")
while True:
    print(pn)
    url = f'https://api.bilibili.com/x/v2/reply?pn={pn}&type=1&oid={oid}&sort={sort}'
    reponse = requests.get(url, headers=headers)
    a = json.loads(reponse.text)
    if pn == 1:
        count = a['data']['page']['count']
        size = a['data']['page']['size']
        page = count // size + 1
        print(page)
    for b in a['data']['replies']:
        panduan = 0
        str1 = ''
        str_list = list(b['content']['message'])
        for x in range(len(str_list)):
            if str_list[x] == '[':
                panduan = 1
            if panduan != 1:
                str1 = str1 + str_list[x]
            if str_list[x] == ']':
                panduan = 0
        fp.write(str(i) + '、' + str1 + '\n' + '-' * 10 + '\n')
        print(str1)
        print('-' * 10)
        i = i + 1
        if pn != page:
            pn += 1
        else:
            fp.close()
            break
