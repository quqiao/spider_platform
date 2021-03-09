# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# s1 = Series(np.random.randn(10))  # Series排序
# print(s1)
# s2 = s1.sort_values()  # 值排序
# print(s2)
# s3 = s1.sort_values(ascending=False)  # 值降序排序
# print(s3)
# s4 = s1.sort_index()  # 对index进行排序
# print(s4)
# s5 = s1.sort_index(ascending=False)  # 对index进行降序排序
# print(s5)

df1 = DataFrame(np.random.randn(40).reshape(8, 5), columns=['A','B','C','D','E'])  # DataFrame排序
# print(df1)
# print(df1['A'].sort_values())  # 某一列Series排序
print(df1.sort_values('A'))  # DataFrame对某列进行排序
print(df1.sort_values('A', ascending=False))  # 降序排序
print(df1.sort_index())  # 对index进行排序