# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:00:38 2023

@author: 李旻恩 123
"""

import random

gamble = []

while len(gamble) < 6: # 執行到gamble長度為6時停止
        
    i = random.randint(1,49) # 隨機取1~49的亂數
    
    if gamble.count(i) < 1: # 為什麼不能用2，是因為含有0嗎？
        gamble.append(i)

print(gamble)   # gamble

pn = []

x = int(input("輸入要兌獎的號碼有幾個："))

for i in range(x):
    
    user = int(input("請輸入對獎號碼："))
    
    if user in gamble:
        pn.append(user)
        
print(pn)
        
times = len(pn)

if times >= 2:
    print("中獎嘍！","對中號碼有",times,"個")
    
else:
    print("沒中獎。","中獎號碼有",times,"個")
    




        






    
    





    


    





