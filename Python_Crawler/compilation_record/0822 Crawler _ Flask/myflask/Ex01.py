# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:04 2023

@author: USER
"""

from flask import Flask , render_template

from ctsnews import getNews

import db

app = Flask(__name__)

@app.route('/')
def home():
    
    allnews = getNews()[:4]
    
    sql = "select * from product order by id desc limit 4"
    db.cur.execute(sql)
    allGoods = db.cur.fetchall()
    
    sql = "select name,photo_url,link,create_date from food order by create_date limit 4"
    db.cur.execute(sql)
    db.conn.commit()
    data = db.cur.fetchall()
    
    return render_template('index.html', **locals())


@app.route("/news")
def news():
    
    allnews = getNews()
    
    return render_template('news.html',**locals())
   
    
@app.route("/product")   
def pchome():
    
    sql = "select * from product order by id desc"
    db.cur.execute(sql)
    allGoods = db.cur.fetchall()
    
    return render_template('product.html',**locals())
    

@app.route("/food")
def GetFood():
    
    sql = "select name,photo_url,link,create_date from food order by create_date"
    db.cur.execute(sql)
    db.conn.commit()
    data = db.cur.fetchall()
    
    return render_template('food.html',**locals())
    
    
    
app.run()

 