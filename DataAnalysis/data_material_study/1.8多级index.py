# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

s1 = Series(np.random.randn(6), index=[['1', '1', '1', '2', '2', '2'],['a', 'b', 'c', 'a', 'b', 'c']])  # 多级Series
# print(s1)
# print(s1['1'])  # 下面一级也是Series
# print(s1['1']['a'])  # 访问
# print(s1[:, 'a'])  # 获取第二级Series
# print(type(s1[:, 'a']))  # 类型
# df1 = s1.unstack()  # 与DataFrame转换
# print(df1)
# df2 = DataFrame([s1['1'], s1['2']])  # DataFrame也可以有多个Series组成
# print(df2)
# s2 = df1.unstack()  # DataFrame转化为Series
# print(s2)
# s3 = df1.T.unstack()
# print(s3)

# df1 = DataFrame(np.arange(16).reshape(4, 4))  # 多级DataFrame
# print(df1)
# df2 = DataFrame(np.arange(16).reshape(4, 4), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]])  # 多级index
# print(df2)
df3 = DataFrame(np.arange(16).reshape(4, 4), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['BJ','BJ','SH','GZ'],[8,9,8,8]])  # 多级colunms
# print(df3)
print(df3['BJ'])
print(type(df3['BJ']))
print(df3['BJ'][8])