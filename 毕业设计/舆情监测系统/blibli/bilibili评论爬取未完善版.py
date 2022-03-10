# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/10 14:18
from xml import etree

import requests
# from lxml import etree
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# import matplotlib.pyplot as plt
#
from matplotlib import pyplot as plt
from wordcloud import WordCloud


class BiliSpider:
    def __init__(self, BV, oid):
        # 构造要爬取的视频url地址
        self.BVurlBV = BV
        self.BVurloid = oid
        self.BVurl = "https://m.bilibili.com/video/" + BV
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    # 弹幕都是在一个url请求中，该url请求在视频url的js脚本中构造
    def getXml_url(self):
        # 获取该视频网页的内容
        response = requests.get(self.BVurl, headers=self.headers)
        html_str = response.content.decode()
        # print(html_str)
        # 使用正则找出该弹幕地址
        # 弹幕地址为https://comment.bilibili.com/oid.xml
        # 格式为：https://comment.bilibili.com/168087953.xml
        # 我们分隔出的是地址中的弹幕文件名，即 168087953
        # getWord_url = re.findall(" '//comment.bilibili.com/'+ (.*) +'.xml',", html_str)
        getWord_url = str(self.BVurloid)

        # getWord_url = getWord_url[0].replace("+", "").replace(" ", "")
        # 组装成要请求的xml地址
        xml_url = "https://comment.bilibili.com/{}.xml".format(getWord_url)
        return xml_url

    # Xpath不能解析指明编码格式的字符串，所以此处我们不解码，还是二进制文本
    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        # print(response.content)
        return response.content

    # 弹幕包含在xml中的<d></d>中，取出即可
    def get_word_list(self, str):
        html = etree.HTML(str)
        word_list = html.xpath("//d/text()")
        return word_list

    # 标题及up主名
    def get_tile(self):
        response = requests.get(self.BVurl, headers=self.headers)
        # print(response.text)
        html_str = response.content.decode()
        html = etree.HTML(html_str)
        # print(html_str)
        up_name = html.xpath('//span/text()')[1]
        up_tile = html.xpath('//h1/text()')[0]
        tile = []
        for i in up_name, up_tile:
            tile.append(i)
        print(up_name)
        print(up_tile)
        print(tile)
        return tile[0]+tile[1]

    # BV1ZV411a7vy 261482616
    # 保存弹幕为文本格式
    def save_file(self, data):
        """
        保存弹幕
        :param data: 弹幕信息
        :return:
        """
        with open("%s弹幕.text" % self.get_tile(), 'w', encoding='utf8') as f:
            for line in data:
                f.write(line)
                f.write('\n')

    # 词云
    def wardcloud_(self):
        fp = open("%s弹幕.text" % self.get_tile(), 'r', encoding='utf-8')
        # fp = open("笔记列表 弹幕.text", 'r', encoding='utf-8')
        text = fp.read()
        # wd = WordCloud(background_color='white', width=300, height=316, margin=2,
        #                font_path='钟齐段宁行书.TTF').generate(text)
        wd = WordCloud(background_color='white', width=300, height=316, margin=2,font_path='simhei.ttf').generate(text)
        plt.figure(dpi=500)
        # 显示词云
        plt.imshow(wd)
        # 去除x，y 轴
        plt.axis('off')
        plt.show()
        # 保存词云
        wd.to_file("%s弹幕.jpg" % self.get_tile())

    def run(self):
        # 1.根据BV号获取弹幕的地址
        start_url = self.getXml_url()
        # 2.请求并解析数据
        xml_str = self.parse_url(start_url)
        # print(start_url)
        word_list = self.get_word_list(xml_str)
        print(word_list)
        # 3.打印
        for word in word_list:
            print(word)
        # 4.保存
        self.save_file(word_list)
        # 5.词云
        # self.wardcloud_()
def bv_to_oid(bv):
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
    oid = dec(bv)
    return oid


if __name__ == '__main__':
    # BVName = input("请输入要爬取的视频的BV号:")
    # oid = input("请输入要爬取的视频的oid（F12中找oid）号:")
    BVName ="BV1xa411h7aM"
    oid = bv_to_oid(BVName)
    spider = BiliSpider(BVName, oid)
    spider.run()
