#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:li hang

import time


# print('嵌套函数')
#
# def func():
#     print('函数1')
#     def func2():
#         print('函数2')
#     func2()
# func()
#
# print('分割线'.center(100, '-'))
#
# str = '''
# 高阶函数:
#     1、一个函数作为参数传入另一个函数
#     2、返回值中包含 N个函数
#     '''
# print(str)
#
# def bar():
#     x = 1;
#     return x
#
# def bar2(y, func):
#     x = func()
#     v = x + y
#     return v
#
# res = bar2(2, bar)
# print(res, '\n')
#
#
# def bar3():
#     print('in the bar')
#
# def foo(func):
#     return func
#
# foo(bar3)()
#
# print('分割线'.center(100, '-'))

# print('内嵌函数+高阶函数+闭包=》装饰器')

# print('范例一：函数参数固定')
#
# def decorartor(func):
#     def wrapper(n):
#         print('starting')
#         func(n)
#         print('stopping')
#     return wrapper
#
#
# def test(n):
#     print('in the test arg is %s' % n)
#
# decorartor(test)('alex')

# print('范例二：函数参数不固定')
#
# def decorartor(func):
#     def wrapper(*args, **kwargs):
#         print('start...')
#         func(*args, **kwargs)
#         print('end...')
#     return wrapper
#
# def test(n, x=1):
#     print('in the test arg is %s' %n)
#
# decorartor(test)('cq', x = 2)

# print('无参装饰器')
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('run start ...')
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print('run end ...','\n')
#         print('run time is %s', (end_time - start_time))
#     return wrapper
# @decorator
# def test(data):
#     for i in data:
#         key = i+1
#         time.sleep(1)
#         print('-'*key, key)
#
# test(range(10))

def timer(timeout=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            stop = time.time()
            print('run time is %s ' % (stop - start))

            print(timeout)

        return wrapper

    return decorator


@timer(2)
def test(list_test):
    for i in list_test:
        time.sleep(0.1)
        print('-' * 20, i)


# timer(timeout=10)(test)(range(10))
test(range(10))
