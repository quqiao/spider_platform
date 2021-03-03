# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([1, 2, 3], index=['A', 'B', 'C'])
s2 = Series([6, 7, 8, 9], index=['A', 'B', 'C', 'D'])
# print(s1 + s2)  # Series 计算 可以计算加减乘, 没有的数据为nan

df1 = DataFrame(np.arange(4).reshape(2, 2), index=['A', 'B'], columns=['BJ', 'GZ'])
df2 = DataFrame(np.arange(9).reshape(3, 3), index=['A', 'B', 'C'], columns=['BJ', 'GZ', 'SH'])
# print(df1 + df2)  # DataFrame计算，可加减乘
df3 = DataFrame([[1, 2, 3], [4, 5, np.nan], [7, 8, 9]], index=['A', 'B', 'C'], columns=['c1', 'c2', 'c3'])  # DataFrame相关函数
print(df3)
# print(df3.sum())  # 列和
# print(df3.sum(axis=1))  # 行和
print(df3.max())  # 最大值列
print(df3.max(axis=1))  # 最大值行
print(df3.min())  # 最小值列
print(df3.min(axis=1))  # 最小值行
print(df3.describe())  # 描述
# print(df3.describe(axis=1))  # 不能使用axis参数
