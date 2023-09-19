# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

from bs4 import BeautifulSoup

url = "https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation"

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

param = {
   '_csrf': '6e74c0c5-82fa-4193-b4a3-e1523c50b66a',
'rideDate': '2023/07/18',
'station': '3300-臺中'
    }


data = requests.post(url,headers=header,data=param).text

soup = BeautifulSoup(data,'html.parser')

direct = soup.find(id='tab1')
retrograde = soup.find(id='tab2')

direct_tr = direct.find_all('tr')
retrograde_tr = retrograde.find_all('tr')


direct_tr = direct_tr[1:]
retrograde_tr = retrograde_tr[1:]

print("順行")
for item in direct_tr:
    tds = item.find_all('td')
    print(tds[0].text.strip().replace('\n',''))
    print(tds[1].text.strip())
    print(tds[2].text.strip())
    print(tds[3].text.strip())
    print()
    
print('-'*30)
    
    
print("逆行")
for item in retrograde_tr:
    tds = item.find_all('td')
    print(tds[0].text.strip().replace('\n',''))
    print(tds[1].text.strip())
    print(tds[2].text.strip())
    print(tds[3].text.strip())
    print()


