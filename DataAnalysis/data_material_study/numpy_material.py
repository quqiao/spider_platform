# -*- coding: utf-8 -*-
# author: quqiao

import numpy as np

list1 = [1, 2, 3, 4, 5]  # 列表
# list1 = {"111": "111", "222": "222"}  # 字典
# list1 = "abcdefghijkl"  # 字符串
# list1 = (1, 2, 3, 4, 5)
array_1 = np.array(list1)  # 一维数组
# print(array_1)
list2 = [6, 7, 8, 9, 10]
array_2 = np.array([list1, list2])  # 二维数组
print(array_2)
print(array_2.shape)  # 形状