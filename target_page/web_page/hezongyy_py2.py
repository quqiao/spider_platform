# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import pandas as pd
import pymysql
from lxml import etree

list_jiage = []
list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []

def crawl_hezongyy():
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
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
    time.sleep(5)
    html_sourcode = driver.page_source
    # html = etree.parse(html_sourcode)
    html = etree.HTML(html_sourcode, etree.HTMLParser())
    for i in range(1, 41):
        jg = html.xpath('//*[@id="datu"]/div/ul/li[%d]/div[2]/div/text()' %i)
        print(jg)
        list_jiage.append(jg)
    print(list_jiage)
    # soup = BeautifulSoup(html_sourcode, 'lxml')
    # all1 = soup.find_all(["li", "div"])
    # print(all1)

def save_csv():
    dataframe = pd.DataFrame({'价格': list_jiage})  # 字典中的key值即为csv中列名
    dataframe.to_csv("test-02.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

if __name__ == '__main__':  # 验证拼接后的正确性
    crawl_hezongyy()
    save_csv()