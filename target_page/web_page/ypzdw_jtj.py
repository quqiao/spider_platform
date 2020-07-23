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
list_shangjia = []

def crawl_ypzdw_jtj(count):
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://account.ypzdw.com/login?application=yw-ypzdw")
    time.sleep(2)
    # 模拟输入账号密码
    username = driver.find_element_by_class_name(
        '//*[@id="app"]/section/section/div/div[2]/div/div[2]/div[1]/div[2]/form/div[1]/div/div/input')
    password = driver.find_element_by_class_name(
        '//*[@id="app"]/section/section/div/div[2]/div/div[2]/div[1]/div[2]/form/div[2]/div/div/input')
    username.send_keys('bianyuantianshi')
    password.send_keys('19860201xy')
    # 模拟点击“登录”按钮
    driver.find_element_by_class_name('el-button.button-submit.el-button--primary').click()
    time.sleep(2)
    for i in range(1, count+1):
        driver.get("'https://www.ypzdw.com/jshop/ca/commonRec?t=personTiered&p=1&show=all&topid=0'" % i)
        time.sleep(3)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
        html_sourcode = driver.page_source
        html = etree.HTML(html_sourcode, etree.HTMLParser())
        for j in range(1, 41):
            jg = html.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[1]/a/div[4]/p[2]/text()' % j)
            jg1 = ''.join(jg)
            list_jiage.append(jg1)
        for n in range(1, 41):
            cj = html.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[3]/p[2]/text()' % n)
            cj1 = ''.join(cj)
            list_compamy.append(cj1)
        for m in range(1, 41):
            mz = html.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[2]/a/text()' % m)
            mz1 = ''.join(mz)
            list_mingzi.append(mz1)
        for g in range(1, 41):
            gg = html.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[3]/p[1]/text()' % g)
            gg1 = ''.join(gg)
            list_guige.append(gg1)
        for s in range(1, 41):
            sj = html.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[3]/p[3]/a/text()' % s)
            sj1 = ''.join(sj)
            list_shangjia.append(sj1)
    driver.close()

"""保存为csv格式文件"""
def save_csv():
    dataframe = pd.DataFrame({'价格': list_jiage, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_shangjia})  # 字典中的key值即为csv中列名
    dataframe.to_csv("test-01.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

"""存储到mysql数据库中"""
def save_mysql():
    conn = pymysql.connect('localhost', 'root', '123456', 'spider_platform')  # 有中文要存入数据库的话要加charset='utf8'
    # 创建游标
    cursor = conn.cursor()  # pymysql.cursors.DictCursor
    cursor.execute("DROP TABLE IF EXISTS ypzdw_jtj")
    # 使用预处理语句创建表
    sql = """
          CREATE TABLE ypzdw_jtj 
          (
             ID int unsigned auto_increment primary key,
             name VARCHAR(100),
             cj VARCHAR(100),
             gg VARCHAR(100),
             sj VARCHAR(100),
             price VARCHAR(100)
          )
          """
    cursor.execute(sql)
    insert_sql = """
                 insert into ypzdw_jtj
                 (name,cj,gg,sj,price) 
                 VALUES
                 (%s,%s,%s,%s,%s)
                 """
    for i in range(len(list_mingzi)):
        cursor.execute(insert_sql, (list_mingzi[i], list_compamy[i], list_guige[i], list_shangjia[i], list_jiage[i]))
    conn.commit()
    cursor.close()
    conn.close()







