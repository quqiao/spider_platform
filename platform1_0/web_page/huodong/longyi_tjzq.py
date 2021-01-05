# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from lxml import etree
import pandas as pd
import pymysql
import openpyxl

"""龙一医药网，活动页面中特价专区"""

list_jiage = []
list_jiage2 = []
list_jiage3 = []
list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []

def clear_list():
    list_jiage.clear()
    list_mingzi.clear()
    list_compamy.clear()
    list_guige.clear()
    list_xiaoqi.clear()

def crawl_longyi_tjzq():
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("http://www.longyiyy.com/login")
    time.sleep(2)
    username = driver.find_element_by_xpath('//*[@id="pane-0"]/form/div[1]/div/div/input')
    password = driver.find_element_by_xpath('//*[@id="pane-0"]/form/div[2]/div/div/input')
    username.send_keys('18030535053')
    password.send_keys('123456')
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/button').click()  # 模拟点击“登录”按钮
    time.sleep(1)
    driver.maximize_window()  # 进行全屏展示
    time.sleep(1)
    driver.get("http://activity.longyiyy.com/tjzq/94,95/94")
    time.sleep(3)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
    for i in range(1, 31):
        html_sourcode = driver.page_source
        html = etree.HTML(html_sourcode, etree.HTMLParser())
        for i in range(1, 21):
            jg = html.xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[%d]/div[5]/p[2]/s/text()' % i)
            jg1 = ''.join(jg)
            list_jiage.append(jg1)

            cj = html.xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[%d]/div[5]/p[3]/span/text()' % i)
            cj1 = ''.join(cj)
            list_compamy.append(cj1)

            mz = html.xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[%d]/div[5]/p[1]/text()' % i)
            mz1 = ''.join(mz)
            list_mingzi.append(mz1)

            gg = html.xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[%d]/div[5]/p[4]/span[2]/text()' % i)
            gg1 = ''.join(gg)
            list_guige.append(gg1)

            xq = html.xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[%d]/div[5]/p[6]/span[2]/text()' % i)
            xq1 = ''.join(xq)
            list_xiaoqi.append(xq1)

        # for j in range(1, 21):
            jg = html.xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[%d]/div[5]/div[1]/p/span[2]/text()' % i)
            jg1 = ''.join(jg)
            list_jiage2.append(jg1)

            jg2 = html.xpath(
                '//*[@id="app"]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[%d]/div[3]/p/span[2]/text()' % i)
            jg3 = ''.join(jg2)
            list_jiage3.append(jg3)
        js = "var q=document.documentElement.scrollTop=10000"  # 滑动到底部
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_class_name('btn-next').click()  # 点击下一页
        time.sleep(5)

    driver.close()

"""保存为csv格式文件"""
def save_csv():
    """使用csv保存数据"""
    # dataframe = pd.DataFrame({'原价': list_jiage, '特价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
    #              '效期': list_xiaoqi})  # 字典中的key值即为csv中列名
    # dataframe.to_csv("hezongyy_20201111.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

    """通过xlsx保存数据"""
    data = {'原价': list_jiage, '特价': list_jiage2,'券后价':list_jiage3, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi}
    dataframe = pd.DataFrame(data, columns=['原价', '特价','券后价', '药名', '厂家', '规格', '效期'])
    dataframe.to_excel("longyitjzq_20210104.xlsx", encoding='utf-8', index=False, header=True, sheet_name='合纵')
    # print(dataframe)

    # """在已有的excel中加入新的sheet保存数据"""
    # nowtime = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当前时间并转化为类似20201217的格式
    # try:
    #     data = {'原价': list_jiage, '券后价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige,
    #             '效期': list_xiaoqi}
    #     wb = openpyxl.load_workbook('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime)
    #     writer = pd.ExcelWriter('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime,
    #                             engine='openpyxl')  # 如果有多个模块可以读写excel文件，这里要指定engine，否则可能会报错
    #     writer.book = wb  # 没有这个语句的话excel表将完全被覆盖
    #     df = pd.DataFrame(data, columns=['原价', '券后价','药名', '厂家', '规格',
    #                                      '效期'])  # 如果有相同名字的工作表，新添加的将命名为Sheet21，如果Sheet21也有了就命名为Sheet22，不会覆盖原来的工作表
    #     df.to_excel(writer, encoding='utf-8', index=False, header=True, sheet_name='龙一')
    #     writer.save()
    #     writer.close()
    # except FileNotFoundError:
    #     data = {'原价': list_jiage, '券后价': list_jiage2, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi}
    #     dataframe = pd.DataFrame(data, columns=['原价', '券后价', '药名', '厂家', '规格', '效期'])
    #     dataframe.to_excel('F:/django/spider_platform/DataAnalysis/data/medical_data_%s.xlsx' % nowtime, encoding='utf-8', index=False, header=True, sheet_name='合纵')


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


if __name__ == '__main__':  # 验证拼接后的正确性
    crawl_longyi_tjzq()
    save_csv()













