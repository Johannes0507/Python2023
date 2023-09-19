# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://supertaste.tvbs.com.tw/food'

header = {
    
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    
}
    
foods = requests.get(url, headers=header).text

soup = BeautifulSoup(foods, 'html.parser')

allFoods = soup.find('div', class_='article__content')

a = allFoods.find_all('a')

for item in a:
    link = item.get('href')
    title = item.find('h3').text.strip()
    post_data = item.find('span').text.strip()
    photo_url = item.find('img').get('data-original')
    
    print(link)
    print(title)
    print(post_data)
    print(photo_url)
    print()