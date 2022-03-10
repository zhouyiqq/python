# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/9 21:22
# import json
# from selenium import webdriver
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
# opt = webdriver.FirefoxOptions()
# opt.add_argument('--user-agent=%s' % user_agent)
# driver = webdriver.Firefox(options=opt)
# url ="https://passport.bilibili.com/ajax/miniLogin/minilogin"
# driver.get(url)
# with open('cookies.txt', 'r') as cookief:
#     # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
#     cookieslist = json.load(cookief)
#     for cookie in cookieslist:
#         driver.add_cookie(cookie)
# driver.get("https://space.bilibili.com/116683")
# driver.refresh()

# table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
# tr={}
# for i in range(58):
# 	tr[table[i]]=i
# s=[11,10,3,8,4,6]
# xor=177451812
# add=8728348608
#
# def dec(x):
# 	r=0
# 	for i in range(6):
# 		r+=tr[x[s[i]]]*58**i
# 	return (r-add)^xor
#
# def enc(x):
# 	x=(x^xor)+add
# 	r=list('BV1  4 1 7  ')
# 	for i in range(6):
# 		r[s[i]]=table[x//58**i%58]
# 	return ''.join(r)
#
# print(dec('BV1ZV411a7vy'))
# print(dec('BV1Q541167Qg'))
# print(dec('BV1mK4y1C7Bz'))
# print(enc(378081993930152813))
# print(enc(455017605))
# print(enc(882584971))


# import requests
# from bs4 import BeautifulSoup
# import json
# headers={
#     'User-Agent': 'XXX'
# }
# #视频bv
# bv = 'BV18t411y7a6'
# #评论页数
# pn = 1
# #排序种类 0是按时间排序 2是按热度排序
# sort = 2
#
# i=1
# panduan=0
#
# #bv，av互换算法
# table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
# tr={}
# for i in range(58):
# 	tr[table[i]]=i
# s=[11,10,3,8,4,6]
# xor=177451812
# add=8728348608
#
# def dec(x):
# 	r=0
# 	for i in range(6):
# 		r+=tr[x[s[i]]]*58**i
# 	return (r-add)^xor
#
# def enc(x):
# 	x=(x^xor)+add
# 	r=list('BV1  4 1 7  ')
# 	for i in range(6):
# 		r[s[i]]=table[x//58**i%58]
# 	return ''.join(r)
#
# #bv转换成oid
# oid = dec(bv)
#
# fp = open('comment.txt',"w",encoding="UTF-8")
# while True:
# 	url =f'https://api.bilibili.com/x/v2/reply?pn={pn}&type=1&oid={oid}&sort={sort}'
# 	reponse = requests.get(url,headers=headers)
# 	a = json.loads(reponse.text)
# 	if pn==1:
# 		count = a['data']['page']['count']
# 		size = a['data']['page']['size']
# 		page = count//size+1
# 		print(page)
# 		for b in a['data']['replies']:
# 			panduan = 0
# 			str1=''
# 			str_list = list(b['content']['message'])
# 			for x in range(len(str_list)):
# 				if str_list[x]=='[':
# 					panduan=1
# 				if panduan!=1:
# 					str1 = str1+str_list[x]
# 				if str_list[x] == ']':
# 					panduan=0
# 			fp.write(str(i)+'、'+str1+'\n'+'-'*10+'\n')
# 			print(str1)
# 			print('-'*10)
# 			i = i + 1
# 			if pn!=page:
# 				pn += 1
# 			else:
# 				fp.close()
# 				break
#
#

#接口已经被关闭
# import requests
# import re
# import os
# import sys
# import json
#
# # B站API详情 https://github.com/Vespa314/bilibili-api/blob/master/api.md
#
# # 视频AV号列表
# aid_list = []
#
# # 评论用户及其信息
# info_list = []
#
# # 获取指定UP的所有视频的AV号 mid:用户编号 size:单次拉取数目 page:页数
# def getAllAVList(mid, size, page):
#     # 获取UP主视频列表
#     for n in range(1,page+1):
#         url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=" + \
#             str(mid) + "&pagesize=" + str(size) + "&page=" + str(n)
#         r = requests.get(url)
#         text = r.text
#         json_text = json.loads(text)
#         # 遍历JSON格式信息，获取视频aid
#         for item in json_text["data"]["vlist"]:
#             aid_list.append(item["aid"])
#     print(aid_list)
#
# # 获取一个AV号视频下所有评论
# def getAllCommentList(item):
#     url = "http://api.bilibili.com/x/reply?type=1&oid=" + str(item) + "&pn=1&nohot=1&sort=0"
#     r = requests.get(url)
#     numtext = r.text
#     json_text = json.loads(numtext)
#     commentsNum = json_text["data"]["page"]["count"]
#     page = commentsNum // 20 + 1
#     for n in range(1,page):
#         url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn="+str(n)+"&type=1&oid="+str(item)+"&sort=1&nohot=1"
#         req = requests.get(url)
#         text = req.text
#         json_text_list = json.loads(text)
#         for i in json_text_list["data"]["replies"]:
#             info_list.append([i["member"]["uname"],i["content"]["message"]])
#     # print(info_list)
#
# # 保存评论文件为txt
# def saveTxt(filename,filecontent):
#     filename = str(filename) + ".txt"
#     for content in filecontent:
#         with open(filename, "a", encoding='utf-8') as txt:
#             txt.write(content[0] +' '+content[1].replace('\n','') + '\n\n')
#         print("文件写入中")
#
# if __name__ == "__main__":
#     # 爬取逆风笑 只爬取第一页的第一个
#     getAllAVList(2019740,1,1)
#     for item in aid_list:
#         info_list.clear()
#         getAllCommentList(item)
#         saveTxt(item,info_list)

# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/10 10:29
# !/usr/bin/env python
# -*-coding:utf-8-*-
# import requests
# import random
# import time
#
#
# def get_json(url,num):
#     headers = {
#         'User-Agent':
#             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
#     }
#
#     params = {
#         'page_size': 10,
#         'next_offset': str(num),
#         'tag': '今日热门',
#         'platform': 'pc'
#     }
#
#     try:
#         html = requests.get(url, params=params, headers=headers)
#         return html.json()
#
#     except BaseException:
#         print('request error')
#         pass
#
#
# def downloader(url, path):
#     start = time.time()  # 开始时间
#     size = 0
#     headers = {
#         'User-Agent':
#             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
#     }
#
#     response = requests.get(url, headers=headers, stream=True)  # stream属性必须带上
#     chunk_size = 1024  # 每次下载的数据大小
#     content_size = int(response.headers['content-length'])  # 总大小
#     if response.status_code == 200:
#         print('[文件大小]:%0.2f MB' % (content_size / chunk_size / 1024))  # 换算单位
#         with open(path, 'wb') as file:
#             for data in response.iter_content(chunk_size=chunk_size):
#                 file.write(data)
#                 size += len(data)  # 已下载的文件大小
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
#         num = i * 10 + 1
#         html = get_json(url,num)
#         infos = html['data']['items']
#         for info in infos:
#             title = info['item']['description']  # 小视频的标题
#             video_url = info['item']['video_playurl']  # 小视频的下载链接
#             print(title)
#
#             # 为了防止有些视频没有提供下载链接的情况
#             try:
#                 downloader(video_url, path='%s.mp4' % title)
#                 print('成功下载一个!')
#
#             except BaseException:
#                 print('凉凉,下载失败')
#                 pass
#
#         # time.sleep(int(format(random.randint(2, 8))))  # 设置随机等待时间


#
# import requests
# from lxml import etree
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# import matplotlib.pyplot as plt
#
# class BiliSpider:
#     def __init__(self, BV, oid):
#         # 构造要爬取的视频url地址
#         self.BVurlBV = BV
#         self.BVurloid = oid
#         self.BVurl = "https://m.bilibili.com/video/" + BV
#         self.headers = {
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#
#     # 弹幕都是在一个url请求中，该url请求在视频url的js脚本中构造
#     def getXml_url(self):
#         # 获取该视频网页的内容
#         response = requests.get(self.BVurl, headers=self.headers)
#         html_str = response.content.decode()
#         # print(html_str)
#         # 使用正则找出该弹幕地址
#         # 弹幕地址为https://comment.bilibili.com/oid.xml
#         # 格式为：https://comment.bilibili.com/168087953.xml
#         # 我们分隔出的是地址中的弹幕文件名，即 168087953
#         # getWord_url = re.findall(" '//comment.bilibili.com/'+ (.*) +'.xml',", html_str)
#         getWord_url = str(self.BVurloid)
#
#         # getWord_url = getWord_url[0].replace("+", "").replace(" ", "")
#         # 组装成要请求的xml地址
#         xml_url = "https://comment.bilibili.com/{}.xml".format(getWord_url)
#         return xml_url
#
#     # Xpath不能解析指明编码格式的字符串，所以此处我们不解码，还是二进制文本
#     def parse_url(self, url):
#         response = requests.get(url, headers=self.headers)
#         # print(response.content)
#         return response.content
#
#     # 弹幕包含在xml中的<d></d>中，取出即可
#     def get_word_list(self, str):
#         html = etree.HTML(str)
#         word_list = html.xpath("//d/text()")
#         return word_list
#
#     # 标题及up主名
#     def get_tile(self):
#         response = requests.get(self.BVurl, headers=self.headers)
#         # print(response.text)
#         html_str = response.content.decode()
#         html = etree.HTML(html_str)
#         # print(html_str)
#         up_name = html.xpath('//span/text()')[1]
#         up_tile = html.xpath('//h1/text()')[0]
#         tile = []
#         for i in up_name, up_tile:
#             tile.append(i)
#         print(up_name)
#         print(up_tile)
#         print(tile)
#         return tile[0]+tile[1]
#
#     # BV1ZV411a7vy 261482616
#     # 保存弹幕为文本格式
#     def save_file(self, data):
#         """
#         保存弹幕
#         :param data: 弹幕信息
#         :return:
#         """
#         with open("%s弹幕.text" % self.get_tile(), 'w', encoding='utf8') as f:
#             for line in data:
#                 f.write(line)
#                 f.write('\n')
#
#     # 词云
#     def wardcloud_(self):
#         fp = open("%s弹幕.text" % self.get_tile(), 'r', encoding='utf-8')
#         # fp = open("笔记列表 弹幕.text", 'r', encoding='utf-8')
#         text = fp.read()
#         # wd = WordCloud(background_color='white', width=300, height=316, margin=2,
#         #                font_path='钟齐段宁行书.TTF').generate(text)
#         wd = WordCloud(background_color='white', width=300, height=316, margin=2,font_path='simhei.ttf').generate(text)
#         plt.figure(dpi=500)
#         # 显示词云
#         plt.imshow(wd)
#         # 去除x，y 轴
#         plt.axis('off')
#         plt.show()
#         # 保存词云
#         wd.to_file("%s弹幕.jpg" % self.get_tile())
#
#     def run(self):
#         # 1.根据BV号获取弹幕的地址
#         start_url = self.getXml_url()
#         # 2.请求并解析数据
#         xml_str = self.parse_url(start_url)
#         # print(start_url)
#         word_list = self.get_word_list(xml_str)
#         print(word_list)
#         # 3.打印
#         for word in word_list:
#             print(word)
#         # # 4.保存
#         # self.save_file(word_list)
#         # 5.词云
#         # self.wardcloud_()
# def bv_to_oid(bv):
#     table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
#     tr = {}
#     for i in range(58):
#         tr[table[i]] = i
#     s = [11, 10, 3, 8, 4, 6]
#     xor = 177451812
#     add = 8728348608
#     def dec(x):
#         r = 0
#         for i in range(6):
#             r += tr[x[s[i]]] * 58 ** i
#         return (r - add) ^ xor
#     def enc(x):#这个代码是oid转bv
#         x = (x ^ xor) + add
#         r = list('BV1  4 1 7  ')
#         for i in range(6):
#             r[s[i]] = table[x // 58 ** i % 58]
#         return ''.join(r)
#     oid = dec(bv)
#     return oid
#
#
# if __name__ == '__main__':
#     # BVName = input("请输入要爬取的视频的BV号:")
#     # oid = input("请输入要爬取的视频的oid（F12中找oid）号:")
#     BVName ="BV1xa411h7aM"
#     oid = bv_to_oid(BVName)
#     spider = BiliSpider(BVName, oid)
#     spider.run()
