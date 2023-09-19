# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 02:17:35 2023

@author: 李旻恩
"""





def interest(rate):
    global money    # 全域變數只能在函式裡設定
    money = 20
    inter = money * rate
    print("利息為：",inter)
    
interest(0.5)
print(money)

