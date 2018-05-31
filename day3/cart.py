#!/usr/bin/env python
# _*_coding:utf-8_*_

goods_list = [
    (1, 'Ipone', 5600),
    (2, 'Mac', 18600),
    (3, 'Watch', 10600),
    (4, 'Bike', 7500),
    (5, 'Coffee', 4600),
    (6, 'Python', 560)
]

'''# 创建或打开
fo = open('goods.txt', 'w+')

# 写入
fo.write(str(goods_list))

# 关闭
fo.close()'''

with open('goods.txt', 'w') as fo:
    fo.write(str(goods_list))

with open('goods.txt', 'r') as f:
    print(f.read())
