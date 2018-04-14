#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
    for...in
'''

print("==================for...in迭代list======================")
l = ["java", "python", 2, "ruby", ["c", "c++", "c#"]]
for name in l:
    print(name)

print("\n==================for...in迭代tuple======================")
t = ("uk", "us", "india", 34, ["chengdu", "shanghai", "beijing"])
for city in t:
    print(city)

print("\n===========================练习============================")
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hello," + name + "!")
