#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
    字符串
'''

# encode()的使用，将“中国”二字转换为utf-8编码的bytes
print("中国".encode("utf-8"))
# decode()的使用，将bytes内容转换为指定编码的str，无需加r,如不确定待转bytes是否正确，
# 可加errors="ignore"忽略错误字节
print("====>" + b'\xe4\xb8\xad\xe5\x9b'.decode("utf-8", errors="ignore"))
# 计算字符串的长度,包含空格
print("====>" + str(len("this is china！")))
# 如果是bytes，则计算字节的长度
print("====>" + str(len(b"\xe4\xb8\xad\xe5\x9b")))

'''
    占位符
'''
print("====>%d" % 3)
# 2表示空几格
print("====>%2d" % 3)
print("====>%f" % 3.12)
# .2表示小数点后仅保留两位,过5进1
print("====>%.2f" % 3.126)
print("====>%s" % 3)

'''
    练习
'''
s1 = 72
s2 = 85
print("====>format方法：今年较去年提升了{0:.1f}%".format((s2 - s1) / s1 * 100))
print("====>占位符方法：今年较去年提升了%.1f" % ((s2 - s1) / s1 * 100))
