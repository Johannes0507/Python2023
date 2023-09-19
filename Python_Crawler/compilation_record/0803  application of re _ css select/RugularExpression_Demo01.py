# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

text = "https://www.lccnet.com.tw"
text2 = "python聯成電腦python"
# .span() 找到位置
print(re.search('https', text).span())
print(re.search('lccnet', text).span())
print(re.search('python', text2).span())

print()

print(re.search('Python', text2))
# flags=re.I 略過大小寫
print(re.search('Python', text2, flags=re.I).span())
# group() 找出所有
print(re.search('python',text2).group())