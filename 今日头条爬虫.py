# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/30 17:10
import sys
import pandas
from selenium.webdriver.support.ui import WebDriverWait
import requests
import bs4
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
import pymysql
password='123456'
def createDb():
    db = pymysql.connect(host='localhost', user='root', password=password, port=3306,charset='utf8mb4')
    cursor = db.cursor();
    sql = 'CREATE DATABASE bilibili CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci'
    cursor.execute(sql)
    cursor.close()
    db = pymysql.connect(host='localhost', user='root', password=password,
                         port=3306, db='news',charset='utf8mb4')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS news (id int(11) NOT NULL AUTO_INCREMENT, ' \
          'title VARCHAR(255) NOT NULL,type VARCHAR(12) NOT NULL, ' \
          'content  NOT NULL, birthday VARCHAR(255),' \
          'focus VARCHAR(255),fans VARCHAR(255),area VARCHAR(255),' \
          'praise VARCHAR(255),view VARCHAR(255),' \
          'sign VARCHAR(255) NOT NULL,title VARCHAR(255) NOT NULL,' \
          'PRIMARY KEY (id,up_id))'
    cursor.execute(sql)
    db.close()
    db = pymysql.connect(host='localhost', user='root', password=password,
                         port=3306, db='bilibili',charset='utf8mb4')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS fans (id int(11) NOT NULL AUTO_INCREMENT,' \
          'up_id VARCHAR(255) NOT NULL,fans_id VARCHAR(255) NOT NULL,' \
          'fans_name VARCHAR(255) NOT NULL, sex VARCHAR(10) NOT NULL,' \
          'fans_level VARCHAR(10) NOT NULL,viplevel VARCHAR(255) NOT NULL,' \
          'time VARCHAR(255) NOT NULL,' \
          'PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()
