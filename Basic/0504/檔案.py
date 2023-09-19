# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:11:10 2023

@author: USER
"""

# 檔案

fn = "file02.txt"
fobj = open(fn,encoding = 'UTF-8') 設定編碼為 UTF-8 才能開啟中文
data = fobj.read()
fobj.close()

print(data)

