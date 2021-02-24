# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import webbrowser

link = 'http://pandas.pydata.org/pandas-docs/version/0.20/io.html'  # io操作详细介绍
webbrowser.open(link)
df1 = pd.read_clipboard()  # 从粘贴板上读取数据
df1.to_clipboard()  # 把数据放入粘贴板中，数据可以直接粘贴到excel文件中
df1.to_csv('df1.csv')  # 读写csv文件
df1.to_csv('df1.csv', index=False)  # 取消index
df2 = pd.read_csv('df1.csv')
df1.to_json()  # 转化为json格式
pd.read_json(df1.to_json())  # 读取json
df1.to_html('df1.html')  # 转化为html格式
df1.to_excel('df1.xlsx')  # 转化为excel格式

