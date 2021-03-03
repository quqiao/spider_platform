# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import webbrowser
import time

# link = "http://www.tiobe.com/tiobe-index/"
# print(webbrowser.open(link))  # 打开相应的网站，需手动复制到剪切板中
# time.sleep(30)
df = pd.read_clipboard()  # 执行这段代码将剪切板上的内容自动生成dataFrame对象
# print(df)
# print(type(df))  # 查看类型
# print(df.columns)  # 查看所有列
# print(df.Ratings)  # 查看
df_new = DataFrame(df, columns=['Feb-20', 'Programming Language', 'test1', 'test2', 'test3', 'test4'])  # 从df中提取指定页,多加不存在的时会自动赋值为空NaN
# print(df_new)
df_new['test1'] = range(0, 20)  # 对序列赋值，使用range函数
# print(df_new)
df_new['test2'] = np.arange(1, 21)  # 使用np下的arange（数组）函数
# print(df_new)
df_new['test3'] = pd.Series(np.arange(2, 22))  # 使用序列修改
# print(df_new)
df_new['test4'] = pd.Series(['100', '200'], index=[3, 4])  # 对单数某一列下的某些行进行赋值
print(df_new)

