# -*- coding: utf-8 -*-
# author: quqiao
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df1 = DataFrame({"城市": ["北京", "上海", "广州"], "人口": [1000, 2000, 1500]})
# print(df1)
# df1['GDP'] = Series([1299, 1399, 1499])  # 用Series添加一列
# print(df1)
# gdp_map = {"北京": 999, "上海": 888, "广州": 777}
# df1['GDP'] = df1['城市'].map(gdp_map)  # 使用map添加一列
# print(df1)
df1.index = ['A', 'B', 'C']  # 修改索引
# print(df1)
# df1['天气'] = Series(['多云', '大雨', '晴朗'])
# print(df1)  # 天气输入为NaN
# df1['天气'] = Series(['多云', '大雨', '晴朗'], index=['A', 'B', 'C'])
# print(df1)  # Series加index后，天气输入才不为NaN

s1 = Series(np.arange(10))
print(s1)
print(s1.replace(1, np.nan))  # 替换一个值,也可以使用字典的方式替换(略)
print(s1.replace([5, 7, 9], [np.nan, 777, 999]))  # 替换多个值
