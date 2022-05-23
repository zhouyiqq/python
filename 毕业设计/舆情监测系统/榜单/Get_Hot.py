# coding:gbk
# ����ֿ� was created by zy on 2022/2/15 21:32
import datetime
import os
import pprint
import sys
import requests
import winsound
from bs4 import BeautifulSoup
import time
import pandas
import re
class GetHot():
    def __init__(self):
        self.url='https://tophub.today'
        self.headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/538.55 (KHTML, like Gecko) Chrome/81.0.3345.132 Safari/538.55'
        }
        html = self.getHtml()
        data = self.get_data(html)
        path = f"./tophub{datetime.datetime.now().strftime('%Y-%m-%d')}.xlsx"
        # if not os.path.exists(path):
        df = pandas.DataFrame()
        df.to_excel(path, index=False)
        res = pandas.read_excel(path,engine=None)
        # text = ["΢��","֪��","΢��","�ٶ�"]
        # res = pandas.DataFrame()
        # # ��ʾ������
        # pandas.set_option('display.max_columns', None)
        # # ��ʾ������
        # pandas.set_option('display.max_rows', None)
        # # ����value����ʾ����Ϊ100��Ĭ��Ϊ50
        # pandas.set_option('max_colwidth', 100 )
        res = self.get_node_data(res, data)
        # pprint.pprint(res)
        print("���ݴ������")
        res.to_excel(path)
        # input()
    def getHtml(self):
        resp = requests.get(self.url, headers=self.headers)
        # pprint.pprint(resp.text)
        return resp.text
    def get_data(self,html):
        soup = BeautifulSoup(html, 'html.parser')
        nodes = soup.find_all('div', class_='cc-cd')
        # pprint.pprint("&" * 10)
        # pprint.pprint(nodes)
        return nodes
    def get_node_data(self,df, nodes):
        # now = int(time.time())
        for node in nodes:
            #�ǰ��ս��ֵ�
            # print(node)
            # print("#"*200)
            # if text == "΢��":
            source = node.find('div', class_='cc-cd-lb').text.strip()
            messages = node.find('div', class_='cc-cd-cb-l nano-content').find_all('a')
            for message in messages:
                content = message.find('span', class_='t').text.strip()
                heat = message.find('span', class_='e').text.strip()
                # if source == text:
                # reg = '��.+?��(.+)'
                # content = re.findall(reg, content)
                # print("#"*15)
                # print(content)
                if df.empty or df[df.content == content].empty:
                    data = {
                        'content': [content],
                        'url': [message['href']],
                        'source': [source],
                        'heat': [heat]
                    }
                    # 'start_time': [now],
                    # 'end_time': [now]

                    item = pandas.DataFrame(data)
                    df = pandas.concat([df, item], ignore_index=True)

                # else:
                    # index = df[df.content == content].index[0]
                    # # df.at[index, 'end_time'] = now
        return df
GetHot()