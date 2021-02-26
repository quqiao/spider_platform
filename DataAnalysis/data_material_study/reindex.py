# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])  # 创建一个Series对象
# print(s1)
# print(s1.reindex(index=['A', 'B', 'C', 'D', 'E']))  # Series的reindex操作
# print(s1.reindex(index=['A', 'B', 'C', 'D', 'E'], fill_value=10))  # 缺失值填充
s2 = Series(['A', 'B', 'C'], index=[1, 5, 10])  # 创建一个Series对象2
# print(s2)
# print(s2.reindex(index=range(15)))
# print(s2.reindex(index=range(15), method='ffill'))  # 缺失值的另一种填充方法，满填

# df1 = DataFrame(np.random.rand(25).reshape(5, 5))  # 创建DataFrame对象
# print(df1)
df1 = DataFrame(np.random.rand(25).reshape(5, 5), index=['A', 'B', 'D', 'E', 'F'], columns=['a1', 'b1', 'c1', 'd1', 'e1'])  # 修改行列
# print(df1)
# print(df1.reindex(index=['A', 'B', 'C', 'D', 'E', 'F']))  # 行的reindex
# print(df1.reindex(columns=['a1', 'b1', 'c1', 'd1', 'e1', 'f1']))  # 列的reindex
# print(df1.reindex(index=['A1', 'B1', 'C1', 'D1', 'E1', 'F1'], columns=['a2', 'b2', 'c2', 'd2', 'e2']))
# print(s1)
# print(s1.drop('A'))  # drop进行删除
# print(df1.drop(['A', 'B'], axis=0))  # DataFrame使用drop是有个参数axis默认值为0，删除行，1则删除列
print(df1.drop('c1', axis=1))
