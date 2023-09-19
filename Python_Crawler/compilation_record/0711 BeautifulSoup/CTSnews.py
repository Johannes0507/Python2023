# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:04:01 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup


url = "https://news.cts.com.tw/real/index.html"

header = {
    
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    
}
    
data = requests.get(url,headers=header)
data.encoding = 'utf-8'

data = data.text

soup = BeautifulSoup(data,'html.parser')

news = soup.find(id='newslist-top')  

allNews = news.find_all('a')

for item in allNews:
    
    link = item.get('href')
    title = item.get('title')
    
    img = item.find('img')
    if not img == None:    
        photo_url = img.get('data-src')
    else:
        photo_url = ""
    
    print(link)
    print(title)
    print(img)
    print(photo_url)
    print()