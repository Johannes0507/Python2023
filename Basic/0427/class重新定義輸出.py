# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:16:11 2023

@author: USER
"""

class myBirth:
    def __init__(self,name,y,m,d):
        self.name = name
        self.year = y
        self.month = m
        self.day = d
    
    # 重新定義方法
    
    # 呼叫字串輸出(給使用者看)
    def __str__(self):   
        print(self.name,'你好')
        return '生日：' + str(self.year) + '年' + str(self.month) + '月' + str(self.day) + '日'
    
    # 呼叫format輸出(給開發者看)
    def __repr__(self):
        return '{}年{}月{}日'.format(self.year,self.month,self.day)
        
birth = myBirth('Bill',1998,5,7)

print(birth) # 使用者

print(repr(birth)) # 開發者



