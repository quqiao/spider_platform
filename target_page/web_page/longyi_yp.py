# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from lxml import etree
import pandas as pd
import pymysql

list_jiage = []
list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []

def crawl_longyi_yp(count):
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("http://www.longyiyy.com/login.html")
    time.sleep(2)
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('userpass')
    username.send_keys('18030535053')
    password.send_keys('123456')
    # 模拟点击“登录”按钮2
    driver.find_element_by_class_name('is').click()
    time.sleep(1)
    for i in range(1, count+1):
        driver.get("http://www.longyiyy.com/goods-filter-0-0-0-0-0-0-1-%d.html" % i)
        time.sleep(3)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
        html_sourcode = driver.page_source
        html = etree.HTML(html_sourcode, etree.HTMLParser())
        for j in range(1, 21):
            jg = html.xpath('//*[@id="pro_list1"]/li[%d]/p[2]/span[2]/text()' % j)
            jg1 = ''.join(jg)
            list_jiage.append(jg1)
        for n in range(1, 21):
            cj = html.xpath('//*[@id="pro_list1"]/li[%d]/p[3]/text()' % n)
            cj1 = ''.join(cj)
            list_compamy.append(cj1)
        for m in range(1, 21):
            mz = html.xpath('//*[@id="pro_list1"]/li[%d]/p[1]/a/text()' % m)
            mz1 = ''.join(mz)
            list_mingzi.append(mz1)
        for g in range(1, 21):
            gg = html.xpath('//*[@id="pro_list1"]/li[%d]/p[4]/span/text()' % g)
            gg1 = ''.join(gg)
            list_guige.append(gg1)
        for x in range(1, 21):
            xq = html.xpath('//*[@id="pro_list1"]/li[%d]/p[6]/span[1]/i/text()' % x)
            xq1 = ''.join(xq)
            list_xiaoqi.append(xq1)
    driver.close()

"""保存为csv格式文件"""
def save_csv():
    dataframe = pd.DataFrame({'价格': list_jiage, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi})  # 字典中的key值即为csv中列名
    dataframe.to_csv("test-01.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

"""存储到mysql数据库中"""
def save_mysql():
    conn = pymysql.connect('localhost', 'root', '123456', 'spider_platform')  # 有中文要存入数据库的话要加charset='utf8'
    # 创建游标
    cursor = conn.cursor()  # pymysql.cursors.DictCursor
    cursor.execute("DROP TABLE IF EXISTS longyi_yp")
    # 使用预处理语句创建表
    sql = """
          CREATE TABLE longyi_yp 
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
                 insert into longyi_yp 
                 (name,cj,gg,xq,price) 
                 VALUES
                 (%s,%s,%s,%s,%s)
                 """
    for i in range(len(list_jiage)):
        cursor.execute(insert_sql, (list_mingzi[i], list_compamy[i], list_guige[i], list_xiaoqi[i], list_jiage[i]))
    conn.commit()
    cursor.close()
    conn.close()







