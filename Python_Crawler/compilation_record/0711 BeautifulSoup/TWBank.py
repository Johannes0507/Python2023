# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:03:53 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup


url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

header = {
    
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    
}
    
data = requests.get(url,headers=header) 
data.encoding = 'utf-8'

data = data.text

soup = BeautifulSoup(data,'html.parser')    

rate = soup.find('table')

allRate = rate.find('tbody')

trs = allRate.find_all('tr')    

for item in trs:
    tds = item.find_all('td')
    currency = tds[0].text.strip() # 去前後空白
    currency = currency.split()  # 以split 去分割空白點變成串列後，再印出。
    print(currency[0], currency[1]) 
    print(tds[1].text.strip())
    print(tds[2].text.strip())
    print(tds[3].text.strip())
    print(tds[4].text.strip())
    print()
    
# homework 去找玉山銀行匯率並且印出。