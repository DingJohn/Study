#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
    此模块主要是对内容进行筛选
'''

# 第一层筛选正则，主要筛选出各个主播的信息（主播名和人气指数）
video_info_pattern = '<div class="video-info">([\s\S]*?)</div>'

# 第二层筛选正则，筛选主播的名字和人气指数
get_name_pattern = '</i>([\s\S]*?)</span>'
get_number_pattern = '<span class="video-number">([\s\S]*?)</span>'
