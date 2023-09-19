# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:30:03 2023

@author: USER
"""

import db

import json

import requests

url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=2000"

data = requests.get(url).text

bike = json.loads(data)

for item in bike:
    station = item['sna']
    
    sql = "select * from ntpbike where station='{}'".format(station)
    
    db.cur.execute(sql)
    
   
    row = db.cur.fetchone()
    
    
    

    if row is None:
        
        sql = "insert into ntpbike(station,tot,rent,space,area,address,lat,lng) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(item['sna'],item['tot'],item['sbi'],item['bemp'],item['sarea'],item['ar'],item['lat'],item['lng'])
        
        db.cur.execute(sql)
        db.conn.commit()
                
    else:
        
        sql = "update ntpbike set rent='{}' , space='{}' where station='{}' ".format(item['sbi'],item['bemp'],item['sna'])
        db.cur.execute(sql)
        db.conn.commit()
                        
        
        
    
    
db.conn.close()    
        


    