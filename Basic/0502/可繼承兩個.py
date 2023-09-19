# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:09:15 2023

@author: USER
"""



class Father:
    def car(self):
        print('Father Car')
    
    def house(self):
        print('Father House')
        
class Mother():
    def car(self):
        print('Mother Car')
        
    def Clothes(self):
        print('漂亮的衣服')

# 繼承
class Son(Father,Mother):
    def school(self):
        print('Son的學校，聯成分校。')
        
    def car(self):
        print('Son Car')
   
f = Father()
s = Son()

f.car()
s.Clothes()
s.car()

