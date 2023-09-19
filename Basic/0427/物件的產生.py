# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:40:21 2023

@author: USER
"""

class myClass:
    def __new__(kind,name): # 建構物建
        if name != '':
            print('建立物件')
            return object.__new__(kind)
        else:
            print('未建構')
            return None

    def __init__(self,name):
        print('物件初始化')
        print(name)
        
x = myClass('')
print()
y = myClass('Bill')

# 物件的產生 new -> init

