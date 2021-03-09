# -*- coding: utf-8 -*-
# author: quqiao

#  在python中，对象赋值实际上是对象的引用。当创建一个对象，然后把它赋给另一个变量的时候，python并没有拷贝这个对象，
#  而只是拷贝了这个对象的引用

alist = [1, 2, 3, ["a", "b"]]

# （1）直接赋值,默认浅拷贝传递对象的引用而已,原始列表改变，被赋值的b也会做相同的改变
# b = alist
# alist.append(5)
# print(alist, b)

# （2）copy浅拷贝，没有拷贝子对象，所以原始数据改变，子对象会改变
# import copy
# c = copy.copy(alist)
# print(alist)
# print(c)
# alist.append("5")
# print(alist)
# print(c)
#
# alist[3].append("aaa")
# print(alist)
# print(c)  # 子对象被改变

# （3）深拷贝，包含对象里面的自对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变
# import copy
# d = copy.deepcopy(alist)
# print(alist)
# print(d)  # 始终没有改变
# alist.append(5)
# print(alist)
# print(d)  # 始终没有改变
# alist[3].append("dddd")
# print(alist)
# print(d)  # 始终没有改变

# 在Python中，对对象有一种很通俗的说法，万物皆对象。说的就是构造的任何数据类型都是一个对象，
# 无论是数字、字符串、还是函数，甚至是模块、Python都对当做对象处理
# 所有Python对象都拥有三个属性：身份、类型、值。
# name = 'test'
# print(name)  # 值
# print(type(name))  # 类型
# print(id(name))  # 身份

# 可变对象： 列表，集合，字典， 可变是指对象的值可变，身份是不变的
# 不可变对象：数字，字符串，元组，不可变对象就是对象的身份和值都不可变

# 引用
# print('引用')
# a = 18
# print(id(a))
# print(id(18))

import copy
# 浅拷贝
# print("浅拷贝：")
# b = [1, 2, 3, 4, 5]
# print("id b:", id(b))
# h = copy.copy(b)
# print("id h", id(h))
# print(h)
# h.append(6)
# print(h)
# print("id h", id(h))
# print(b)  # 浅拷贝新的列表h改变了，原来的b没变。
# b[1] = 'n'  # 列表元素改变后，新的列表也没变
# print(h)

# 深复制
print('深复制')
a = [1, 2]
l1 = [3, 4, a]
l2 = copy.deepcopy(l1)
print(l1)
print(l2)
print(id(l1))
print(id(l2))
a[0] = 11
print(id(l1))
print(id(l2))
print(l1)

