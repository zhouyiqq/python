# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/16 19:17
import re
import urllib.request
import time
# 其中参数 pn 是评论的页数 ； oid 就是视频网址后面的 av那一串数字；sort一看就清楚是排序方式，0是按时间排序，2是按热度
def test1():
   time.sleep(2)
   comment_list = []  #创建空列表
   for i in range(115): #动态下面的评论总共有115页
      url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn='+str(i)+'&type=17&oid=378081993930152813&sort=2' #动态评论的接口（请大家不要恶意攻击造成负荷）
      headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' } #代理用户进行浏览器伪装
      html = urllib.request.Request(url = url,headers = headers)
      data = urllib.request.urlopen(html).read().decode('utf-8')
      comment = re.findall(r'"content":{"message":"(.*?)"',data,re.S) #用正则表达式扒所需要的评论内容获取，只爬了评论内容
      print(len(comment)) #输出每页有多少个回复
      comment_list.extend(comment) #将评论内容一个个添加进空列表
   print('评论已经爬取完成')
   comment_txt = open(r'/test_t/爬取b站评论并制作词云/comment.txt', 'w', encoding='utf-8') #创建txt文本

   for r in comment_list:

      comment_txt.write(r) #写入txt文本
   comment_txt.close()
