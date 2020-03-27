#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 下午11:38
# @Author  : silence
# @File    : pppd.py
# @Project : Sample

import requests
from lxml import etree

# 怼人表情包网址http://www.doutula.com/search?type=photo&more=1&keyword=%E6%80%BC%E4%BA%BA&page=8
# 规律一眼就发现是改个数字就行了，就用for i inrange（）

for i in range(1, 50):  # 上次给女朋友发了20000句情话，你们说发的太多，所以这次就爬50页，也就50*72=3600个表情包，打败她应该够了，不够再爬
    url = "http://www.doutula.com/search?type=photo&more=1&keyword=%E6%80%BC%E4%BA%BA&page=" + str(i)  # 用数字拼接网址
    res = requests.get(url).text  # 用requests.get（）函数获得拼接网址的数据
    # print(res)    #打印显示一下
    res_xpath = etree.HTML(res)  # 转换为xpath可用的格式
    # 用xpath提取表情包的具体网址
    bqb_urls = res_xpath.xpath('//*[@id="search-result-page"]/div/div/div[2]/div/div[1]/div[1]/div//img/@data-original')
    for bqb_url in bqb_urls:  # 依次循环提取表情包网址
        try:
            res = requests.get(bqb_url).content  # 获得二进制数据
            file_name = bqb_url.split('/')[-1]  # 表情包名字就取网址中的最后一个
            with open(file_name, 'wb') as f:  # 用“wb”模式打开，没有就新建，肯定是需要自动新建的
                f.write(res)  # 将获得的二进制数据写到文件中
        except:
            pass  # 3600个，失败几个无所谓的，不在乎
print("表情包爬取完成，准备战斗吧！")