# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:06:35 2023

@author: 李旻恩
"""

def total(n1,n2,n3):
    res = 0
    for i in range(n1,n2+1,n3):
        res += i
    return res

print("計算總和")

key = input("按y開始：")

while key == 'y':
    start = int(input("開始數字："))
    end = int(input("結束位置："))
    step = int(input("間隔數字："))
    result = total(start,end,step)
    print("總和",result)
    key = input("按y繼續：")
               
             


