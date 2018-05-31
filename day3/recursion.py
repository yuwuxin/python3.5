#!/user/bin/env python
# _*_coding:utf-8_*_

def calc(val):
    print('cs=',val)
    if int(val/2) > 0:
        return calc(int(val/2))
    print('-->', val)

calc(10)