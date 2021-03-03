# -*- coding: utf-8 -*-
# author: quqiao

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

path = 'F:\django\spider_platform\DataAnalysis\data\medical_data_20201109.xlsx'
df = pd.read_excel(path, sheet_name='聚创')
# print(df)
# print(df['原价'])  # 支持索引操作
# print(df[['原价', '特价']])
# print(df.iloc[1:5, 2:3])  # 使用iloc进行index切片操作，前一个切片表示行，后一个切片表示列
# df1 = df.iloc[5:11, 1:5]
# print(df1)
# print(df.loc[1:10])  # 使用loc对内容进行挑选
# print(df.loc[1:10, :'特价'])
print(df.loc[1:10, '原价': '规格'])