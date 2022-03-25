import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.Login import Login
from pages.config import config


class BasePage:
    _baseurl = 'https://ipark-sit.bgy.com.cn/welcome'

    def __init__(self, driver=None, op=1):
        self._baseurl = config.get("home-page")
        """
        初始化启动浏览器
        :param driver: 解决继承的子类重复初始化打开浏览器问题
        :param op: 0为复用流量器启动driver,1为打开新的浏览器复用旧的cookie
        """
        if driver is None:
            if op == 0:
                self.driver = self.options_chrome()
            elif op == 1:
                self.driver = self.cookie_chrome()
        else:
            self.driver: WebDriver = driver
        time.sleep(3)  # 新打开一个页面强制等待3秒
        # Login().login(self.driver)  # 将登录后的cookie写进cookie.yml
        Login().inner_login(self.driver)  # 将登录后的cookie写进cookie.yml
        # Login().set_login_cookie(self.driver.get_cookies())  # 将登录后的cookie写进cookie.yml
        self.driver.implicitly_wait(10)  # 设置隐式断言10秒

    def options_chrome(self):
        """复用浏览器"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self._baseurl)
        return self.driver

    def cookie_chrome(self):
        """读取cookie复用登录状态"""
        self.driver = webdriver.Chrome()
        self.driver.get(self._baseurl)  # 打开首页
        # cookie = Login().get_login_cookie()
        # if cookie is not None:
        #     cookies = self.driver.get_cookies()
        #     print(cookies)
        #     for e in cookie:
        #         print(e)
        #         self.driver.add_cookie(e)  # 将cookie添加到打开的浏览器中
        # self.driver.refresh()  # 刷新浏览器
        return self.driver

    def my_locator(self, by, locator=None):
        """
        封装元素为止传参,使可兼容多种传参
        :param by: css,id,xpath,class_name,link_text,partial_link_text,tag_name
        :param locator:
        :return:
        """
        if locator is None:
            by, value = by[0], by[1]
        else:
            by, value = by, locator

        if by.upper() == 'CSS':
            by = By.CSS_SELECTOR
        elif by.upper() == 'ID':
            by = By.ID
        elif by.upper() == 'XPATH':
            by = By.XPATH
        elif by.upper() == 'CLASS_NAME':
            by = By.CLASS_NAME
        elif by.upper() == 'LINK_TEXT':
            by = By.LINK_TEXT
        elif by.upper() == 'PARTIAL_LINK_TEXT':
            by = By.PARTIAL_LINK_TEXT
        elif by.upper() == 'TAG_NAME':
            by = By.TAG_NAME
        else:
            by = by
        return by, value

    def find_ele(self, by, locator=None):
        """
        查找元素,支持传(By.type, value),也支持传入By.type, value;
        :param by: css,id,xpath,class_name,link_text,partial_link_text,tag_name
        :param locator:
        :return:
        """
        if locator is None:
            by, value = by[0], by[1]
        else:
            by, value = by, locator

        if by.upper() == 'CSS':
            by = By.CSS_SELECTOR
        elif by.upper() == 'ID':
            by = By.ID
        elif by.upper() == 'XPATH':
            by = By.XPATH
        elif by.upper() == 'CLASS_NAME':
            by = By.CLASS_NAME
        elif by.upper() == 'LINK_TEXT':
            by = By.LINK_TEXT
        elif by.upper() == 'PARTIAL_LINK_TEXT':
            by = By.PARTIAL_LINK_TEXT
        elif by.upper() == 'TAG_NAME':
            by = By.TAG_NAME
        else:
            by = by
        self.wait_clickable(by, value)
        return self.driver.find_element(by, value)

    def find_ele_list(self, by, locator=None):
        """
        查找元素,支持传(By.type, value),也支持传入By.type, value;
        :param by: css,id,xpath,class_name,link_text,partial_link_text,tag_name
        :param locator:
        :return:
        """
        if locator is None:
            by, value = by[0], by[1]
        else:
            by, value = by, locator

        if by.upper() == 'CSS':
            by = By.CSS_SELECTOR
        elif by.upper() == 'ID':
            by = By.ID
        elif by.upper() == 'XPATH':
            by = By.XPATH
        elif by.upper() == 'CLASS_NAME':
            by = By.CLASS_NAME
        elif by.upper() == 'LINK_TEXT':
            by = By.LINK_TEXT
        elif by.upper() == 'PARTIAL_LINK_TEXT':
            by = By.PARTIAL_LINK_TEXT
        elif by.upper() == 'TAG_NAME':
            by = By.TAG_NAME
        else:
            by = by
        return self.driver.find_elements(by, value)

    def wait_clickable(self, by, locator=None, time=30):
        """
        显式等待
        :param by:css,id,xpath,class_name,link_text,partial_link_text,tag_name
        :param locator: 等待元素可点击为止,这里需要传入元素的locator
        :param time: 等待时间
        :return:
        """
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(self.my_locator(by, locator)))

    def wait_visibility(self, by, locator=None, time=30):
        """
        显式等待
        :param by: css,id,xpath,class_name,link_text,partial_link_text,tag_name
        :param locator: 等待元素可见为止,这里需要传入元素的locator
        :param time: 等待时间
        :return:
        """
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(self.my_locator(by, locator)))

    def ele_click(self, by, locator=None):
        """
        点击元素,支持传(By.type, value),也支持传入By.type, value;
        :param by: css,id,xpath,class_name,link_text,partial_link_text,tag_name
        :param locator:
        :return:
        """
        self.find_ele(by, locator=locator).click()

    @property
    def baseurl(self):
        return self._baseurl

