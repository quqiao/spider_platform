# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd

# series 是pandas两大数据结构之一
# Series 是带标签的一维数组，可存储整数、浮点数、字符串、Python 对象等类型的数据

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])  # 使用列表创建
# print(s1)
# print(s1.values)  # 查看s1的值
# print(s1.index)  # 查看s1的索引
# print(s1.dtype)  # 查看s1的类型

# s2 = pd.Series(np.arange(10))  # 使用数组创建
# print(s2)

# s3 = pd.Series({'test1': 1, 'test2': 2, 'test3': 3})  # 使用字典创建
# print(s3)

# Series的访问
s4 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(s4)
# print(s4['e'])
# print(s4[s4 > 2])
# print(s4.to_dict())  # s4转换为字典
# print(pd.Series(s4.to_dict()))  # 字典转换为Series

# e索引无值补充为NaN
index_1 = ['a', 'b', 'c', 'd', 'e']
# print(pd.Series(s1, index=index_1))
# print(pd.isnull(s1))  # NaN判断
# print(pd.notnull(s1))  # NaN判断

# 命名修改
s1.name = 'demo'
# print(s1)
s1.index.name = 'demo_modify'
print(s1.index)
