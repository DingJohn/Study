#!/usr/bin/env python
# _*_ coding:utf-8 _*_


print("==============================简单递归计算阶乘=====================")


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


'''
    ===> fact(5)
    ===> 5 * fact(4)
    ===> 5 * (4 * fact(3))
    ===> 5 * (4 * (3 * fact(2)))
    ===> 5 * (4 * (3 * (2 * fact(1))))
    ===> 5 * (4 * (3 * (2 * 1)))
    ===> 5 * (4 * (3 * 2))
    ===> 5 * (4 * 6)
    ===> 5 * 24
    ===> 120
'''
print(fact(5))

print("\n==============================尾递归计算阶乘=====================")


def fact1(number):
    return fact2(number, 1)


def fact2(num, defalut):
    if num == 1:
        return defalut
    return fact2(num - 1, num * defalut)


'''
    ===> fact_iter(5, 1)
    ===> fact_iter(4, 5)
    ===> fact_iter(3, 20)
    ===> fact_iter(2, 60)
    ===> fact_iter(1, 120)
    ===> 120
'''

print(fact1(5))

print("\n==============================练习(汉诺塔)=====================")


def hn(n, a, b, c):
    if n == 1:
        return a + " ---> " + c
    else:
        hn(n - 1, a, c, b)
        print(a + " ---> " + b)
        hn(1, a, b, c)
        print(a + " ---> " + c)
        hn(n - 1, b, a, c)
        print(b + " ---> " + c)
    return


print(hn(2, 'A', 'B', 'C'))
