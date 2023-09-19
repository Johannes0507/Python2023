# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:20:53 2023

@author: USER
"""

import re

text = "John 在上課,在上課中喝Drank很快樂"

result = re.search("(.*)在上課,在上課中喝([A-Za-z]*)", text)
    
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.groups())