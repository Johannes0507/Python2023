# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:49:58 2023

@author: USER
"""

# 不可變型別：1.整數 2.字串 3.元祖

# 可變型別：1.串列 2.字典

# 淺複製：對於"不變形別"的行為不受影,對於"可變型別"受影響

# 深複製：對於"可變型別"與"不變型別"的行為都不受影響

number = [[10,20,30],[1,2],[2,3,4,5,6]]
print(number[1][0])
for item in number:
    for i in item:
        print(i,end = ",")
    print()