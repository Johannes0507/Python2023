# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:07:44 2023

@author: USER
"""

# 不可變型別：1.整數 2.字串 3.元祖

# 可變型別：1.串列 2.字典

# 淺複製：對於"不變形別"的行為不受影,對於"可變型別"受影響

# 深複製：對於"可變型別"與"不變型別"的行為都不受影響

import copy
list1 = [1,2,3,4,5]
list2 = [1,[2,3]]

# 淺複製 copy 

newlist1 = copy.copy(list1)
newlist2 = copy.copy(list2)

list1[0] = 100
print(list1)
print(newlist1)

list2[1][0] = 100
print(list2)
print(newlist2)

# 深複製 deepcopy

newlist3 = copy.deepcopy(list1)
newlist4 = copy.deepcopy(list2)
list2[1][1] = 99
print(list2)
print(newlist4)