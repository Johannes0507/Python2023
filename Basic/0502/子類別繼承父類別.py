# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Father:
    def car(self):
        print('Father Car')
    
    def house(self):
        print('Father House')

class Son(Father):
    def car(self):
        print('Son Car')
    
    def school(self):
        print('Son的學校，聯成分校。')


son = Son()

print()

son.car()
son.school()

print()

s2 = Son()
s2.car()
s2.school()

