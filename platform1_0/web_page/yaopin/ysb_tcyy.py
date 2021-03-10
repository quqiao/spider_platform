# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from lxml import etree
import pandas as pd
import pymysql
import openpyxl
from bs4 import BeautifulSoup

"""药师帮-拓创医药旗舰店全部品种"""


list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []
list_price1 = []
list_price2 = []
list_price3 = []

def clear_list():
    list_price1.clear()
    list_price2.clear()
    list_price3.clear()
    list_mingzi.clear()
    list_compamy.clear()
    list_guige.clear()
    list_xiaoqi.clear()

def crawl_ysb_lyg():
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://dian.ysbang.cn/index.html#/login")
    time.sleep(2)
    username = driver.find_element_by_id('userAccount')
    password = driver.find_element_by_id('password')
    username.send_keys('13518134160')
    password.send_keys('yxs78311')
    time.sleep(10)  # 手动输入验证码
    driver.find_element_by_id('loginBtn').click()  # 模拟点击“登录”按钮
    time.sleep(1)
    driver.maximize_window()  # 进行全屏展示
    time.sleep(5)
    driver.get("https://dian.ysbang.cn/index.html#/supplierstore?providerId=3347")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]').click()  # 全部商品
    time.sleep(5)


    for i in range(1, 82):
        time.sleep(3)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
        html_sourcode = driver.page_source
        html = etree.HTML(html_sourcode, etree.HTMLParser())
        for j in range(1, 61):
            jg = html.xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[%d]/div[2]/div[1]/strong/text()' % j)
            jg1 = ''.join(jg)
            list_price1.append(jg1)

            jg2 = html.xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[%d]/div[2]/div[1]/span/text()' % j)
            jg3 = ''.join(jg2)
            list_price2.append(jg3)

        for t in range(1, 61):
            mz = html.xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[%d]/div[2]/div[2]/span/text()' % t)
            mz1 = ''.join(mz)
            list_mingzi.append(mz1)
        for i in range(1, 61):
            jg = html.xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[%d]/div[2]/div[4]/text()' % i)
            jg1 = ''.join(jg)
            list_compamy.append(jg1)
        for k in range(1, 61):
            jg = html.xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[%d]/div[1]/div[2]/div/text()' % k)
            jg1 = ''.join(jg)
            list_xiaoqi.append(jg1)
        time.sleep(5)
        driver.find_element_by_class_name("pagination-next").click()
    driver.close()
    # print(list_price1)
    # print(list_mingzi)
    # print(list_compamy)
    # print(list_xiaoqi)


"""保存为csv格式文件"""
def save_csv():
    """使用csv保存数据"""
    # dataframe = pd.DataFrame({'价格': list_price1, '药名': list_mingzi, '厂家': list_compamy, '效期': list_xiaoqi})  # 字典中的key值即为csv中列名
    # dataframe.to_csv("ysb_lyg_20210310.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

    """通过xlsx保存数据"""
    data = {'价格': list_price1, '折后约': list_price2, '药名': list_mingzi, '厂家': list_compamy, '效期': list_xiaoqi}
    dataframe = pd.DataFrame(data, columns=['价格', '折后约', '药名', '厂家', '效期'])
    dataframe.to_excel("ysb_tcyy_20210310.xlsx", encoding='utf-8', index=False, header=True, sheet_name='拓创医药')
    print(dataframe)

    # """在已有的excel中加入新的sheet保存数据"""
    # nowtime = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当前时间并转化为类似20201217的格式
    # try:
    #     data = {'原价': list_price1, '特价': list_price2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
    #             '效期': list_xiaoqi}
    #     wb = openpyxl.load_workbook('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime)
    #     writer = pd.ExcelWriter('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime,
    #                             engine='openpyxl')  # 如果有多个模块可以读写excel文件，这里要指定engine，否则可能会报错
    #     writer.book = wb  # 没有这个语句的话excel表将完全被覆盖
    #     df = pd.DataFrame(data, columns=['原价', '特价', '药名', '厂家', '规格',
    #                                      '效期'])  # 如果有相同名字的工作表，新添加的将命名为Sheet21，如果Sheet21也有了就命名为Sheet22，不会覆盖原来的工作表
    #     df.to_excel(writer, encoding='utf-8', index=False, header=True, sheet_name='聚创')
    #     writer.save()
    #     writer.close()
    # except FileNotFoundError:
    #     data = {'原价': list_price1, '特价': list_price2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi}
    #     dataframe = pd.DataFrame(data, columns=['原价', '特价', '药名', '厂家', '规格', '效期'])
    #     dataframe.to_excel('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime, encoding='utf-8', index=False, header=True, sheet_name='聚创')

"""存储到mysql数据库中"""
def save_mysql():
    conn = pymysql.connect('localhost', 'root', '123456', 'spider_platform')  # 有中文要存入数据库的话要加charset='utf8'
    # 创建游标
    cursor = conn.cursor()  # pymysql.cursors.DictCursor
    cursor.execute("DROP TABLE IF EXISTS scjuchuang_py")
    # 使用预处理语句创建表
    sql = """
          CREATE TABLE scjuchuang_py 
          (
             ID int unsigned auto_increment primary key,
             name VARCHAR(100),
             cj VARCHAR(100),
             gg VARCHAR(100),
             xq VARCHAR(100),
             price1 VARCHAR(100),
             price2 VARCHAR(100),
             price3 VARCHAR(100)
          )
          """
    cursor.execute(sql)
    insert_sql = """
                 insert into scjuchuang_py 
                 (name,cj,gg,xq,price1,price2,price3) 
                 VALUES
                 (%s,%s,%s,%s,%s,%s,%s)
                 """
    for i in range(len(list_mingzi)):
        cursor.execute(insert_sql, (list_mingzi[i], list_compamy[i], list_guige[i], list_xiaoqi[i], list_price1[i], list_price2[i], list_price3[i]))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':  # 验证拼接后的正确性
    crawl_ysb_lyg()
    save_csv()





