# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import pandas as pd

executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"

# def get_html_page(url):
#    try:
#        driver = webdriver.Chrome(executable_path=executable_path)
#        driver.get("https://www.hezongyy.com/auth/login")
#        time.sleep(2)
#        username = driver.find_element_by_name('user_name')
#        password = driver.find_element_by_name('password')
#        username.send_keys('测试05')
#        password.send_keys('123456')
#        # 模拟点击“登录”按钮
#        driver.find_element_by_class_name('login').click()
#        time.sleep(1)
#        driver.get(url)
#        time.sleep(3)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
#        html_sourcode = driver.page_source
#        driver.close()
#        return html_sourcode
#    except Exception as e:
#        print(e)
#
# def crawl_page(url):
#     html_doc = get_html_page(url)
#     soup = BeautifulSoup(html_doc, 'lxml')

driver = webdriver.Chrome(executable_path=executable_path)
driver.get("https://www.hezongyy.com/auth/login")
time.sleep(2)
username = driver.find_element_by_name('user_name')
password = driver.find_element_by_name('password')
username.send_keys('测试05')
password.send_keys('123456')
# 模拟点击“登录”按钮
driver.find_element_by_class_name('login').click()
time.sleep(1)
driver.get("https://www.hezongyy.com/puyao.html")
time.sleep(3)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
html_sourcode = driver.page_source
driver.close()
soup = BeautifulSoup(html_sourcode, 'lxml')
# jg = soup.find_all(attrs={'class': {'datu-jiage'}})
jg = soup.find_all(class_="datu-jiage")
mz = soup.find_all(class_="datu-mingzi")
list1 = []
for i in jg:
    list1.append(i.text)
list2 = []
for t in mz:
    list2.append(t.text)
dataframe = pd.DataFrame({'a_name': list1, 'b_name': list2})  # 字典中的key值即为csv中列名
dataframe.to_csv("test-01.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True






