# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import pandas as pd
from lxml import etree
import openpyxl
import pymysql

list_jiage = []
list_jiage2 = []
list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []

def crawl_hezongyy_yp():
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://www.hezongyy.com/#/login")  # 获取登录界面
    time.sleep(2)
    username = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/form/div[1]/div/div[1]/input')  # 账号输入框
    password = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input')  # 密码输入框
    username.send_keys('测试05')
    password.send_keys('a123456')
    driver.find_element_by_class_name('el-button.el-button--primary').click()  # 模拟点击“登录”按钮
    time.sleep(1)
    driver.get("https://www.hezongyy.com/#/puyaoList")  # 获取普药列表
    time.sleep(1)
    driver.maximize_window()  # 进行全屏展示

    for i in range(1, 4):
        time.sleep(5)
        html_sourcode = driver.page_source  # 获取页面源码
        html = etree.HTML(html_sourcode, etree.HTMLParser())  # 利用etree.HTML，将字符串解析为HTML文档
        for i in range(1, 41):
            jg = html.xpath('//*[@id="app"]/div/div[7]/div[2]/div[3]/ul[1]/li[%d]/div/div/div[3]/span/del/text()' % i)
            jg1 = ''.join(jg)
            list_jiage.append(jg1)

            mz = html.xpath('//*[@id="app"]/div/div[7]/div[2]/div[3]/ul[1]/li[%d]/div/div/p[1]/text()' % i)
            mz1 = ''.join(mz)
            list_mingzi.append(mz1)

            cj = html.xpath('//*[@id="app"]/div/div[7]/div[2]/div[3]/ul[1]/li[%d]/div/div/p[2]/text()' % i)
            cj1 = ''.join(cj)
            list_compamy.append(cj1)

            gg = html.xpath('//*[@id="app"]/div/div[7]/div[2]/div[3]/ul[1]/li[%d]/div/div/p[3]/text()' % i)
            gg1 = ''.join(gg)
            list_guige.append(gg1)

            xq = html.xpath('//*[@id="app"]/div/div[7]/div[2]/div[3]/ul[1]/li[%d]/div/div/p[4]/span[1]/text()' % i)
            xq1 = ''.join(xq)
            list_xiaoqi.append(xq1)

        for i in range(1, 41):
            jg2 = html.xpath('//*[@id="app"]/div/div[7]/div[2]/div[3]/ul[1]/li[%d]/div/div/div[3]/span/text()' % i)
            jg3 = ''.join(jg2)
            list_jiage2.append(jg3)

        time.sleep(2)
        driver.find_element_by_class_name('el-icon.el-icon-arrow-right').click()  # 点击下一页
    driver.close()  # 关闭网页

def save_excel():
    """使用csv保存数据"""
    # dataframe = pd.DataFrame({'原价': list_jiage, '特价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
    #              '效期': list_xiaoqi})  # 字典中的key值即为csv中列名
    # dataframe.to_csv("hezongyy_20201111.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

    """通过xlsx保存数据"""
    # data = {'原价': list_jiage, '特价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi}
    # dataframe = pd.DataFrame(data, columns=['原价', '特价', '药名', '厂家', '规格', '效期'])
    # dataframe.to_excel("hezongyy_20201111.xlsx", encoding='utf-8', index=False, header=True, sheet_name='合纵')
    # print(dataframe)

    """在已有的excel中加入新的sheet保存数据"""
    nowtime = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当前时间并转化为类似20201217的格式
    try:
        data = {'原价': list_jiage, '特价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
                '效期': list_xiaoqi}
        wb = openpyxl.load_workbook('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime)
        writer = pd.ExcelWriter('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime, engine='openpyxl')  # 如果有多个模块可以读写excel文件，这里要指定engine，否则可能会报错
        writer.book = wb  # 没有这个语句的话excel表将完全被覆盖
        df = pd.DataFrame(data, columns=['原价', '特价', '药名', '厂家', '规格', '效期'])  # 如果有相同名字的工作表，新添加的将命名为Sheet21，如果Sheet21也有了就命名为Sheet22，不会覆盖原来的工作表
        df.to_excel(writer, encoding='utf-8', index=False, header=True, sheet_name='合纵')
        writer.save()
        writer.close()
    except FileNotFoundError:
        data = {'原价': list_jiage, '特价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi}
        dataframe = pd.DataFrame(data, columns=['原价', '特价', '药名', '厂家', '规格', '效期'])
        dataframe.to_excel("F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx" % nowtime, encoding='utf-8', index=False, header=True, sheet_name='合纵')

def save_mysql():
    conn = pymysql.connect('localhost', 'root', '123456', 'spider_platform')  # 有中文要存入数据库的话要加charset='utf8'
    # 创建游标
    cursor = conn.cursor()  # pymysql.cursors.DictCursor
    cursor.execute("DROP TABLE IF EXISTS hezongyy_yp")
    # 使用预处理语句创建表
    sql = """
          CREATE TABLE hezongyy_yp 
          (
             ID int unsigned auto_increment primary key,
             name VARCHAR(100),
             cj VARCHAR(100),
             gg VARCHAR(100),
             xq VARCHAR(100),
             price VARCHAR(100),
             price1 VARCHAR(100)
          )
          """
    cursor.execute(sql)
    insert_sql = """
                 insert into hezongyy_yp 
                 (name,cj,gg,xq,price,price1) 
                 VALUES
                 (%s,%s,%s,%s,%s,%s)
                 """
    for i in range(len(list_jiage)):
        cursor.execute(insert_sql, (list_mingzi[i], list_compamy[i], list_guige[i], list_xiaoqi[i], list_jiage[i], list_jiage2[i]))
    conn.commit()
    cursor.close()
    conn.close()



if __name__=='__main__':  # 验证拼接后的正确性
    crawl_hezongyy_yp()
    save_mysql()