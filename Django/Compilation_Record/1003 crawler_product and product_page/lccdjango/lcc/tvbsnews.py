# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

from bs4 import BeautifulSoup

from datetime import datetime

import time

import db

today = datetime.today()
today = today.strftime("%Y-%m-%d")

url = "https://news.tvbs.com.tw/realtime"

data = requests.get(url).text


soup = BeautifulSoup(data,'html.parser')

newslist = soup.find('div',class_='news_list')

allnews = newslist.find('div',class_='list')

news = allnews.find_all('li')

for item in news:
    adata = item.find('a')
    if not(adata == None):
        link = 'https://news.tvbs.com.tw' + adata.get('href')
        
        img = adata.find('img').get('data-original')
        title = adata.find('h2').text
        
        sql ="select * from news where title='{}'".format(title)
        
        db.cur.execute(sql)
        
        res = db.cur.fetchone()
        if res == None:
            sql = "insert into news(title,content,photo_url,c_date) values('{}','{}','{}','{}')".format(title,title,img,today)
            
            db.cur.execute(sql)
            db.conn.commit()
            
        
        # content = requests.get(link).text
        # sp = BeautifulSoup(content,'html.parser')
        # newsinfo = sp.find(id='news_detail_div')
        # info = newsinfo.text
        # info = info.replace('\n','')
        # print(info)

        # print(img)
        # print(title)
        # print(link)
        # print()
        # break


db.conn.close()

