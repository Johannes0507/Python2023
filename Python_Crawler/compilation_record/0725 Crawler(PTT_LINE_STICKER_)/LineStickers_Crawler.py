# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:02:51 2023

@author: USER
"""

import requests

from bs4 import BeautifulSoup

import json

import urllib.request # 抓取圖片


url = 'https://store.line.me/stickershop/product/29005/zh-Hant'

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

data = requests.get(url, headers=header).text

soup = BeautifulSoup(data, 'html.parser')

li = soup.find_all('li',class_='mdCMN09Li FnStickerPreviewItem static-sticker')

i = 1
for row in li:
    
    img = row.get('data-preview')
    line = json.loads(img)
    urllib.request.urlretrieve(line['staticUrl'],str(i) + ".png")
    i += 1