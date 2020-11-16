# -*- coding: utf-8 -*-

from selenium import webdriver
import time

"""119活动抽奖页面执行"""
executable_path = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get("http://192.168.0.99:10001/#/login")
time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/form/div[1]/div/div[1]/input')
password = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input')
username.send_keys('测试05')
password.send_keys('a123456')
time.sleep(2)
driver.find_element_by_class_name('el-button.el-button--primary').click()
time.sleep(3)
driver.get('http://192.168.0.99:10001/#/lotteryDraw')

# js = "var q=document.documentElement.scrollTop=10000"  # 滑动到底部
# driver.execute_script(js)
# time.sleep(2)
# driver.find_element_by_xpath(('//*[@id="app"]/div/div[9]/div[5]/div[1]/img'))  # 进入抽奖界面
# time.sleep(2)
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
# time.sleep(2)


for i in range(1, 100000):
    time.sleep(2)
    driver.find_element_by_class_name('start').click()
    time.sleep(10)
    driver.refresh()
