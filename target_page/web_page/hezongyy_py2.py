# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import pandas as pd
import pymysql
from lxml import etree

list_jiage = []
list_mingzi = []
list_compamy = []
list_guige = []
list_xiaoqi = []

def crawl_hezongyy():
    executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("http://127.0.0.1:8000/index/")
    time.sleep(2)
    frame = driver.find_element_by_id("ifm")
    driver.switch_to.frame(frame)
    html_sourcode = driver.page_source
    html = etree.HTML(html_sourcode, etree.HTMLParser())
    result = html.xpath('//ul/li[1]//text()') or html.xpath()
    print(result)
    # soup = BeautifulSoup(html_sourcode, 'lxml')
    # all1 = soup.find_all(["li", "div"])
    # print(all1)

if __name__ == '__main__':  # 验证拼接后的正确性
    crawl_hezongyy()