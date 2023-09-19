# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:07:50 2023

@author: USER
"""

class Account:
    
    def __init__(self,number,acc):  # 初始化
        # __ 物件變數私有化，只能在類別裡面更改。
        self.__number = number
        self.__account = acc 
        self.__balance = 0
        
    def display(self):  # 存帳戶
        print('帳號：',self.__number)
        print('戶名：',self.__account)
        
    def deposit(self,money):    # 存錢
        if money > 0:
            self.__balance += money
            if money >= 100000: # 利息
                self.__interest()
        else:
            raise RuntimeError('錢必須 > 0')
            #print('錢必須為正的')
            
    def withDraw(self,money):   # 領錢
        if self.__balance >= money:
            self.__balance -= money
    
    def getBalance(self):   # 查詢餘額
        return self.__balance
    
    # 物件封裝
    def __interest(self):
        interest = self.__balance * 0.002
        self.__balance += interest
    
            
