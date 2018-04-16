#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import math
from functools import reduce

'''
    高阶函数
'''

print("==============================map()=======================")


def f(x):
    return math.pow(x, 3)


l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# 因为l列表中全是字符串，所以需要先使用map函数将其转换为int
l = map(int, l)
# 使用map函数计算l列表元素的立方
print(list(map(f, l)))

print("\n==============================map()与reduce()=======================")


def f1(x, y):
    return x * 10 + y


def f2(number):
    d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    return d[number]


# map(f2, "7659") 将7659拆开为单独的值去匹配f2中的key，并获取对应的value
print(reduce(f1, map(f2, "7659")))
