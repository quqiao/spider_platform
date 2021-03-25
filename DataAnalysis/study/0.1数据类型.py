# -*- coding: utf-8 -*-
# author: quqiao

# Python Number 数据类型用于存储数值
# number1 = 1.0
# number2 = 10
# print(int(number1))  # 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
# # print(long(number1))  # 长整型（long), Python3.x 版本已删除 long() 函数。
# print(float(number1))  # 浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# print(complex(number1))  # 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
# print(complex(number1, number2))

# Python 字符串
# 访问字符串中的值
# var1 = 'Hello World!'
# print(var1[4])
# print(var1[:5])
# print(var1[1:5])
# print(var1[4:])
# print(var1[-5: -1])
# 字符串更新
# var2 = 'Hello World!'
# print('更新为：', var2[:6] + "football" )
# 字符串运算符
# a = "Hello"
# b = "Python"
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
# if ("H" in a):
#     print("H 在变量 a 中")
# else:
#     print("H 不在变量 a 中")
# if ("M" not in a):
#     print("M 不在变量 a 中")
# else:
#     print("M 在变量 a 中")
# print(r'\n')
# print(R'\n')
# 字符串格式化
# print("大家好，我叫%s，今年%d岁了。" % ('小明', 10))

# python列表
# 访问列表中的值
# list1 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# print(list1[1])
# print(list1[-6])
# list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(list2[:5])
# print(list2[3:5])
# print(list2[3:])
# print(list2[-5:-1])
# print(list2[1:-5])
# 更新列表
# list3 = ['name', 'id', 'age', 'rank']
# list3[1] = 'sex'
# print(list3)
# 删除列表元素
# list4 = ['name1', 'name2', 'name3', 'name4']
# del list4[2]
# print(list4)
# 列表脚本操作符
# list5 = [1, 2, 3]
# list6 = [4, 5, 6]
# print(list5 + list6)
# print(len(list5))
# print(list5 * 3)
# print(3 in list6)
# for i in list5:
#     print(i, end='*')
# 嵌套列表
# list7 = [1, 2, [10, 20], 4, [30, 40]]
# print(list7[2][0])
# 列表函数与方法
# list8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ss = ('test', 'text', 'teet')
# print(len(list8))  # 查询列表元素个数
# print(max(list8))  # 返回列表最大值
# print(min(list8))  # 返回列表最小值
# print(list(ss))  # 将元组装换为列表
# list8.append(9)  # 在列表末尾添加新元素
# print(list8.count(9))  # 统计某个元素出现的次数
# list8.extend(list4)  # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# print(list8)
# print(list4.index('name2'))  # 从列表中找出某个值第一个匹配项的索引位置
# list4.insert(4, 'name5')  # 将对象插入列表中指定位置index
# list4.pop(0)  # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# print(list4.pop(0))  # 返回移除的值
# list8.remove('name')  # 移除列表中某个值的第一个匹配项
# list8.reverse()  # 反向列表中元素
# list8.sort(reverse=True)  # 降序排序
# list8.clear()  # 清空列表
# list9 = list8.copy()  # 复制列表
# print(list9)
# students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# students.sort(key=lambda student: student[2])  # 通过key的函数进行排序
# print(students)
list1 = [1, 2, 3, 4, 5, 3, 5, 5, 7, 8, 9, 2, 2]
a = set(list1)
print(a)
b = list(a)
print(b)


# python元组：与列表类似，不同之处在于元组的元素不能修改
# print(type((10)))   # 不加逗号，类型为整型
# print(type((1, 2, 3, 4, 5)))  # 加上逗号，类型为元组
# 访问元组
# tup1 = (10, 20, 30, 40, 50, 60)
# print(tup1[1])
# print(tup1[:5])
# print(tup1[2:4])
# print(tup1[-5:-1])
# 修改元组，元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
# tup2 = ('test1', 'test2')
# del tup2
# print(tup2)
# tup3 = tup1 + tup2
# print(tup3)  # 创建一个新的元组
# tup4 = (1, 2, 3)
# tup5 = (40, 50, 60)
# print(len(tup4))  # 计算元素个数
# print(tup4 + tup5)  # 连接
# print(tup4 * 3)  # 复制
# print(4 in tup4)  # 检查元素是否存在
# for i in tup4:  # 迭代
#     print(i)
# 元组内置函数
# print(max(tup5))  # 返回元组最大值
# print(min(tup5))  # 返回元组最小值
# print(tuple(list8))  # 将可迭代系列转化为元组
# tup = ('r', 'u', 'n', 'o', 'o', 'b')
# print(id(tup))
# tup = (1, 2, 3)
# print(id(tup))  # 绑定新的对象，重新修改内存地址

# python字典：可变容器模型，可存储任意类型对象。键（key)不可变,值（value)可变
# 访问字典里的值
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(dict['Name'])
# 修改字典里的值,key没有新建，key存在进行修改
# dict['Age'] = 10
# print(dict)
# 删除字典元素
# del dict['Name']  # 删除字典键值
# dict.clear()  # 清空字典
# del dict  # 删除字典
# print(dict)
# 字典键的特性
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# dict2 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行.

# dict3 = {['Name']: 'Runoob', 'Age': 7}
# 字典内置函数
# print(len(dict))
# print(str(dict))
# print(type(dict))
# 字典内置方法
# dict1 ={'user': 'runoob', 'num': [1, 2, 3]}
# dict2 = dict1  # 引用
# dict3 = dict1.copy()  # 返回一个字典的浅复制:深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
# dict1['user'] = 'harder'
# dict1['num'].remove(1)
# print(dict1)
# print(dict2)
# print(dict3)
# seq = ('name', 'age', 'sex')
# dict4 = dict.fromkeys(seq)
# dict5 = dict.fromkeys(seq, 'test')  # 以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
# print(dict5)
# dict6 = {"name": "harden", "age": 31, "location": "PG", "rank": 2}
# dict7 = {"sdf": "sfa", "tttt": "ssss"}
# print(dict6.get("name", "No Data"))  # 返回key的指定值，没有时返回默认值
# print(dict6.items())  # 以列表返回可遍历的(键, 值) 元组数组。
# print(dict6.keys())  # 返回一个可迭代对象，可以使用 list() 来转换为列表
# print(dict6.setdefault("name1", "ssf"))  # 类似get()方法，
# dict6.update(dict7)  # 把字典参数 dict7 的 key/value(键/值) 对更新到字典 dict6 里
# print(dict6)
# print(list(dict6.values()))  # 返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。
# dict_pop = dict6.pop("name")  # 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出
# print(dict_pop)
# dict_popitem = dict6.popitem()  # 随机返回并删除字典中的最后一对键和值。
# print(dict_popitem)
# print(dict6)

# python集合：是一个无序的不重复元素序列
basket1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# a = set('abracadabra')
# print(a)
# print('orange' in basket1)
# 集合的基本操作
# basket1.add("peach")  # 集合中添加指定元素，元素已存在则不进行任何操作
# basket1.update([1, 2], [3, 4])  # 添加元素，可以是列表，元组，字典
# basket1.remove("apple")  # 从集合中移除元素，不存在会发生错误
# basket1.discard("app")  # 从集合中移除元素,不存在不会发生错误
# basket1.clear()  # 清空集合中所有元素
# print(basket1.copy())  # 复制集合1
# print(basket1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"football", "apple", "basketball"}
# r = x.difference(y)  # 返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中
# x.difference_update(y)  # 用于移除两个集合中都存在的元素。
# print(x)
# r = x.intersection(y, z)  # 用于返回两个或更多集合中都包含的元素，即交集
# x.intersection_update(y, z)  # 用于获取两个或更多集合中都重叠的元素，即计算交集。
# r = x.isdisjoint(y)  # 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
# r = x.issubset(y)  # 判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False
# r = x.issuperset(y)  # 判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False
# r = x.symmetric_difference(y)  # 返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素
# r = x.symmetric_difference_update(y)  # 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
# r = x.union(y)  # 返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次
# print(x)
# print(r)

