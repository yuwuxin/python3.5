#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:li hang

print('题目：有1、2、3、4个数字 能组成多少个互不相同且无重复数字的三位数？都是多少！')
print('程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。')
print('程序源代码：')

d = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (j != k):
                d.append({i,j,k})
print("总数量：", len(d))
print(d)