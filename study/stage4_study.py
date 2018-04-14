#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
    list
'''

print("==========list=============")
students = ["jack", "tony", "john"]
students.append("kevin")
students.insert(1, "lisa")
students.pop()
students.pop(0)
print(students)
print(len(students))
print(students[0])
print(students[-1])

'''
    tuple
'''

print("\n==========tuple=============")
t = (1, 2, 3, 4, 5, [6, 7])
print(t[2])
print(t[-1])
t[-1][1] = 8
print(t)

'''
    练习
'''

print("\n==========练习=============")
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[-1][-1])
