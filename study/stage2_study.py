#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
    转义符的使用
'''

# \n 表示换行
print("====>I'm \n python")
# \t 表示空格，空格的个数是缩进的空格数
print("====>I'm\tpython")
# \\ 表示\
print("====>this is \\ python")
# r的使用，表示输出字符串中的转义符就只是一个字符串的意思，不做转义的操作
print(r"====>this is \\ python")
# R的使用同r
print(R"====>this is \\ python")
# 使用三引号（‘’‘ ’‘’）可以不使用\n的情况下对字符串进行换行
print('''====>this
        is
        python''')

'''
    bool运算
'''

# and运算，都为true结果才为true，否则结果为false
print("====>True and True:", True and True)
print("====>True and False:", True and False)
print("====>False and False:", False and False)

# or运算，只要有一个为true，结果就为true
print("====>True or True:", True or True)
print("====>True or False:", True or False)
print("====>False or False:", False or False)

# not运算，单目运算符，把True变成False，False变成True
print("====>not True:", not True)
print("====>not False:", not False)

# Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 12
# 此处的a是number类型，如果要做字符串的链接操作，则需要使用str()方法将a转换为字符串类型
print("====>" + str(a))
a = 'hello'
print("====>" + a)
