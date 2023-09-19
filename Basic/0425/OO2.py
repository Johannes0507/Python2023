# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:14:49 2023

@author: USER
"""

from OO3 import Account

if __name__ == '__main__':
    
    myAcc = Account('123-234-123','Bill')
    myAcc.display()
    
    print('餘額：',myAcc.getBalance())
    
    money = int(input('輸入存款金額：'))
    
    if money <= 0:
        print('無法存錢')
    else:
        myAcc.deposit(money)    
    
    myAcc.withDraw(1)
    print('餘額：',myAcc.getBalance())