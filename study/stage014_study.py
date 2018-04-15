#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import math
import os

'''
    列表生成式
'''

print("===========================简单列表生成式==================")

# 从1开始生成100个数
print(list(range(1, 101)))

# 计算100以内的偶数平方，此处pow函数必须要两个参数，原因未知
print([int(math.pow(x, 2)) for x in range(1, 101) if x % 2 == 0])

# 计算1,2,3和4,5,6可以组成的所有2位数
print([x + y for x in "123" for y in "456"])

# 列出F盘下的所有目录文件
print([d for d in os.listdir("F:\\")])

# 将dict的所有key，value生成为list
d = {"China": "Beijing", "US": "NewYork", "France": "Paris", "Mexico": "Mexico City"}
print([key + "===" + value for key, value in d.items()])

# 将list中的小写转换为大写
l = ['chn', 'us', 'hk', 'ro']
print([s.upper() for s in l])

print("===============================练习==============================")
L1 = ['Hello', 'World', 18, 'Apple', None]

# 题目要求只保留str类型
print([x for x in L1 if isinstance(x, str)])
