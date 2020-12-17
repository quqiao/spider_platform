# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import pandas as pd
import pymysql
from lxml import etree
import openpyxl

list_jiage = []
list_jiage2 = []
list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []

def crawl_rjyiyao_yp():
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("http://new.rjyiyao.com/web/login")
    time.sleep(2)
    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')
    username.send_keys('18030535053')
    password.send_keys('123456')
    # 模拟点击“登录”按钮
    driver.find_element_by_id('btnLogin').click()
    time.sleep(3)
    driver.maximize_window()

    for i in range(1, 2):
        driver.get(
            "http://new.rjyiyao.com/web/product/gmed?type=1&page=%d" % i)
        time.sleep(5)
        html_sourcode = driver.page_source
        html = etree.HTML(html_sourcode, etree.HTMLParser())
        for i in range(1, 41):
            jg = html.xpath('//*[@id="pageContent"]/div/div[%d]/h2/span[1]/text()' % i)
            jg1 = ''.join(jg)
            list_jiage.append(jg1)

            mz = html.xpath('//*[@id="pageContent"]/div/div[%d]/h1/text()' % i)
            mz1 = ''.join(mz)
            list_mingzi.append(mz1)

            cj = html.xpath('//*[@id="pageContent"]/div/div[%d]/p/text()' % i)
            cj1 = ''.join(cj)
            list_compamy.append(cj1)

            gg = html.xpath('//*[@id="pageContent"]/div/div[%d]/section[1]/p[1]/text()' % i)
            gg1 = ''.join(gg)
            list_guige.append(gg1)

            xq = html.xpath('//*[@id="pageContent"]/div/div[%d]/section[2]/p[1]/text()' % i)
            xq1 = ''.join(xq)
            list_xiaoqi.append(xq1)

        for i in range(1, 41):
            jg2 = html.xpath('//*[@id="pageContent"]/div/div[%d]/h2/span[2]/text()' % i)
            jg3 = ''.join(jg2)
            list_jiage2.append(jg3)
        time.sleep(1)
    driver.close()

def save_csv():
    """使用csv保存数据"""
    # dataframe = pd.DataFrame({'原价': list_jiage, '特价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
    #              '效期': list_xiaoqi})  # 字典中的key值即为csv中列名
    # dataframe.to_csv("hezongyy_20201111.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

    """通过xlsx保存数据"""
    # data = {'原价': list_jiage, '特价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi}
    # dataframe = pd.DataFrame(data, columns=['原价', '特价', '药名', '厂家', '规格', '效期'])
    # dataframe.to_excel("hezongyy_20201111.xlsx", encoding='utf-8', index=False, header=True, sheet_name='蓉锦')
    # print(dataframe)

    """在已有的excel中加入新的sheet保存数据"""
    nowtime = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当前时间并转化为类似20201217的格式
    try:
        data = {'原价': list_jiage, '券后约': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
                '效期': list_xiaoqi}
        wb = openpyxl.load_workbook('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime)
        writer = pd.ExcelWriter('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime, engine='openpyxl')  # 如果有多个模块可以读写excel文件，这里要指定engine，否则可能会报错
        writer.book = wb  # 没有这个语句的话excel表将完全被覆盖
        df = pd.DataFrame(data, columns=['原价', '券后约', '药名', '厂家', '规格', '效期'])  # 如果有相同名字的工作表，新添加的将命名为Sheet21，如果Sheet21也有了就命名为Sheet22，不会覆盖原来的工作表
        df.to_excel(writer, encoding='utf-8', index=False, header=True, sheet_name='蓉锦')
        writer.save()
        writer.close()
    except FileNotFoundError:
        data = {'原价': list_jiage, '券后约': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi}
        dataframe = pd.DataFrame(data, columns=['原价', '券后约', '药名', '厂家', '规格', '效期'])
        dataframe.to_excel('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime, encoding='utf-8', index=False, header=True, sheet_name='蓉锦')



if __name__ == '__main__':  # 验证拼接后的正确性
    crawl_rjyiyao_yp()
    save_csv()