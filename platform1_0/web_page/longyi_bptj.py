# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from lxml import etree
import pandas as pd
import pymysql

list_jiage = []
list_jiage2 = []
list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []
list_xiangou = []

def clear_list():
    list_jiage.clear()
    list_mingzi.clear()
    list_compamy.clear()
    list_guige.clear()
    list_xiaoqi.clear()

def crawl_longyi_tjbp():
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("http://www.longyiyy.com/login")
    time.sleep(2)
    username = driver.find_element_by_xpath('//*[@id="pane-0"]/form/div[1]/div/div/input')
    password = driver.find_element_by_xpath('//*[@id="pane-0"]/form/div[2]/div/div/input')
    username.send_keys('18030535053')
    password.send_keys('123456')
    # 模拟点击“登录”按钮2
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/button').click()
    time.sleep(3)
    driver.get("http://activity.longyiyy.com/eleven/tjzq/58,59,60,52/58")
    time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/img').click()
    for i in range(1, 49):
        time.sleep(6)  # 停顿3秒等待页面加载完毕！！！（必须留有页面加载的时间，否则获得的源代码会不完整。）
        html_sourcode = driver.page_source
        html = etree.HTML(html_sourcode, etree.HTMLParser())
        for j1 in range(1, 21):
            jg = html.xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[3]/div/div/div[%d]/div[5]/p[3]/span[2]/text()' % j1)
            jg1 = ''.join(jg)
            list_jiage2.append(jg1)
        for j in range(1, 21):
            jg = html.xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[3]/div/div/div[%d]/div[3]/p/span[2]/text()' % j)
            jg1 = ''.join(jg)
            list_jiage.append(jg1)
        for n in range(1, 21):
            cj = html.xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[3]/div/div/div[%d]/div[5]/p[4]/span/text()' % n)
            cj1 = ''.join(cj)
            list_compamy.append(cj1)
        for m in range(1, 21):
            mz = html.xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[3]/div/div/div[%d]/div[5]/p[1]/text()' % m)
            mz1 = ''.join(mz)
            list_mingzi.append(mz1)
        for g in range(1, 21):
            gg = html.xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[3]/div/div/div[%d]/div[5]/p[5]/span[2]/text()' % g)
            gg1 = ''.join(gg)
            list_guige.append(gg1)
        for x in range(1, 21):
            xq = html.xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[3]/div/div/div[%d]/div[5]/p[7]/span[2]/text()' % x)
            xq1 = ''.join(xq)
            list_xiaoqi.append(xq1)
        for z in range(1, 21):
            xg = html.xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[3]/div/div/div[%d]/div[5]/p[3]/span[3]/span[2]/text()' % z)
            xg1 = ''.join(xg)
            list_xiangou.append(xg1)

        js = "var q=document.documentElement.scrollTop=10000"  # 滑动到底部
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_css_selector('#app > div > div > div > div.main > div.list-bg > div.el-pagination.is-background > button.btn-next > span').click()
    driver.close()

"""保存为csv格式文件"""
def save_csv():
    dataframe = pd.DataFrame({'特价': list_jiage2, '券后折扣价': list_jiage, '药名': list_mingzi, '厂家': list_compamy, '规格': list_guige, '效期': list_xiaoqi, '限购': list_xiangou})  # 字典中的key值即为csv中列名
    dataframe.to_csv("longyi_tjbp_20201102_xiangou.csv", index=False, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

# """存储到mysql数据库中"""
# def save_mysql():
#     conn = pymysql.connect('localhost', 'root', '123456', 'spider_platform')  # 有中文要存入数据库的话要加charset='utf8'
#     # 创建游标
#     cursor = conn.cursor()  # pymysql.cursors.DictCursor
#     cursor.execute("DROP TABLE IF EXISTS longyi_tjzq")
#     # 使用预处理语句创建表
#     sql = """
#           CREATE TABLE longyi_tjzq
#           (
#              ID int unsigned auto_increment primary key,
#              name VARCHAR(100),
#              cj VARCHAR(100),
#              gg VARCHAR(100),
#              xq VARCHAR(100),
#              price VARCHAR(100)
#           )
#           """
#     cursor.execute(sql)
#     insert_sql = """
#                  insert into longyi_tjzq
#                  (name,cj,gg,xq,price)
#                  VALUES
#                  (%s,%s,%s,%s,%s)
#                  """
#     for i in range(len(list_mingzi)):
#         cursor.execute(insert_sql, (list_mingzi[i], list_compamy[i], list_guige[i], list_xiaoqi[i], list_jiage[i]))
#     conn.commit()
#     cursor.close()
#     conn.close()

if __name__ == '__main__':# 验证拼接后的正确性
    crawl_longyi_tjbp()
    save_csv()


