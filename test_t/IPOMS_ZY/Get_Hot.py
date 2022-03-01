# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/15 21:32
import requests
from bs4 import BeautifulSoup
import time
import pandas
import re
class GetHot:
    url = 'https://tophub.today'
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/538.55 (KHTML, like Gecko) Chrome/81.0.3345.132 Safari/538.55'}
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)
    # nodes = soup.find_all('div', class_='cc-cd')
    # res = pandas.read_excel('tophub.xlsx',engine='xlrd')
    # now = int(time.time())
    # for node in nodes:
    # 	source = node.find('div', class_='cc-cd-lb').text.strip()
    # 	messages = node.find('div', class_='cc-cd-cb-l nano-content').find_all('a')
    # 	for message in messages:
    # 		content = message.find('span', class_='t').text.strip()
    # 		if source == '微信':
    # 			reg = '「.+?」(.+)'
    # 			content = re.findall(reg, content)[0]
    #
    # 		if df.empty or df[df.content == content].empty:
    # 			data = {
    # 				'content': [content],
    # 				'url': [message['href']],
    # 				'source': [source],
    # 				'start_time': [now],
    # 				'end_time': [now]
    # 			}
    #
    # 			item = pandas.DataFrame(data)
    # 			df = pandas.concat([df, item], ignore_index=True)
    #
    # 		else:
    # 			index = df[df.content == content].index[0]
    # 			df.at[index, 'end_time'] = now
    #
    # res.to_excel('tophub.xlsx')