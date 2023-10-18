# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:54:23 2023

@author: USER
"""

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import db

# import time
# import random 


url = "https://news.tvbs.com.tw/realtime"

data = requests.get(url).text
# print(data)
soup = BeautifulSoup(data, 'html.parser')

newslist = soup.find('div', class_='news_list')
allnews = newslist.find('div', class_='list')
news = allnews.find_all('li')

for item in news:
    a_data = item.find('a')
    
    if not(a_data == None):
        
        link = "https://news.tvbs.com.tw/" + a_data.get('href')
        img = a_data.find('img', class_='lazyimage').get('data-original')
        today = datetime.today()
        title_ = a_data.find('h2').text
        today = today.strftime('%Y%m%d')
        
        sql = f"select * from news where title='{title_}'"
        db.cur.execute(sql)
        res= db.cur.fetchone()

        if res ==None:
            
            sql = "insert into news(title, content, photo_url, c_date) value('{}', '{}', '{}', {})".format(title_, title_, img, today)
            db.cur.execute(sql)
            db.conn.commit()
        

db.cur.close()
        

        
        # 以下是抓content用的，因為顯示太多筆會被tvbs封鎖所以不沿用。
        # data_1 = requests.get(link).text
        # sp = BeautifulSoup(data_1, 'html.parser')
        # content = sp.find(id='news_detail_div').text.replace('\n', '')
        # print(content)
        

        # time.sleep(random.randint(1, 5))
