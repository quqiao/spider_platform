# -*- coding: utf-8 -*-

# NumPy(Numerical Python)是Python语言的一个扩展程序库
# 支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
# 一个强大的N维数对象ndarray
# 广播功能函数
# 整合 C/C++/Fortran 代码的工具
# 线性代数、傅里叶变换、随机数生成等功能

# Ndarray对象
# object:数组或嵌套的数列
# dtype: 数组元素的数据类型，可选
# copy: 对象是否需要复制，可选
# order: 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
# subok: 默认返回一个与基类类型一致的数组
# ndmin: 指定生成数组的最小维度
# import numpy as np
# a = np.array([1, 2, 3], ndmin=2, dtype=complex)
# print(a)

# numpy创建数组
# ndarray数组除了可以使用底层ndarray构造器来创建外，也可以通过以下几种方式来创建
# numpy.empty方法用来创建一个指定的形状（sharp),数据类型（dtype)且未初始化的数组
# import numpy as np
# x = np.empty([3, 2], dtype=float)
# print(x)
# numpy.zeros创建指定大小的数组，数组元素以0来填充
# import numpy as np
# x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
# print(x)
# numpy.ones创建指定形状的数组，数组元素以1来填充
# import numpy as np
# x = np.ones([2, 2], dtype=int)
# print(x)

# numpy从已有的数组创建数组
# numpy.asarray
# import numpy as np
# x = [(1, 2, 3), (4, 5)]
# a = np.asarray(x)
# print(a)
# numpy.frombuffer用于实现动态数组，接受buffer输入参数，以流的形式读入转化成ndarray对象
# import numpy as np
# s = b'Hello World'
# a = np.frombuffer(s, dtype='S1')
# print(a)
# numpy.fromiter方法从可迭代对象中建立ndarray对象，返回一维数组
# import numpy as np
# list = range(5)
# it = iter(list)
# x = np.fromiter(it, dtype=float)
# print(x)

# numpy从数值范围创建数组
# numpy.arange：numpy包中的使用arange函数创建数值范围并返回ndarray对象
# import numpy as np
# x = np.arange(10, 20, 2)
# print(x)
# numpy.linspace函数用于创建一个一维数组，数组是一个等差数列构成的
# import numpy as np
# a = np.linspace(1, 10, 10).reshape([10, 1])
# print(a)
# numpy.logspace函数用于创建一个等比数列
# import numpy as np
# x = np.logspace(0, 9, num=10, base=2)
# print(x)

# numpy切片和索引
# ndarray对象的内容可以通过索引或切片来访问和修改，与python中的list的切片操作一样
# import numpy as np
# x = np.arange(10)
# y = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
# print(y[0])
# print(x[2:])

# numpy高级索引
# 整数数组索引
# import numpy as np
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
# print('\n')
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = x[rows, cols]
# print("这个四角数值")
# print(y)
# 布尔索引：通过一个布尔数组来索引目标数组，通过布尔运算来获取符合指定条件的元素的元组
# import numpy as np
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
# print('\n')
# # 现在我们会打印出大于 5 的元素
# print('大于 5 的元素是：')
# print(x[x > 5])
# 花式索引：指的是利用整数数组进行索引
# import numpy as np
# x1 = np.arange(32).reshape((8, 4))
# print(x1[[4, 2, 1, 7]])

# Numpy广播(Broadcast):
# 是numpy对不同形状的数值进行数值计算的方式，对数组的算数运算通常在相应的元素上进行
# 如果两个数组a和b形状相同，即维度相同且各维度的长度相同
# import numpy as np
# a = np.array([1, 2, 3, 4])
# b = np.array([10, 20, 30, 40])
# c = a*b
# print(c)
# 当两个数组的形状不同时,自动触发广播机制
# import numpy as np
# a = np.array([1, 2, 3, 4])
# b = np.array([[10, 20, 30, 40], [100, 200, 300, 400]])
# c = a + b
# print(c)
# 4x3 的二维数组与长为 3 的一维数组相加，等效于把数组 b 在二维上重复 4 次再运算
# import numpy as np
# a = np.array([[0, 0, 0],
#            [10, 10, 10],
#            [20, 20, 20],
#            [30, 30, 30]])
# b = np.array([1, 2, 3])
# bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
# print(a + bb)

# numpy迭代数组
# numpy.nditer提供了一种灵活访问一个或者多个数组元素的方式
# import numpy as np
# a = np.arange(6).reshape(2, 3)
# print('原始数组是：')
# print(a)
# print('\n')
# print('迭代输出元素：')
# for x in np.nditer(a):
#     print(x, end=',')
# print('\n')
# 控制遍历顺序，Fortran order,即是列序优先。C order,即是行序优先
import numpy as np
a = np.arange(0, 60, 5)
a1 = a.reshape(3, 4)
print("原始数据：")
print(a1)
print('\n')
print("原始数据转置")
b = a1.T
print(b)
print('\n')
