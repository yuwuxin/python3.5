#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:li hang

list = set([1, 4, 5, 7, 3, 6, 7, 9])

list_2 = set([2, 6, 0, 66, 22, 8, 4])

print(set(list), type(set(list)))

# 交集
print(list.intersection(list_2))

print(list.union(list_2))

str = '分割线'

print(str.center(100, '-'))

a = [333, 1234.5, 1, 333, -1, 66.25]
a.sort()
print(a)