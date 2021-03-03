# -*- coding: utf-8 -*-
# author: quqiao

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = {'Student': ['XiaoMing', 'XiaoHong', 'XiaoQiang'], 'Grade': ['100', '95', '90'], 'Class': ['RG1', 'RG2', 'RG3']}  # 创建一个字典

s1 = pd.Series(data['Student'])  # 创建一个Series对象
# print(s1)
# print(s1.values)  # 查看这个对象的属性
# print(s1.index)  # 没有给索引赋值时默认
s2 = pd.Series(data['Student'], index=['first', 'second', 'third'], name='hahaha')  # 创建并修改默认索引，增加列名
# print(s2)
df1 = pd.DataFrame(data)  # 使用字典创建DataFrame对象
# print(df1)
cou = df1['Grade']
# print(cou)
# print(type(cou))  # 列的类型为Series
# print(df1.index)  # 默认索引
c1 = df1['Student'][2]
# print(c1)  # 查看某一行某一列
# print(type(c1))
# for row in df1.iterrows():
#     print(row), print(type(row)), print(type(row[0])), print(type(row[1]))
#     break

s1 = pd.Series(data['Student'])
s2 = pd.Series(data['Grade'])
s3 = pd.Series(data['Class'])
df_new = pd.DataFrame([s1, s2, s3])  # 当以列表的形式构建的时候会按行来放，有时候可以优先选择按行放
# print(df_new)
# print(df_new.T)  # 进行行列转置
# df_new.index = ['first', 'second', 'third']
# print(df_new)
