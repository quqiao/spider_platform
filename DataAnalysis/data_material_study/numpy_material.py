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
# print(array_2)
# print(array_2.shape)  # 形状
# print(array_2.dtype)  # 类型
array_3 = np.array([[1.0, 2.0, 3.0], [4.0, 3, 4]])
# print(array_3.dtype)  # 类型，int和float则都转换为float

# 切片一维数组
array_4 = np.arange(1, 10, 2)
# print(array_4)

# 0数组
# print(np.zeros(5))
# print(np.zeros([2, 3]))

# 单位矩阵
# print(np.eye(5))
# print(np.eye(5).dtype)

# 数组查询
# a = np.arange(1, 10)
# print(a)

# 切片查询
# print(a[1:5])

# 下标查询
# b = np.array([[1, 2, 4], [4, 5, 6]])
# print(b)
# print(b[1])
# print(b[1][0])


# 行列查询
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(c[:2, 1:])  # 第0,1行，第1,2列

# 快速创建数组
# print(np.random.randn(10))  # 符合标准的正太分布
# print(np.random.randint(10, size=20))  # 一维
# print(np.random.randint(10, size=(2, 3)))  # 二维
# print(np.random.randint(10, size=20).reshape(4, 5))  # 指定形状

# 数组运算,不要用除法, 可能会除到0
# a = np.random.randint(10, size=(4, 5))
# b = np.random.randint(10, size=(4, 5))
# print(a)
# print(b)
# print(a+b)
# print(a*b)
# print(a-b)

# 矩阵mat可以把数组转换为矩阵
# x = np.mat([[1, 2, 3], [4, 5, 6]])
# print(x)

# 矩阵求逆
# import numpy.linalg as nlg
# a = np.random.randn(3, 3)
# print(np.mat(a))
# print(nlg.inv(a))

# 求特征值和特征向量
# a = np.random.randint(10, size=9).reshape(3, 3)
# ia = nlg.inv(a)
# eig_value, eig_vector = nlg.eig(a)  # 特征值和特征向量
# print(eig_value)  # 特征值
# print(eig_vector)  # 特征向量

# 按列拼接两个向量成一个矩阵
# a = np.array((1, 2, 3))
# b = np.array((4, 5, 6))
# print(np.column_stack((a, b, a+b)))

# 在循环处理某些数据得到结果后，将结果拼接成一个矩阵是十分有用的，可以通过vstack和hstack完成
# a = np.random.randint(10, size=(2, 5))
# b = np.random.randint(10, size=(2, 5))
# c = np.hstack([a, b])
# d = np.vstack([a, b])
# print(d)

# 缺失值：缺失值在分析中也是信息的一种，NumPy提供nan作为缺失值的记录，通过isnan判定。
# a = np.random.rand(2, 2)
# a[0][1] = np.nan
# print(np.isnan(a))
# print(a)
# print(np.nan_to_num(a))

# array常用函数
# a = np.random.randint(10, size=20).reshape(4, 5)
# print(a)
# print(np.unique(a))  # 去重函数
# print(sum(a))  # 求各列的和
# print(sum(a[0]))  # 求第0行的和
# print(sum(a[:, 0]))  # 求第0列的和
# print(max(a[0]))  # 求第0行的最大值
# print(min(a[0]))  # 求第0行的最小值
# print(max(a[:, 1]))  # 求第1列的最大值
# print(min(a[:, 1]))  # 求第1列的最小值
# print(a.max())  # 矩阵的最大值
# print(a.min())  # 矩阵的最小值

# 使用pickle序列化numpy array
# import pickle
# x = np.arange(10)
# f = open('test.pkl', 'wb')
# pickle.dump(x, f)
# f = open('test.pkl', 'rb')
# pickle.load(f)

# 使用numpy
import pickle
# x = np.arange(10)
# np.save('one_array', x)
# np.load('one_array.npy')
# y = np.arange(20)
# np.savez('two_array.npz', a=x, b=y)  # 压缩多个数组
# c = np.load('two_array.npz')
# print(c['a'])
# print(c['b'])



