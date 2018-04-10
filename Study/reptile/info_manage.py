#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re
from urllib import request
import reptile.dou_yu_config as config
import reptile.conditional_screening as pattern

'''
    本模块是对数据进行处理的各种方法
'''


class InfoMange:

    # 获取初步
    def __upLoad_data(self, url):
        return str(request.urlopen(url).read(), encoding="utf-8")

    # 取得视频信息
    def __get_video_info(self, data):
        return re.findall(pattern.video_info_pattern, data)

    # 获取主播名字和人气字典
    def __get_name_number_dict(self, video_info):
        anchors = []
        for anchor_info in video_info:
            name = re.findall(pattern.get_name_pattern, anchor_info)
            number = re.findall(pattern.get_number_pattern, anchor_info)
            anchor = {"name": name, "number": number}
            anchors.append(anchor)
        return anchors

    def __refine(self, name_number_dict):
        l = lambda anchor: {
            "name": anchor["name"][0].strip(),
            "number": anchor["number"][0]
        }
        return map(l, name_number_dict)

    # 排序
    def __sort(self, name):
        sorted(name, key=self.__number, reverse=True)
        return name

    def __number(self, number):
        raise1 = float(re.findall(r"\d[\.\d]*", number["number"])[0])
        if "万" in number["number"]:
            raise1 *= 10000
        return raise1

    # 展示
    def __show(self,sort_number):
        for top in range(0,len(sort_number)):
            print("第"+str(top +1)+"名："+sort_number[top]["name"]+"---------人气："+sort_number[top]["number"])

    # 展示信息的方法
    def go(self):
        data = self.__upLoad_data(config.stimulate_battlefield_info_url)
        video_info = self.__get_video_info(data)
        name_number_dict = self.__get_name_number_dict(video_info)
        name = list(self.__refine(name_number_dict))
        sort_number = self.__sort(name)
        self.__show(sort_number)


data = InfoMange()
get = data.go()
