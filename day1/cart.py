#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:li hang

# 练习 购物车

goods_list = [
    ('Ipone', 5600),
    ('Mac', 18600),
    ('Watch', 10600),
    ('Bike', 7500),
    ('Coffee', 4600),
    ('Python', 560)
]

money = input('请输入你的薪资:')

if money.isdigit():
    money = int(money)
    while True:
        for imte in goods_list:
            print(imte)