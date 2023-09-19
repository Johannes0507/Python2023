# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:43:03 2023

@author: USER
"""

import requests
import json

    
url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results'

header = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
   }

param = {
    'q':'可口可樂',
    'page':'1',
    'sort':'sale/dc'
    }
for i in range(1,6):
    param['page'] = str(i)
    pchome = requests.get(url, headers=header, params=param).text
    
    data = json.loads(pchome)
    prods = data['prods']
    
    for item in prods:
        name = item['name']
        price = item['price']
        originPrice = item['originPrice']
        describe = item['describe']
        prods_url = 'https://24h.pchome.com.tw/prod/' + item['Id']
        
        print('品名：',name)
        print('優惠價格：',price)
        print('原價：',originPrice)
        print('簡述：',describe)
        print('產品連結：',prods_url)
        print()
        
    print('-'*30)
    