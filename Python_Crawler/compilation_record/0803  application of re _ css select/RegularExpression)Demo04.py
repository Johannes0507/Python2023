# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:40:15 2023

@author: USER
"""

import re

text = "find abbbbc, bc, skip, c, bbbbcc"

# *前一字元出現0次或多次

pattern = "a*b+c"

result = re.findall(pattern, text)

print(result)
# a*b* => aaaaab、aabb、ab、bbb
print()

text2 = "good 123 ya 456 lccnet 789"
result = re.findall('([a-z]+)', text2)
print(result)
print()

text3 = "year 2023 Month 08 day 03"
pattern = "[0-9]+"
result = re.findall(pattern, text3) 
print(result)
print()

pattern = "[A-Za-z]"
result = re.findall(pattern, text3)
print(result)
print()

text4 = "abb  aab abbbb "
pattern = "ab*"
result = re.findall(pattern, text4)
print(result)
print()

pattern = "a*b*c"
result = re.findall(pattern, text)
print(result)

