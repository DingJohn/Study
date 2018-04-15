#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import math

'''
    生成器
'''

print("============================生成器=========================")

# 这就是一个简单的生成器g，与列表生成式的区别在于括号，生成器是()
g = (math.pow(x, 2) for x in range(1, 10))
print(g)
for x in g:
    print(x)


def f1(x):
    n, y, z = 0, 0, 1
    while n < x:
        yield z
        y, z = z, y + z
        n += 1
    return 'done'


print(f1(10))

for x in f1(10):
    print(x)
