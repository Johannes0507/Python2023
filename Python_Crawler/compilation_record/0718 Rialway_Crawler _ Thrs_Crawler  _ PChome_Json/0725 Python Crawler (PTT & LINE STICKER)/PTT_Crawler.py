# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:41:10 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup


url = "https://www.ptt.cc/bbs/Beauty/index.html"

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'cookie':'over18=1'

    }

soup = BeautifulSoup('', 'html.parser')
for i in range(1,6):
    
    if i > 1:
        uppage = soup.find_all('a', class_='btn wide')
        url = 'https://www.ptt.cc' + uppage[1].get('href')
        
    data = requests.get(url, headers=header).text
    
    soup = BeautifulSoup(data, 'html.parser')
    
    Beauty = soup.find_all('div', class_='r-ent')
    
    for item in Beauty:
        
        a = item.find('a')
        
        if not (a==None):

            Title = item.find('a').text
            Link = item.find('a').get('href')   
                
            print('標題:',Title)
            print('連結:',Link)
    
