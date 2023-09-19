# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:02:23 2023

@author: USER
"""
import requests
from bs4 import BeautifulSoup

url = "https://tw.buy.yahoo.com/search/product"

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
    
param = {}

p = input('請輸入查詢商品：')

param['p'] = p


yahoo = requests.get(url,params=param,headers=header).text

soup = BeautifulSoup(yahoo,'html.parser')

goods = soup.find_all('a',class_='sc-1drl28c-1 hcbDur')

for item in goods:
    
    link = item.get('href')    
    title = item.find('img').get('alt')
    
    allprice = item.find('div',class_='sc-1ap2njs-0 dPpkAj')
    
    price = allprice.find_all('span',class_='eCzBYn')
    
    #for pr in price:
    #    print(pr.text)
    
    #print('特價：',price[0].text)
    intprice = price[0].text.replace('$','')
    intprice = intprice.replace(',','')
    
    
    print('特價：',intprice)
    if len(price) == 2:
        print('原價：',price[1].text)
    
    
    
    
    print(link)
    print(title)
    print()
    
    
    
    
    
    
    
    


