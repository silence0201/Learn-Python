#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

age = int(input('请输入你的年龄:'))

if age >= 18:
    print("成年人")
elif age >= 6:
    print("青少年")
else:
    print('孩子')
    