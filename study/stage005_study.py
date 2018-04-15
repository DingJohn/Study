#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
    条件判断
'''

print("=======================条件判断==========================")

age = input("please input your age:")
if int(age) < 18:
    print("your age is " + str(age) + ",you are child")
elif int(age) < 50:
    print("your age is " + str(age) + ",you are mid-life")
else:
    print("your age is " + str(age) + ",you are old age")

print("\n=======================练习==========================")

height = 1.75
weight = 70.5

BMI = weight / (height * height)
if BMI < 18.5:
    print("过轻")
elif BMI < 25:
    print("正常")
elif BMI < 28:
    print("过重")
elif BMI < 32:
    print("肥胖")
else:
    print("严重肥胖")
