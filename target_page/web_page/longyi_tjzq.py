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
list_guige = []
list_xiaoqi = []

def crawl_longyi_tjzq(count):
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("http://www.longyiyy.com/login.html")
    time.sleep(2)
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('userpass')
    username.send_keys('18030535053')
    password.send_keys('123456')
    # 模拟点击“登录”按钮
    driver.find_element_by_class_name('is').click()
    time.sleep(1)
    for i in range(1, count+1):
        driver.get("http://www.longyiyy.com/events-filter-589-%d-1.html" % i)
        time.sleep(3)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
        html_sourcode = driver.page_source
        soup = BeautifulSoup(html_sourcode, 'lxml')
        # jg = soup.find_all(attrs={'class': {'datu-jiage'}})
        jg = soup.find_all(class_="datu-jiage")
        mz = soup.find_all(class_="datu-mingzi")
        cj = soup.find_all(class_="datu-compamy")
        gg = soup.find_all(class_="datu-guige")
        xq = soup.find_all(class_="datu-xiaoqi")
        for i in jg:
            list_jiage.append(i.text)
        for t in mz:
            list_mingzi.append(t.text)
        for j in cj:
            list_compamy.append(j.text)
        for g in gg:
            list_guige.append(g.text)
        for x in xq:
            list_xiaoqi.append(x.text)
    driver.close()


def save_csv():
    dataframe = pd.DataFrame({'价格': list_jiage, '药名': list_mingzi})  # 字典中的key值即为csv中列名
    dataframe.to_csv("test-01.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

def save_mysql():
    conn = pymysql.connect('localhost', 'root', '123456', 'spider_platform')  # 有中文要存入数据库的话要加charset='utf8'
    # 创建游标
    cursor = conn.cursor()  # pymysql.cursors.DictCursor
    cursor.execute("DROP TABLE IF EXISTS hezongyy_py")
    # 使用预处理语句创建表
    sql = """
          CREATE TABLE hezongyy_py 
          (
             ID int unsigned auto_increment primary key,
             name VARCHAR(100),
             cj VARCHAR(100),
             gg VARCHAR(100),
             xq VARCHAR(100),
             price VARCHAR(100)
          )
          """
    cursor.execute(sql)
    insert_sql = """
                 insert into hezongyy_py 
                 (name,cj,gg,xq,price) 
                 VALUES
                 (%s,%s,%s,%s,%s)
                 """
    for i in range(len(list_jiage)):
        cursor.execute(insert_sql, (list_mingzi[i], list_compamy[i], list_guige[i], list_xiaoqi[i], list_jiage[i]))
    conn.commit()
    cursor.close()
    conn.close()







