# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/9 21:22
import json
from selenium import webdriver
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
opt = webdriver.FirefoxOptions()
opt.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Firefox(options=opt)
url ="https://passport.bilibili.com/ajax/miniLogin/minilogin"
driver.get(url)
with open('cookies.txt', 'r') as cookief:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)
    for cookie in cookieslist:
        driver.add_cookie(cookie)
driver.get("https://space.bilibili.com/116683")
driver.refresh()