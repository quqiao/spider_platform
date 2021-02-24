# -*- coding: utf-8 -*-
# author: quqiao

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

path = 'F:\django\spider_platform\DataAnalysis\data\medical_data_20201109.xlsx'
df = pd.read_excel(path, sheet_name='聚创')
print(df)
print(df['原价'])  # 支持索引操作
print(df[['原价', '特价']])