#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import math

'''
    定义函数
'''

print("========================定义函数===================")


def my_abs(x):
    return abs(x)


print("==========>测试函数-9的绝对值：" + str(my_abs(-9)))

print(2 / 3)

print("========================练习======================")


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or \
            not isinstance(b, (int, float)) or \
            not isinstance(c, (int, float)):
        return "您输入的不是数字"
    else:
        x = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
        y = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
        return x, y


a = input("请输入a的值：")
b = input("请输入b的值：")
c = input("请输入c的值：")

print(quadratic(int(a), int(b), int(c)))
