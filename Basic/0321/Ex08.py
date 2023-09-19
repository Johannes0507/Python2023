# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:56:14 2023

@author: USER
"""

#print(random.random())      # 抓不會是零的浮點數

import random
ans = random.randint(1,100)         # 崁入 1 ~ 100隨機值
guess = 0

while guess != ans:
    guess = int(input("請輸入1~100："))
    if guess > ans:
        print("猜小一點！")
    elif guess < ans:
        print("猜大一點！")
        
print("猜對了")
    