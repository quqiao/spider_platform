# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import pandas as pd
import pymysql

list_jiage = []
list_mingzi = []
list_compamy = []
list_xiaoqi = []

def clear_list():
    list_jiage.clear()
    list_mingzi.clear()
    list_compamy.clear()
    list_xiaoqi.clear()

def crawl_ysb_lyg(count):
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://dian.ysbang.cn/index.html#/login")
    time.sleep(2)
    username = driver.find_element_by_id('userAccount')
    password = driver.find_element_by_id('password')
    username.send_keys('13518134160')
    password.send_keys('yxs78311')
    # 模拟点击“登录”按钮
    time.sleep(10)
    driver.find_element_by_id('loginBtn').click()
    time.sleep(5)
    driver.get("https://dian.ysbang.cn/index.html#/supplierstore?providerId=2758")
    time.sleep(5)
    # driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]').click()
    driver.find_element_by_class_name('provider-tab active')  # 全部商品
    time.sleep(5)
    for i in range(1, count+1):
        time.sleep(3)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
        html_sourcode = driver.page_source
        soup = BeautifulSoup(html_sourcode, 'lxml')
        # jg = soup.find_all(attrs={'class': {'datu-jiage'}})
        jg = soup.find_all(class_="price-wrap")
        mz = soup.find_all(class_="title-row")
        cj = soup.find_all(class_="factory-row")
        xq = soup.find_all(class_="validate-date")
        # for y in jg:
        #     list_jiage.append(y.text)
        # for t in mz:
        #     list_mingzi.append(t.text)
        for j in cj:
            list_compamy.append(j.text)
        for x in xq:
            list_xiaoqi.append(x.text)
        time.sleep(5)
        driver.find_element_by_class_name("pagination-next").click()
    driver.close()


def save_csv():
    dataframe = pd.DataFrame({'厂家': list_compamy, '效期': list_xiaoqi})  # 字典中的key值即为csv中列名
    dataframe.to_csv("test-ysb_lyg.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

def save_mysql():
    conn = pymysql.connect('localhost', 'root', '123456', 'spider_platform')  # 有中文要存入数据库的话要加charset='utf8'
    # 创建游标
    cursor = conn.cursor()  # pymysql.cursors.DictCursor
    cursor.execute("DROP TABLE IF EXISTS ysb_lyg")
    # 使用预处理语句创建表
    sql = """
          CREATE TABLE ysb_lyg 
          (
             ID int unsigned auto_increment primary key,
             name VARCHAR(100),
             cj VARCHAR(100),
             gg VARCHAR(100),
             price VARCHAR(100)
          )
          """
    cursor.execute(sql)
    insert_sql = """
                 insert into ysb_lyg 
                 (name,cj,gg,price) 
                 VALUES
                 (%s,%s,%s,%s)
                 """
    for i in range(len(list_jiage)):
        cursor.execute(insert_sql, (list_mingzi[i], list_compamy[i], list_xiaoqi[i], list_jiage[i]))
    conn.commit()
    cursor.close()
    conn.close()







