# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:07:41 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://tw.buy.yahoo.com/search/product'

header = {
    
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    
}
    
param = {}
p = input('請輸入產品名稱:')
param['p'] = p  

yahoo = requests.get(url, headers=header, params=param).text

soup = BeautifulSoup(yahoo, 'html.parser')

goods = soup.find_all('a', class_='sc-1drl28c-1 hcbDur')

for item in goods:
    link = item.get('href')
    title = item.find('img').get('alt')     
    allPrice = item.find('div', class_='sc-1ap2njs-0 dPpkAj')
    
    price = allPrice.find_all('span', class_='eCzBYn')
    intprice = price[0].text.replace('$','')
    intprice = intprice.replace(',','') 
    
    print(link)
    print(title)
    # print('特價：',price[0].text)
    print('特價：',intprice)
    if len(price) == 2:
        print('原價：',price[1].text)
    print()
    
    

