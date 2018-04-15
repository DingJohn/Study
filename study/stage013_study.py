#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from collections import Iterable

'''
    迭代
'''

print("==============================list迭代=========================")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 判断一个对象是否是可迭代对象
if isinstance(l, Iterable):
    for x in l:
        print("==========>list的迭代：", x)

print("\n==============================tuple的迭代=========================")
t = (1, 3, 5, 7, 9)

for x in t:
    print("==========>tuple的迭代:", x)

print("\n==============================字符串的迭代=========================")
s = "我爱你中国"

# enumerate 可以迭代出索引和元素
for x, value in enumerate(s):
    print("==========>字符串的迭代:index:", x, "-----value:", value)

print("\n==============================dict的迭代=========================")
d = {"China": "Beijing", "US": "NewYork", "France": "Paris", "Mexico": "Mexico City"}

for x in d:
    print("==========>dict只迭代key:", x)

for value in d.values():
    print("==========>dict只迭代value:", value)

for key, value in d.items():
    print("==========>dict迭代key-value:", key, "<----->", value)

print("\n==============================迭代多个变量=========================")
# 前后个数必须一致
# for x, y, z in [(1, 2, 3), (3, 4)]:   这样子就会报错，下面就不会
for x, y, z in [(1, 2, 3), (3, 4, 6)]:
    print("==========>多变量迭代:x-->", x, ",y-->", y, ",z-->", z)
