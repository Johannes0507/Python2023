# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:18:36 2023

@author: USER
"""

from bs4 import BeautifulSoup
import re

html = """
<div class="content">
E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
<ul class="price">定價：360 元 </ul>
<img src="http://test.com.tw/p1.jpg">
<img src="http://test.com.tw/p2.jpg">
<img src="http://test.com.tw/p3.png">
</div>
"""

# pattern = ""

soup = BeautifulSoup(html, 'html.parser') 
# select => CSS 選擇器
data =  soup.select('.price')[0].text
print(data)

result = re.findall('[0-9]+', data)
print(result[0])
# r => 不轉役  \. => 
emails = re.findall(r"[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+", html)

for email in emails:
    print(email)