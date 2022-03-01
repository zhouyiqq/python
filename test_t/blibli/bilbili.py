import requests
import bs4
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
import pymysql

def createDb():
    db = pymysql.connect(host='localhost', user='root', password='', port=3306)
    cursor = db.cursor();
    sql = 'CREATE DATABASE bilibili'
    cursor.execute(sql)
    cursor.close()
    db = pymysql.connect(host='localhost', user='root', password='',
                         port=3306, db='bilibili')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS up (id int(11) NOT NULL AUTO_INCREMENT, ' \
          'up_id VARCHAR(255) NOT NULL,up_name VARCHAR(255) NOT NULL, ' \
          'sex VARCHAR(10) NOT NULL, birthday VARCHAR(255),' \
          'focus VARCHAR(255),fans VARCHAR(255),area VARCHAR(255),' \
          'praise VARCHAR(255),view VARCHAR(255),' \
          'sign VARCHAR(255) NOT NULL,title VARCHAR(255) NOT NULL,' \
          'PRIMARY KEY (id,up_id))'
    cursor.execute(sql)
    db.close()
    db = pymysql.connect(host='localhost', user='root', password='',
                         port=3306, db='bilibili')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS fans (id int(11) NOT NULL AUTO_INCREMENT,' \
          'up_id VARCHAR(255) NOT NULL,fans_id VARCHAR(255) NOT NULL,' \
          'fans_name VARCHAR(255) NOT NULL, sex VARCHAR(10) NOT NULL,' \
          'fans_level VARCHAR(10) NOT NULL,viplevel VARCHAR(255) NOT NULL,' \
          'time VARCHAR(255) NOT NULL,' \
          'PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()

def insertUp(mid,name,sex,sign,birthday,title):
    db = pymysql.connect(host ='localhost', user='root', password ='',
                         port=3306, db='bilibili')
    cursor = db.cursor()
    sql = 'INSERT INTO up(up_id,up_name,sex,sign,birthday,title) values(%s,%s,%s,%s,%s,%s)'
    val = (mid,name,sex,sign,birthday,title)
    try :
        cursor.execute (sql, val)
        db.commit()
    except:
        db. rollback ()
    db.close()


def insertFans(up_mid,fans_mid, time, uname, viplevel, sex, level):
    db = pymysql.connect(host='localhost', user='root', password='',
                         port=3306, db='bilibili')
    cursor = db.cursor()
    sql = 'INSERT INTO fans(up_id,fans_id,fans_name,sex,fans_level,viplevel,time) values(%s,%s,%s,%s,%s,%s,%s)'
    val = (up_mid, fans_mid, uname, sex, level, viplevel, time)
    try:
        cursor.execute(sql, val)
        db.commit()
    except:
        db.rollback()
    db.close()

def getPage(mid,n,href):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Referer': href+'/fans/fans',
    }
    params = (
        ('vmid', str(mid)),
        ('pn', str(n)),
        ('ps', '50'),
        ('order', 'desc'),
    )
    response = requests.get('https://api.bilibili.com/x/relation/followers', headers=headers, params=params)
    return response

def getUserDetails(mid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Origin': 'https://space.bilibili.com',
        'Connection': 'keep-alive',
        'Referer': 'https://space.bilibili.com/546195/fans/fans',
        'Cache-Control': 'max-age=0',
    }
    params = (
        ('mid', str(mid)),
        ('jsonp', 'jsonp'),
    )
    response = requests.get('https://api.bilibili.com/x/space/acc/info', headers=headers, params=params)
    return response

def getUpInfoBySelenium(href, mid):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
    opt = webdriver.FirefoxOptions()
    opt.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Firefox(options=opt)
    try:
        driver.get('https:' + href+'/video')
        html = driver.execute_script("return document.documentElement.outerHTML")  # 必须执行js
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        focus = soup.find('p', 'n-data-v space-attention').text  # 关注数
        fans = soup.find('p', 'n-data-v space-fans').text  # 粉丝数
        div = soup.find('div', 'n-statistics')
        praise = div.contents[2].find('p', 'n-data-v').text  # 获赞数
        view = div.contents[3].find('p', 'n-data-v').text  # 播放数
        div = soup.find('div', id='submit-video-type-filter') #分区
        a = div.find_all('a', attrs={'class': ''})
        dict = {}
        for each in a:
            lstrip = each.text.lstrip()
            dict[lstrip[0:2]] = int(lstrip[2:])
        maxArea = max(zip(dict.values(), dict.keys()))
        print("关注数" + str(focus), "粉丝数" + str(fans), "获赞数" + str(praise),
              "播放数：" + str(view),"主分区：" + maxArea[1] + "区")
        db = pymysql.connect(host='localhost', user='root', password='',
                             port=3306, db='bilibili')
        cursor = db.cursor()
        sql = 'UPDATE up SET focus = %s,fans =%s,praise =%s,view =%s,area =%s WHERE up_id = %s'
        val = (focus[:-1], fans[:-1], praise[:-1], view[:-1], maxArea[1], mid)
        try:
            cursor.execute(sql, val)
            db.commit()
        except:
            db.rollback()
        db.close();
    finally:
        driver.close()

def viplevel(vip):
    if vip == 0:
        vipname = '非会员'
    elif vip == 1:
        vipname = '会员'
    else:
        vipname = '大会员'
    return vipname

response = requests.get('https://www.kanbilibili.com/rank/ups/fans')
soup = BeautifulSoup(response.text, 'html.parser')
a = soup.find('div', 'ups-list').find_all('a', limit=3)
createDb()
for each in a:
    href = str(each.get('href')) # 每个up主个人空间
    up = getUserDetails(href.lstrip()[21:]) #获取up主个人信息(json)
    json_obj = json.loads(up.text)
    up_mid = json_obj['data']['mid']
    name = json_obj['data']['name']
    sex = json_obj['data']['sex']
    sign = json_obj['data']['sign']
    level = json_obj['data']['level']
    birthday = json_obj['data']['birthday']
    title = json_obj['data']['official']['title']
    print("up主uid："+str(up_mid),"用户名："+name,"性别："+sex,
          "留言："+sign,"生日："+birthday,"称号："+title)
    insertUp(str(up_mid),name,sex,sign,birthday,title)
    getUpInfoBySelenium(href,str(up_mid)) # 打印粉丝数、播放数、分区等(selenium)
    print("Ta的粉丝：")
    print("----------------")
    for i in range(1, 5):
        r = getPage(href.lstrip()[21:],i,href);
        json_obj = json.loads(r.text); #返回json格式
        for entry in json_obj['data']['list']:
            fans_mid = entry['mid']
            mtime = entry['mtime']
            uname = entry['uname']
            vip = entry['vip']['vipType']
            fansDetails = getUserDetails(fans_mid)
            json_obj = json.loads(fansDetails.text)
            sex = json_obj['data']['sex']
            level = json_obj['data']['level']
            print("uid：" + str(fans_mid), "关注时间："+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime)),
                               "用户名：" + uname, "vip等级：" + viplevel(vip), "性别："+sex, "账户等级："+str(level))
            insertFans(str(up_mid),str(fans_mid), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime)),
                       uname,viplevel(vip),sex,str(level))
        time.sleep(5) # 防止封ip
    print("----------------")