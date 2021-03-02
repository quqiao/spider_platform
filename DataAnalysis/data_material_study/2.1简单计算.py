# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([1, 2, 3], index=['A', 'B', 'C'])
s2 = Series([6, 7, 8, 9], index=['A', 'B', 'C', 'D'])
print(s1 + s2)  # Series 计算 可以计算加减乘, 没有的数据为nan

df1 = DataFrame(np.arange(4).reshape(2, 2), index=['A', 'B'], columns=['BJ', 'GZ'])
df2 = DataFrame(np.arange(9).reshape(3, 3), index=['A', 'B', 'C'], columns=['BJ', 'GZ', 'SH'])
print(df1 + df2)  # DataFrame计算，可加减乘
