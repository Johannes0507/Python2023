# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:19:37 2023

@author: USER
"""

# 正則表達式
# [a-z] 任何小寫 [A-Z] 任何大寫 [A-Z a-z 0-9] 大小寫與數字 [^0-9] 除數字之外


import re

text = "https://www.lccnet.com.tw"
text2 = 'python聯成電腦'

print(re.match('https', text))
print(re.match('https', text).span())
print(re.match('lccnet', text2))
# re.I 略過大小寫
print(re.match('Python', text2))
print(re.match('Python', text2, flags=re.I))

