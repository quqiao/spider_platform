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
list_jiage3 = []
list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []

def crawl_hezongyy():
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://www.xmyc.com.cn/login")
    time.sleep(2)
    username = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div/div/input')
    password = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div/input')
    username.send_keys('13379084449')
    password.send_keys('123456')
    # 模拟点击“登录”按钮
    driver.find_element_by_class_name('ivu-btn.ivu-btn-success.ivu-btn-long.ivu-btn-large').click()
    time.sleep(1)
    driver.get("https://www.xmyc.com.cn/searchresult")
    for i in range(200):
        time.sleep(5)
        html_sourcode = driver.page_source
        html = etree.HTML(html_sourcode, etree.HTMLParser())
        for i in range(1, 31):
            jg = html.xpath('//*[@id="app"]/div[2]/div[2]/ul[1]/li/div[%d]/div[2]/a/div[1]/span[1]/text()' % i)
            jg1 = ''.join(jg)
            list_jiage.append(jg1)

        for i in range(1, 31):
            # ss = html.xpath('//*[@id="app"]/div[2]/div[2]/ul[1]/li/div[%d]/div[2]/a/div[1]/span[2]/img/@src' % i)
            # print(ss)
            if html.xpath('//*[@id="app"]/div[2]/div[2]/ul[1]/li/div[%d]/div[2]/a/div[1]/span[2]/img/@src' % i) == ['/img/goods/default-coupon.png']:
                list_jiage2.append("优惠券")
            else:
                list_jiage2.append("无")

        for i in range(1, 31):
            jg = html.xpath('//*[@id="app"]/div[2]/div[2]/ul[1]/li/div[%d]/div[2]/a/div[1]/span[2]/em/text()' % i)
            jg3 = ''.join(jg)
            list_jiage3.append(jg3)

        for j in range(1, 31):
            mz = html.xpath('//*[@id="app"]/div[2]/div[2]/ul[1]/li/div[%d]/div[2]/a/div[2]/text()' % j)
            mz1 = ''.join(mz)
            list_mingzi.append(mz1)

        for n in range(1, 31):
            cj = html.xpath('//*[@id="app"]/div[2]/div[2]/ul[1]/li/div[%d]/div[2]/a/p[4]/text()' % n)
            cj1 = ''.join(cj)
            list_compamy.append(cj1)

        for g in range(1, 31):
            gg = html.xpath('//*[@id="app"]/div[2]/div[2]/ul[1]/li/div[%d]/div[2]/a/p[1]/text()' % g)
            gg1 = ''.join(gg)
            list_guige.append(gg1)

        for x in range(1, 31):
            xq = html.xpath('//*[@id="app"]/div[2]/div[2]/ul[1]/li/div[%d]/div[2]/a/p[2]/span[1]/label/text()' % x)
            xq1 = ''.join(xq)
            list_xiaoqi.append(xq1)
        time.sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"  # 滑动到底部
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_class_name('ivu-page-next').click()  # 点击下一页
    driver.close()

def save_csv():
    """使用csv保存数据"""
    # dataframe = pd.DataFrame({'原价': list_jiage, '特价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
    #              '效期': list_xiaoqi})  # 字典中的key值即为csv中列名
    # dataframe.to_csv("hezongyy_20201111.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

    """通过xlsx保存数据"""
    data = {'原价': list_jiage, "优惠券":list_jiage2, "券":list_jiage3, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi}
    dataframe = pd.DataFrame(data, columns=['原价', '优惠券', '券', '药名', '厂家', '规格', '效期'])
    dataframe.to_excel("xmyc_yp_20201217.xlsx", encoding='utf-8', index=False, header=True, sheet_name='熊猫')
    print(dataframe)

    """在已有的excel中加入新的sheet保存数据"""
    # data = {'原价': list_jiage,'药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
    #         '效期': list_xiaoqi}
    # wb = openpyxl.load_workbook('/DataAnalysis/data/medical_data_20201109.xlsx')
    # writer = pd.ExcelWriter('/DataAnalysis/data/medical_data_20201109.xlsx', engine='openpyxl')  # 如果有多个模块可以读写excel文件，这里要指定engine，否则可能会报错
    # writer.book = wb  # 没有这个语句的话excel表将完全被覆盖
    # df = pd.DataFrame(data, columns=['原价', '特价', '药名', '厂家', '规格', '效期'])  # 如果有相同名字的工作表，新添加的将命名为Sheet21，如果Sheet21也有了就命名为Sheet22，不会覆盖原来的工作表
    # df.to_excel(writer, encoding='utf-8', index=False, header=True, sheet_name='合纵')
    # writer.save()
    # writer.close()


if __name__ == '__main__':  # 验证拼接后的正确性
    crawl_hezongyy()
    save_csv()