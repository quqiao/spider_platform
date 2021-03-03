# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

n = np.nan
# print(type(n))  # nan类型与运算
m = 1
# print(n+m)  # nan参与运算结果还是nan
s1 = Series([1, 2, np.nan, 3, 4], index=['A', 'B', 'C', 'D', 'E'])
# print(s1)
# print(s1.isnull())  # 判断是否为nan
# print(s1.notnull())  # 判断是否为非nan
# print(s1.dropna())  # 去掉nan值

df1 = DataFrame([[1, 2, 3], [np.nan, 5, 6], [7, 8, np.nan], [np.nan, np.nan, np.nan]])  # DataFrame中nan的使用
print(df1)
# print(df1.isnull())
# print(df1.notnull())
df2 = df1.dropna(axis=0)  # 去掉有nan的行
# print(df2)
df3 = df1.dropna(axis=1)  # 去掉有nan的列
# print(df3)
df4 = df1.dropna(axis=0, how='any')  # 参数how，any：如果存在nan则去掉，
# print(df4)
df5 = df1.dropna(axis=0, how='all')  # all：如果全为nan则去掉
# print(df5)

dframe = DataFrame([[1, 2, 3], [np.nan, 5, 6], [7, np.nan, np.nan], [np.nan, np.nan, np.nan]])
# print(dframe)
df6 = dframe.dropna(axis=0, thresh=2)  # 参数thresh指定去掉多少个nan，大于等于
# print(df6)
# print(dframe.fillna(value=1))  # nan填充
print(dframe.fillna(value={0: 0, 1: 1, 2: 2, 3: 3}))  # 指定列进行填充，如0列填充0,1列填充1，自己指定

