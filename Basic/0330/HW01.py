# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
scores = [100,99,80,70,89,66,50,99,99]
start = 0
while True:
    print("目前串列有：",scores)
    num = int(input("輸入欲刪除號碼,-1 exit："))
    
    if num == -1:
        break
    
    if scores.count(num) > 0:
    
        for i in range(scores.count(num)):
            index = scores.index(num,start)
            scores.pop(index)
            start = index        
       
    else:
        print("找不到")
