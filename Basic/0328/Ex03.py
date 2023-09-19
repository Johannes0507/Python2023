# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:17:37 2023

@author: USER
"""

fruits = ['香蕉','蘋果','香瓜','西瓜']

while True:
    print("目前的水果有：" , fruits)
    
    f =  input("請輸入欲刪除的水果Enter離開：")
    
    if f == "":
        break
    
    if fruits.count(f) > 0:
        fruits.remove(f)
    else:
        print("找不到此水果")