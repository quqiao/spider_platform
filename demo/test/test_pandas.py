# Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具
# 该工具是为了解决数据分析任务而创建的
from pandas import Series
import pandas as pd

# Series：一维数组，与Numpy中的一维array类似
# s = Series([1, 4, 'www', 'tt'])
# print(s)
# print(s.index)

s2 = Series(['wangxing','man', 24], index=['name','sex','age'])
# print(s2)
# print(s2['name'])
# s2['name'] = 'weiwei'
# print(s2)

sd = {'python': 9002, 'c++': 9001, 'c#': 9000}
# s3 = Series(sd)
# print(s3)

s4 = Series(sd, index=['java', 'python', 'c#'])
# print(s4)
# print(pd.isnull(s4))
# print(s4.isnull())

# DataFrame 是一种二维的数据结构，非常接近于电子表格或者类似 mysql 数据库的形式。
# 它的竖行称之为 columns，横行跟前面的 Series 一样，称之为 index
data = {"name": ['google', 'baidu', 'yahoo'], "marks": [100, 200, 300], "price": [1, 2, 3]}
f1 = pd.DataFrame(data)
# print(f1)
f2 = pd.DataFrame(data, columns=['name', 'price', 'marks'])
# print(f2)
# 索引自定义
f3 = pd.DataFrame(data, columns=['name', 'price', 'marks'], index=['a', 'b', 'c'])
# print(f3)
f3['name'] = 'google'
# print(f3)
# 字典套字典方式
newData = {'lang': {'first': 'python', 'second': 'java'}, 'price': {'first': 5000, 'second': 2000}}
# f4 = pd.DataFrame(newData)
# print(f4)

io = r'hezongyy_20201111.xls'
data = pd.read_excel(io, sheet_name=0)
# pd = data.head()
print(data)
