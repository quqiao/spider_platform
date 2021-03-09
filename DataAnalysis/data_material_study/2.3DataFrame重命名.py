# -*- coding: utf-8 -*-
# author: quqiao

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(9).reshape(3, 3), index=['BJ', 'SH', 'GZ'], columns=['bj', 'sh', 'gz'])
print(df1)
