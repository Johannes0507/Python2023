# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

from bs4 import BeautifulSoup



url =  "https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates"


header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
data = requests.get(url,headers=header).text

soup = BeautifulSoup(data,'html.parser')   

rate = soup.find(id='exchangeRate')

trs = rate.find_all('tr')
trs = trs[2:]

for item in trs:
    tds = item.find_all('td')
    if len(tds) == 7:
        currency = tds[0].text.strip().split()
        print(currency[0])
        # print(tds[1].text.strip())
        print(tds[2].text.strip())
        print(tds[3].text.strip())
        print(tds[4].text.strip())
        print(tds[5].text.strip())
        print(tds[6].text.strip())
        print()






