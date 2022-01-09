# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/5 17:48
#自动化测试用代码是测试代码
#webUI，APPUI,接口自动化测试
"""
Selenium/QTP/uft:web测试
Appnium/airtest/Monkey/MonkeyRunner:App自动化测试
jmeter/Postman/soapUi:接口测试
loadrunner:性能测试
jenkins:持续测试
"""
import os
from selenium.webdriver.common.by import By
from pathlib import Path#pathlib：路径处理库
from time import sleep
from selenium import webdriver
#导入键盘模块Keys
from selenium.webdriver.common.keys import Keys
#鼠标模块
from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()#C要大写！ 通过Chrome浏览器打开浏览器
#Chorme哪里来的? --在webdriver中__init__.py中有定义from .chrome.webdriver import WebDriver as Chrome
#所以from selenium import webdriver其实等同于
#from selenium.webdriver.chrome.webdriver import WebDriver as Chrome ---可读性差
# driver.get(os.getcwd()+r'\test.html')#打开刚才我们自己写的html文件
# driver.find_element('username').send_keys('小鹏长翅')
# driver = webdriver.Chrome()#打开chrome浏览器
# html = Path('./test.html')
# driver.get(str(html.resolve()))#Path.resolve:该方法将一些的 路径/路径段 解析为绝对路径
# print(str(html.resolve()))
#第二种转为绝对路径的方法
# html = os.path.abspath('./test.html')#返回绝对路径
# driver = webdriver.Chrome()
# driver.get(html)
# os.getcwd('www.baidu.com')
#优雅的打开浏览器
# with webdriver.Chrome() as driver:#with上下文管理器，不需要我去关闭
#     driver.get('https://www.baidu.com')#打开百度
#     sleep(5)#等5秒，自动关闭
#定位元素
#祖宗方法
# find_element
# #通过class属性的值定位(底层是css)
# find_element_by_class_name
# #√√√通过css 选择器定位(推荐，最快)
# find_element
# #√通过id的值定位(底层是css)
# find_element_by_id
# #√通过a标签的文本定位(底层是XPATH)
# find_element_by_link_text
# #通过name属性的值来定位(底层是css)
# find_element_by_name
# #通过a标签的部分文本定位（模糊匹配）(底层是XPATH)
# find_element_by_partial_link_text
# #通过标签名来定位(底层是css)
# find_element_by_tag_name
# #√√通过xpath方法定位(慢)
# find_element_by_xpath
#以下方法的用法同上，只是返回的是一组元素（列表形式）
# find_elements
# find_elements_by_class_name
# find_elements_by_css_selector
# find_elements_by_id
# find_elements_by_link_text
# find_elements_by_name
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_xpath
# https://www.w3school.com.cn/tags/html_ref_standardattributes.asp
# 通过name属性的值来定位
# 1.如果遇到重复的元素，操作的永远是第一个
# 2.send_keys方法，不会清空原来的内容
# with webdriver.Chrome() as driver:#打开chrome浏览器
#     html = Path('./test.html')
#     driver.get(str(html.resolve()))#Path.resolve:该方法将一些的 路径/路径段 解析为绝对路径
#     driver.find_element(By.NAME,'username').send_keys('admin')#在这个元素里写入值
#     #找到name的值为'username'的标签，并输入'admin'
#     sleep(5)#5秒后关闭
# 通过id的值定位
# 1.id是唯一的
# 2.可能会变，需要注意识别
# 3.首字符是数字的要注意css的表达式（后续详细介绍）
# with webdriver.Chrome() as driver:
#     html = os.path.abspath('./test.html')#获取绝对路径
#     driver.get(html)
#     driver.find_element(By.ID,'username').send_keys('admin')
#     #找到id的值为'username'的标签，并输入'admin'
#     sleep(5)
# 通过class属性的值定位
# 1.class也容易重复
# 2.class ='bb cc'规定元素的一个或多个类名，等同于class1,class2='bb','cc'
# 所以不能直接用driver.find_element_by_class_name('bb cc')
# with webdriver.Chrome() as driver:
#     html = os.path.abspath('./test.html')#获取绝对路径
#     driver.get(html)
#     # 1. 输入用户名
#     driver.find_element(By.CLASS_NAME,'aa').send_keys('admin')
#     #找到class的值为'aa'的标签，并输入'admin'
#     # 2. 输入密码
#     # driver.find_element_by_class_name('bb cc').send_keys('123456')--错误写法
#     driver.find_element(By.CLASS_NAME,'bb').send_keys('pass')
#     #找到class的值为'bb'的标签，输入'pass'
#     # driver.find_element(By.CLASS_NAME,'cc').send_keys('word')
#     #找到class的值为'cc'的标签，输入'word'
#     sleep(5)

# 通过a标签的部分文本定位（模糊匹配）
# 1.link_text 的两种定位方式只适用于a标签的文本
# 2.link_text 完全匹配
# 3.parti_link_text  部分（模糊）可以是开头是、包含、结尾是
# with webdriver.Chrome() as driver:
#     html = os.path.abspath('./test.html')#获取绝对路径
#     driver.get(html)
#     driver.find_element(By.PARTIAL_LINK_TEXT,'必应').click()
#     #找到包含'必应'文本的a标签，并点击
#     sleep(5)#等待5秒关闭

# XPath是XML的路径语言，通俗一点讲就是通过元素的路径来查找到这个标签元素
# XPath使用路径表达式在XML文档中进行导航
# https://www.w3school.com.cn/xpath/index.asp
# 1.xpath中的值用引号引起来时，在代码中要注意区分，内单外双，内双外单。
# 2.xapth的class的值要填写全部，注意与find_element_by_class_name的区别。
# 3.xpath还支持逻辑运算符and/or，多用and来缩小范围，例如//*[@id='username' and @type='text']
# 4.要注意xpath中//input[1]代表第一个input标签，而不是用0，与python中的下标索引不同

# xpath轴语法
# ancestor#选取当前节点的所有先辈（父、祖父等）。
# ancestor-or-self#选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
# attribute#选取当前节点的所有属性。
# child#选取当前节点的所有子元素。
# descendant#选取当前节点的所有后代元素（子、孙等）。
# descendant-or-self#选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
# following#选取文档中当前节点的结束标签之后的所有节点。
# namespace#选取当前节点的所有命名空间节点。
# parent#选取当前节点的父节点。
# preceding#选取文档中当前节点的开始标签之前的所有节点。
# preceding-sibling#选取当前节点之前的所有同级节点。
# self#选取当前节点。

# 1.打开微博官网
# 2.找到热搜榜按钮位置，并点击
# 3.找到热搜标题位置，获得文本
# driver = webdriver.Chrome()#打开浏览器
# url = 'https://weibo.com'
# driver.get(url)#打开微博官网
# sleep(5)
# driver.find_element(By.XPATH,"//*[@title='热搜榜']").click()#找到热搜榜并点击
# for i in range(2,7):
#     sleep(1)
#     print(f'此时此刻热搜第{i-1}名为：'+driver.find_element(By.XPATH, f"//main/div//div[{i}]//*[starts-with(@class,'HotTopic_tit_')]").text)

# # 再整一下豆瓣的电影排行榜
# driver = webdriver.Chrome()
# url = 'https:/douban.com'
# driver.get(url)
# driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/ul/li[2]/a').click()
# #这用的完整的绝对路径
# sleep(5)
# driver.find_element(By.XPATH,"//div/ul/li/a[text()='排行榜']").click()
# #找规律精简后的路径
# for i in range(1,11):
#     sleep(2)
#     print(f'豆瓣排行榜第{i}名：'+driver.find_element(By.XPATH,f'//table[{i}]//a[@class=""]').text)

# webUI的自动化元素定位是分析网页的一个过程
# 绝对路径不稳定，基本不用，前边随便一个爷爷变了，孙子就找不到了。
# 学习时先在浏览器的F12调试界面多试，确定好后再复制到代码里
# 路径法和属性法要结合使用，找到定位元素最准确且精简路径
# 属性值和网址这些东西，能复制尽量不要手敲
# 刚开始学不要过度使用‘复制Xptah’，还是要先会写，再复制。
# 根据基础用法实在定位不到元素，还有轴定位（要能想起来）。

#通过css定位
# driver = webdriver.Chrome()
# url = 'https://www.douban.com/'#打开豆瓣官网
# driver.get(url)
# css1 = 'a.lnk-music'#音乐按钮位置
# css2 = '#db-nav-music ul>li:nth-child(3)>a'#排行榜按钮位置
# driver.find_element(By.CSS_SELECTOR,css1).click()#点击音乐按钮
# a=driver.window_handles#返回一个window列表
# #第一步点击音乐按钮，打开了新的window，所以要切换下
# driver.switch_to.window(a[1])#切换到新打开的window
# driver.find_element(By.CSS_SELECTOR,css2).click()#点击排行榜按钮
# sleep(2)
# for i in range(1,11):
#     css3 = f'.col5>li:nth-child({i}) a:nth-child(1)'
#     print(f'排行榜第{i}名：'+driver.find_element(By.CSS_SELECTOR,css3).text)
#     sleep(1)


# webdriver常用方法
# back  #浏览器后退
# close #关闭tab页，不关闭driver.exe
# quit#退出浏览器，关闭driver.exe
# current_url#当前的url地址
# execute_script#执行js脚本
# forward#前进
# fullscreen_window#全屏
# get#打开指定url
# get_window_rect#得到窗口的矩形
# get_window_position#得到窗口的位置
# get_window_size#得到窗口的大小
# maximize_window#最大化窗口
# minimize_window#最小化窗口
# name#浏览器名字
# page_source#页面源代码
# refresh#刷新页面
# save_screenshot#保存界面截图，建议为png格式
# set_window_pisition#设置窗口位置
# set_window_rect#设置窗口矩形
# set_window_size#设置窗口大小
# title#浏览器当前页的标题

# with webdriver.Chrome() as driver:
#
#     #打开豆瓣电影
#     driver.get('https://movie.douban.com/')
#     #点击排行榜按钮，进入排行榜页面
#     driver.find_element(By.XPATH,'//*[@id="db-nav-movie"]//a[text()="排行榜"]').click()
#     #查看当前页面的标题
#     print('点击排行榜后的页面标题为：'+driver.title)
#     sleep(2)
#     #返回豆瓣电影页
#     driver.back()
#     sleep(2)
#     #查看当前页面的标题
#     print('返回后的页面标题为：'+driver.title)
#     sleep(2)
#     #设置窗口大小
#     driver.set_window_size(800,200)
#     sleep(2)
#     #打印窗口大小
#     print('设置完后的窗口大小为：'+str(driver.get_window_size()))
#     sleep(2)
#     #打印窗口的矩形
#     print('当前的窗口矩形为：'+str(driver.get_window_rect()))
#     sleep(2)
#     #打印当前的url
#     print('当前页面url为：'+str(driver.current_url))
#     sleep(2)
#     #打印浏览器名称
#     print('浏览器名称为：'+str(driver.name))
#     sleep(2)
#     now_html = driver.page_source#获取当前页面源代码
#     with open(r'./htm1.html','w+',encoding='utf-8') as fi:
#         fi.write(now_html)#把当前页面源代码写入到文件
#     #退出浏览器
#     driver.quit()
#
# webelement对象方法
# clear#清空元素上的内容
# click#点击元素
# find_element#在元素上找元素
# get_attribute#获得属性
# is_display#是否显示
# is_enable#是否使能
# is_selected#是否选择
# location#位置
# rect#矩形
# screenshot_as_png#元素存为png图片，bytes类型，可用于验证码
# send_keys#输入信息（追加）
# size#大小
# submit#提交
# tag_name#标签名
# text#文本
# location_once_scrolled_into_view#滚动到可见
# value_of_css_property#css属性的值

#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# sleep(2)
# #先找到搜索栏#再在搜索栏元素上找另外一个元素（小相机按钮）并点击
# driver.find_element(By.CSS_SELECTOR,'.bg.s_ipt_wr.new-pmd.quickdelete-wrap').find_element(By.CSS_SELECTOR,'.soutu-btn').click()
# sleep(2)
# #点击X按钮
# driver.find_element(By.CSS_SELECTOR,'a.soutu-close.c-icon.soutu-close-new').click()
# #在百度搜索栏输入内容
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('zhouyi')
# sleep(1)
# #点击确定按钮
# driver.find_element(By.CSS_SELECTOR,'#su').click()
# sleep(1)
# # 找到‘下一页’按钮
# ele = driver.find_element(By.CSS_SELECTOR, '#page > div > a.n')
# sleep(1)
# # 滑动到页面最底部，使‘下一页按钮’可见
# ele.location_once_scrolled_into_view
# for i in range(10):
#     ele.click()
# sleep(1)
# #返回上一页面
# driver.back()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('小鹏长翅')
# #清空输入框内容
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#kw').clear()
# sleep(1)
# size = driver.find_element(By.CSS_SELECTOR,'#su').size
# #查看‘百度一下’按钮大小
# print('"百度一下"按钮的大小为:'+str(size))
# tag_name=driver.find_element(By.CSS_SELECTOR,'#su').tag_name
# #查看‘百度一下’按钮的标签名
# print('"百度一下"按钮的标签名为:'+str(tag_name))
# #打印网页上的文字‘请按“回车”键发起检索’
# print(driver.find_element(By.CSS_SELECTOR,'#ent_sug').text)
# driver.set_window_size(500,500)
# driver.quit()

# 键盘模块
# 1、仍然使用send_keys发送按键
# 2、selenium有专门的Keys模块进行键盘操作
# 3、组合键的发送用Keys.control,'A'(复制)
# 4、按键不区分大小写
# 5、连续按键可以用"*n"
# 我们先看下类Keys下面有哪些按键，输入Keys，然后按住ctrl点击
# 按键名:对应值
# 所以进行按键操作时，有两种方式
# 1.Keys.按键名
# 2.直接输入按键对应的值

# 自己想个需求：
# 1.打开必应官网
# 2.在国内版搜索框输入‘小鹏长翅公众号’并复制
# 3.切换到国际版
# 4.在国际版搜索框粘贴
# 5.删除‘公众号’并按回车键进行搜索


# driver = webdriver.Chrome()
# #1.打开必应官网
# driver.get('https://cn.bing.com/')
# #2.在国内版搜索框输入‘小鹏长翅公众号’
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#sb_form_q').send_keys('小鹏长翅公众号')
# #复制文本
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#sb_form_q').send_keys(Keys.CONTROL,'A')#全选
# driver.find_element(By.CSS_SELECTOR,'#sb_form_q').send_keys(Keys.CONTROL,'C')#复制
# #3.切换到国际版
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#est_en').click()
# #4.在国际版搜索框粘贴
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#sb_form_q').send_keys('\ue009','V')#Keys.CONTROL = '\ue009'
# #5.删除‘公众号’三个字--BACKSPACE*3
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#sb_form_q').send_keys(Keys.BACKSPACE*3)
# #6.按回车键进行搜索
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#sb_form_q').send_keys(Keys.ENTER)

# #右键
# context_click(self, on_element=None)
# #双击
# double_click(self,on_element=None)
# #左键
# click(self,on_element=None)
# #鼠标移动到某个元素
# move_to_element(self,to_element=None)
# #按住左键不放
# click_and_hold(self,on_element=None)
# #拖拽到某个元素然后松开
# drag_and_drop(self,soure,target)
# #拖拽到某个坐标然后松开
# drag_and_drop_by_offset(self,source,xoffset,yoffset)
# #按下某个键
# key_down(self,value,element=None)
# #松开某个键
# key_up(self,value,element=None)
# #鼠标从当前位置移动到某个坐标
# move_by_offset(self,xoffset,yoffset)
# #移动到距某个元素（左上角坐标）多少的位置
# move_to_element_with_offset(self, to_element, xoffset, yoffset)
# #在某个元素位置松开鼠标左键
# release(self,on_element=None)
# #发送某个键到当前焦点的元素
# send_keys(self,*keys_to_send)
# #发送某个键到指定元素
# send_keys_to_element(self,element,*keys_to_send)

# 两种用法：
# 1.链式调用
# ActionChains(driver).动作1.动作2.perform()  #perform执行动作
# 2.分步执行
# my_action =ActionChains(driver)
# my_action.动作1
# my_action.动作2
# my_action.perform()

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')#打开百度
# driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('小鹏长翅')#搜索栏输入‘小鹏长翅’
# my_action = ActionChains(driver)
# ele1 = driver.find_element(By.CSS_SELECTOR,'#su')#找到‘百度一下’按钮
# my_action.move_to_element(ele1).perform()#鼠标移动到‘百度一下’
# my_action.click()#点击
# my_action.perform()
# sleep(1)
# driver.back()#返回上一页
# sleep(1)
# ele2 = driver.find_element(By.CSS_SELECTOR,'#s-top-left>div>a')#找到‘更多’按钮
# my_action1 = ActionChains(driver)
# my_action1.move_to_element(ele2)#鼠标移动到‘更多按钮’
# my_action1.perform()

# 认识JavaScript（JS）
#     JavaScript是运行在浏览器上的脚本语言，简称JS。
#     JavaScript和java没有任何关系，只是语法类似。
#     JS本身和selenium无关。
#     通过selenium执行JS代码可以让我们的操作更加丰富，理论上一个HTML的所有行为都可以通过JS来控制
#     selenium中常用JS的基础语法和DOM操作
# 学习地址：https://www.w3school.com.cn/js/js_htmldom.asp

driver = webdriver.Chrome()   
#1.打开豆瓣官网
driver.get('https://www.douban.com/')
sleep(2)
#2.返回网页的title和url
title = 'return document.title'#return不能少
url = 'return document.URL'
print('网页标题：'+driver.execute_script(title))
print('网页地址：'+driver.execute_script(url))
#3.滑动到网页右下角
x = 'return document.body.scrollWidth'
X = driver.execute_script(x)#获取网页最大宽度
y = 'return document.body.scrollHeight'
Y = driver.execute_script(y)#获取网页最大高度
driver.execute_script(f'window.scrollTo({X},{Y})')
sleep(2)
#4.找到搜索框，并滑动到按钮可见
ele1 = driver.find_element(By.CSS_SELECTOR,"#anony-nav input[name='q']")
driver.execute_script('arguments[0].scrollIntoView()',ele1)
#此处的arguments[0]等于ele1
sleep(2)
#5.修改搜索框的placeholder属性
#先找到搜索框
ele2 = 'ele=document.querySelector("#anony-nav>div.anony-srh>form>span.inp>input[type=text]")'
#修改placeholder的值
js1 = 'ele.placeholder="小鹏长翅"'
driver.execute_script(ele2)
driver.execute_script(js1)
sleep(2)
#6.移除属性
#直接移除搜索框的placeholder属性
driver.execute_script("ele.removeAttribute('placeholder')")
