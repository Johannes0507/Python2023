# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:11:19 2023

@author: USER
"""

# Yahoo購物產品資訊

# 導入 requests、BeautifulSoup、json
import requests

from bs4 import BeautifulSoup

import json


url = "https://tw.buy.yahoo.com/search/product?p=switch"

# 模擬瀏覽器
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

# 
data = requests.get(url, headers=header).text

# 使用BeautifulSoup 的HTML解析器
soup = BeautifulSoup(data,'html.parser')

# 找出所有產品內容
goods = soup.find_all('a',class_='sc-1drl28c-1 hcbDur')

# 找尋json檔案
allimg = soup.find(id='isoredux-data').get('data-state')

# 把json寫成文字檔到 online json parser 搜尋相關參數
# with open('yahoo.txt','w',encoding='utf-8') as o:
#     o.write(allimg)
    
# 解析json
images = json.loads(allimg)

# 尋找圖片網址
pimg = images['search']['ecsearch']['hits']


for item in goods:
    
    # 產品連結
    link = item.get('href')    
    # 產品名稱
    title = item.find('img').get('alt')
    
    # 印出產品連結
    for row in pimg:
        # 判斷json檔裡面是否
        if link == row['ec_item_url']:
            yaphoto = row['ec_image']
            break
    
    allprice = item.find('div',class_='sc-1ap2njs-0 dPpkAj')
    price = allprice.find_all('span',class_='eCzBYn')
    intprice = price[0].text.replace('$','')
    intprice = intprice.replace(',','')
    
    
    print('特價：',intprice)
    if len(price) == 2:
        print('原價：',price[1].text)
    
    
    print(link)
    print(title)
    print('圖片：',yaphoto)
    print()