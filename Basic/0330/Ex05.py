# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:21:15 2023

@author: USER
"""

content = {"A":"內向","B":"樂觀","O":"自信","AB":"負責"}
blood = input("請輸入血型:")
blood = blood.upper()   # upper()英文轉大寫 lower()英文轉小寫 
if content.get(blood) == None:
    print("找步道血型：",blood)
else:
    print(blood,content[blood])