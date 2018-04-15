#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
    函数的参数
'''

print("===============================默认参数====================================")


def enroll(name, age, sex='男', city='上海'):
    print("姓名：" + str(name) + "，年龄：" + str(age) + "，性别:" + str(sex) + "，地址：" + str(city))


enroll("jack", "12", "女")

enroll("tony", "10", city='北京')

print("\n==========================默认参数为可变对象============================")


def add(L=[]):
    L.append("end")
    return L


print(add())

print("\n==========================可变参数============================")


def add_sum(*number):
    sum = 0
    for x in number:
        sum = sum + x;
    return str(sum)


print(add_sum(1, 2, 3, 4, 5, 6, 7, 8))

# 当实参为list或tuple时传值方式
l = [1, 2, 4, 5, 6, 7, 8, 9]
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("实参为list：" + add_sum(*l))
print("实参为tuple：" + add_sum(*t))

print("\n==========================关键字参数============================")


def student_info(name, age, **kwargs):
    print("name:", name, ",age:", age, ",other_info:", kwargs)


# 自己传入实参
student_info("kevin", 20, address='xi\'an', sex='boy')
# 现有字典参数
d = {'first-name': 'monkey', 'date': '2017-12-02'}
student_info("kevin", 20, **d)

print("\n==========================命名关键字参数============================")


def person_info(name, age, *, city='BeiJin', job):
    print(name, age, city, job)


# 函数有几个形参就要传几个实参,如形参有默认值，则可不传对应实参
person_info('jack', 12, job='driver')

print("\n==========================组合参数============================")


def f1(a, b, c='23', *args, city, **kwargs):
    print('a:', a, 'b:', b, 'c:', c, 'args:', args, 'city:', city, 'kw:', kwargs)


def f2(a, b, *, city, age, **kwargs):
    print('a:', a, 'b:', b, 'city:', city, 'age:', age, 'kw:', kwargs)


f1('aaa', 'bbb', 'ccc', 'sss', 'sd', city='ddd', xx='fff', yy='ds')
f2('aaa', 'bbb', city='ddd', xx='fff', yy='ds', age='19')

print("\n==========================练习============================")


def product(*number):
    if len(number) == 0:
        return "请输入至少一个数字"
    else:
        pro = 1;
        for x in number:
            pro *= x;
        return pro


l = [5, 6, 7, 9]
print(product(*l))
