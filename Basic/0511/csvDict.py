# -*- coding: utf-8 -*-
"""
Created on Sat May 13 00:50:01 2023

@author: 李旻恩
"""

import csv

# 溝通大部分用csv or jason 不用excel

fileName = "dictcsv.csv"
with open(fileName,'w',encoding='utf-8',newline='') as fO:
    fields = ['name','sex','age']
    
    # 建立 Writer 的物件
    dictWriter = csv.DictWriter(fO,fieldnames=fields)
    
    # 寫入標題
    dictWriter.writeheader()
    
    dictWriter.writerow({'name':'陳美麗','sex':'女','age':'30'})
    dictWriter.writerow({'name':'陳聰明','sex':'男','age':'21'})
    
    
        
    