# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:12:25 2023

@author: USER
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="body strikout">Test</p>', 'html.parser')

p = soup.find('p', class_='strikout').text
P_tag = soup.select('p.body.strikout')[0].text

print(P_tag)
print(p)