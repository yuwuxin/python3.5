#!/usr/bin/env python

class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=1000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        print('Game start ...')

    def shot(self):
        print('%s 手持 %s 射击' % (self.name, self.weapon))

    def got_shot(self, got_name):
        print('%s 被 %s 手持的 %s 爆了头 ' % (got_name,self.name, self.weapon)

    def buy_gun(self, name):
        print('%s GG挂了' % name)

    def __del__(self):
        print('Game end ... 重新开始!')


r1 = Role('lihang', 'jc', 'M4')
r1.shot()
r1.got_shot('lishi')
r1.buy_gun('lishi')
