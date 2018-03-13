#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:li hang

import sys
import time

# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

def consumer(name):
    print('%s 准备吃包子' %name)
    while True:
        baozi = yield

        print('包子%s来啦，被%s吃了' % (baozi, name))

def producer(name):
    c = consumer('张三')
    c2 = consumer('李四')

    c.__next__()
    c2.__next__()

    print('老子开始准备做包子了!')
    for i in range(10):
        time.sleep(1)
        print('做了两个包子！')
        c.send(i)
        c2.send(i)

producer('lihang')
