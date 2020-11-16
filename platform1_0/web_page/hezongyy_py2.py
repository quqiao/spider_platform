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
    driver.get("https://www.hezongyy.com/#/login")
    time.sleep(2)
    username = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/form/div[1]/div/div[1]/input')
    password = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input')
    username.send_keys('测试05')
    password.send_keys('a123456')
    # 模拟点击“登录”按钮
    driver.find_element_by_class_name('el-button.el-button--primary').click()
    time.sleep(1)
    driver.get("https://www.hezongyy.com/#/puyaoList")
    time.sleep(5)
    html_sourcode = driver.page_source
    # html = etree.parse(html_sourcode)
    html = etree.HTML(html_sourcode, etree.HTMLParser())
    for i in range(1, 41):
        jg = html.xpath('//*[@id="app"]/div/div[7]/div[2]/div[3]/ul[1]/li[%d]/div/div/div[3]/span/text()' % i)
        jg1 = ''.join(jg)
        list_jiage.append(jg1)
    # print(list_jiage)
    for j in range(1, 41):
        mz = html.xpath('//*[@id="app"]/div/div[7]/div[2]/div[3]/ul[1]/li[%d]/div/div/p[2]/text()' % j)
        mz1 = ''.join(mz)
        list_mingzi.append(mz1)
    # print(list_mingzi)
    driver.close()

def save_csv():
    # dataframe = pd.DataFrame({'价格': list_jiage, '名字': list_mingzi})  # 字典中的key值即为csv中列名
    # dataframe.to_csv("hezongyy_20201111.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True
    data = {'价格': list_jiage, '名字': list_mingzi}
    dataframe = pd.DataFrame(data, columns=['价格', '名字'])
    print(dataframe)
    dataframe.to_excel("hezongyy_20201111.xls", encoding='utf-8', index=False, header=True)

if __name__ == '__main__':  # 验证拼接后的正确性
    crawl_hezongyy()
    save_csv()