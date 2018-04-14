#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
    dict
'''

print("=======================dict===============================")

d = {"jack": "beijing", "tony": "shanghai", "lisa": "wuhan"}
# 查询key中是否有一个名为lisa的
print("lisa" in d)
# 查询d中是否有一个key为jack的，如有则返回value，如没有则返回none
print(d.get("john"))
# 修改key为lisa的值
d["lisa"] = "guang'an"
print(d["lisa"])
# 删除key为lisa的键值
d.pop("lisa")
print("lisa" in d)

'''
    set
'''
print("\n=======================set===============================")

s = set([1, 2, 2, 2, 3, 4, 5])
s1 = set([4, 5, 6, 7, 8])

# set会自动去重
print(s)
# 删除值为2的key
s.remove(2)
print(s)
# 新加一个0
s.add(0)
print(s)
# 求s和s1的交集
print(s & s1)
# 求s和s1的并集
print(s | s1)


