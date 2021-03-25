# -*- coding: utf-8 -*-
# author: quqiao

#   有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != k) and (j != k) and (i != j):
#                 print(i, j, k)

# for i in range(1, 5):
#     for j in range(10, 15):
#         for k in range(20, 25):
#             print("%d 乘以 %d 乘以 乘以 %d 等于"%(i, j, k), (i*j))

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数
# I = int(input("请输入利润："))
# if I <= 100000:
#     profit = I*0.1
#     print(profit)
# elif 100000 < I <= 200000:
#     profit = (I-100000) * 0.075 + 100000 * 0.1
#     print(profit)
# elif 200000 < I <= 400000:
#     profit = (I - 200000) * 0.05 + 100000 * 0.1 + 100000 * 0.075
#     print(profit)
# elif 400000 < I <= 600000:
#     profit = (I - 400000) * 0.03 + 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05
#     print(profit)
# elif 600000 < I <= 1000000:
#     profit = (I - 600000) * 0.015 + 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03
#     print(profit)
# elif 1000000 < I:
#     profit = (I - 1000000) * 0.01 + 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015
#     print(profit)
# i = int(input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i-arr[idx])*rat[idx]
#         print((i-arr[idx])*rat[idx])
#         i = arr[idx]
# print(r)

# 输入三个整数x,y,z，请把这三个数由小到大输出
# l = []
# for i in range(1, 4):
#     num = int(input("输入数字："))
#     l.append(num)
# l.sort()
# print(l)

# 输出 9*9 乘法口诀表
# for i in range(1, 10):
#     print()
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (i, j, i*j), end=" ")

# 题目：判断101-200之间有多少个素数，并输出所有素数。
# h = 0  # 总数
# leap = 1
# from math import sqrt
# for m in range(101, 201):
#     k = int(sqrt(m + 1))
#     print(k)
#     for i in range(2, k + 1):
#         if m % i == 0:
#             leap = 0
#             break
#     if leap == 1:
#         # print('%-4d' % m)
#         h += 1
#         if h % 10 == 0:
#             print('')
#     leap = 1
# print('The total is %d' % h)

# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# score = (int(input("请输入分数：")))
# if score >= 90:
#     print("A")
# elif 60 <= score <= 89:
#     print("B")
# elif score <= 60:
#     print("C")

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# string1 = input("输入一行字符：")
# num = 0
# alpha = 0
# space = 0
# other = 0
# for i in string1:
#     if i.isdigit():
#         num += 1
#     elif i.isalpha():
#         alpha += 1
#     elif i.isspace():
#         space += 1
#     else:
#         other += 1
# print("number is %d" % num, "alpha is %s" % alpha, "space is %s" % space, "other is %s" % other)
str1 = "1234567890abcdefg"
print(len(str1))

