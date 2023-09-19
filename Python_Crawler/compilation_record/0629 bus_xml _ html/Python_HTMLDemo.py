# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 21:06:43 2023

@author: USER
"""

from bs4 import BeautifulSoup

    html_doc = """
    <html><head><title>Hello World</title></head>
    <body><h2>Test Header</h2>
    <p>This is a test.</p>
    <a id="link1" href="/my_link1">Link 1</a>
    <a id="link2" href="/my_link2">Link 2</a>
    <p>Hello, <b class="boldtext">Bold Text</b></p>
    <img src='iu.jpg'>
    
    <div id="area">
    <p>This is a test.</p>
    <a id="link1" href="/my_link1">Link 1</a>
    <a id="link2" href="/my_link2">Link 2</a>
    <p>Hello, <b class="boldtext">Bold Text</b></p>
    <img src='iu.jpg'>
    </div>
    
    </body></html>
    """

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# 抓標題 
title = soup.find('title')
h2 = soup.find('h2').text
p = soup.find_all('p')

print(title.text)
print(h2)
print(p)
print()

# get沒辦法跟text共用，一定要分開來顯示。 抓連結
a = soup.find('a')
link = a.get('href')
txt = a.text

print(a)
print(txt)
print()

# 抓圖片
img = soup.find('img').get('src')
print(img)
print()

# 抓連結位置
a_id = soup.find(id='link2')
print(a_id)

print()

textarea = soup.find(id='area')
print(textarea)
print()

tp = textarea.find('p')
print(tp)

# find抓標籤 get抓屬性
