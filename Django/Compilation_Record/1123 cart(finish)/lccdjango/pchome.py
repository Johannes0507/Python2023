# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:30:24 2023

@author: USER
"""


import requests
import json

from datetime import datetime

import db

today = datetime.today()
today = today.strftime("%Y-%m-%d")

url = "https://24h.pchome.com.tw/onsale/v5/data/data.json"

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
pchome = requests.get(url,headers=header).text    

data = json.loads(pchome)

onsale = data['OnsaleJson']

for item in onsale:
    if item ['BlockId'] == 1:
        print("3C")
    elif item['BlockId'] == 2:
        print("家電")
    elif item['BlockId'] == 3:
        print("日常")
    else:continue
        
    
    
    
    
    if item['BlockId'] == 1:
        print("3C")
        goods = item['Nodes']
        for p in goods:
            link ='https:'+ p['Link']['Url']
            onsale = p['Link']['Text2']
            price = p['Link']['Text6']
            photo ='https://fs.ecimg.tw'+ p['Img']['Src']
            title = p['Img']['Title']
            
            sql ="select * from product where name='{}'".format(title)
            
            db.cur.execute(sql)
            
            res = db.cur.fetchone()
            if res == None:
                sql = "insert into product(name,price,photo_url,link_url,c_date) values('{}','{}','{}','{}','{}')".format(title,onsale,photo,link,today)
                
                db.cur.execute(sql)
                db.conn.commit()

            
    elif item['BlockId'] == 2:
        print("家電")
        goods = item['Nodes']
        for p in goods:
            link = 'https:'+ p['Link']['Url']
            onsale = p['Link']['Text2']
            price = p['Link']['Text6']
            photo = p['Img']['Src']
            title = p['Img']['Title']
            sql ="select * from product where name='{}'".format(title)
            
            db.cur.execute(sql)
            
            res = db.cur.fetchone()
            if res == None:
                sql = "insert into product(name,price,photo_url,link_url,c_date) values('{}','{}','{}','{}','{}')".format(title,onsale,photo,link,today)
                
                db.cur.execute(sql)
                db.conn.commit()
        
    elif item['BlockId'] == 3:
        print("日常")  
        goods = item['Nodes']
        for p in goods:
            link = 'https:'+ p['Link']['Url']
            onsale = p['Link']['Text2']
            price = p['Link']['Text6']
            photo = p['Img']['Src']
            title = p['Img']['Title']
            sql ="select * from product where name='{}'".format(title)
            
            db.cur.execute(sql)
            
            res = db.cur.fetchone()
            if res == None:
                sql = "insert into product(name,price,photo_url,link_url,c_date) values('{}','{}','{}','{}','{}')".format(title,onsale,photo,link,today)
                
                db.cur.execute(sql)
                db.conn.commit()


    