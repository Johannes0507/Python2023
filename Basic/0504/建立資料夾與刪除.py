# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:39:23 2023

@author: USER
"""

import os # os系統

myDir = "lcc"   # 可以在這裡指定位置

if os.path.exists(myDir):   # 判斷此路徑是否存在
    os.rmdir(myDir) # os.rmdir => 移除
    print('已刪除')
    
else:
    os.mkdir(myDir) # 建立資料夾myDir
    