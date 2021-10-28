#-*-coding:utf-8-*-

from __future__ import division
import time,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from readConfig import get_ini


# 选择驱动打开浏览器
def chose_driver():
    try:
        # options = webdriver.ChromeOptions()
        chrome_options = Options()
        #options.set_headless()  # 设置启动无界面化
        # chrome中加入配置参数
        global driver
        chrome_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=chrome_options,executable_path=os.getcwd()+"\\chromedriver.exe")
        # options.add_argument('--ignore-certificate-errors')
        # driver = webdriver.Chrome(chrome_options=options)
        driver.maximize_window()
        return driver
    except Exception as e:
        raise e


# 判断元素是否存在
def isElementPresent(pelement, by, value):
    """
    用来判断元素标签是否存在，
    """
    try:
        element = pelement.driver.find_element(by=by, value=value)

    # 原文是except NoSuchElementException, e:
    except NoSuchElementException as e:
        # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
        #print("1")
        return False

    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        #print("2")
        return True

def isElementExist(driver,element):
    flag=True
    # driver=self.driver
    try:
        # driver.find_element_by_css_selector(element)
            WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,element))
            return flag
    except:
            flag = False
            return flag



#登录
def login():
    driver = chose_driver()
    url = get_ini("AUTOINFO","url")
    driver.get(url)
    try:
        time.sleep(2)
        # WebDriverWait(driver, 10).until(EC.visibility_of(
        #     driver.find_element(by=By.XPATH, value='//*[@id="userAccount"]'))).clear()
        driver.close()
        return True

    except Exception as e:
        driver.close()
        raise e