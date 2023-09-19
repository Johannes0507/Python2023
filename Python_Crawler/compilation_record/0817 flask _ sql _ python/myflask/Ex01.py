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
    return render_template('index.html')


@app.route("/news")
def news():
    
    allnews = getNews()
    return render_template('news.html',**locals())
   
@app.route("/product")
def pchome():
    # 查詢product 資料表所有資料，desc -> 呈現遞減資料
    sql = "select * from product order by id desc"
    
    db.cur.execute(sql)
    allGoods = db.cur.fetchall()
    
    return render_template('Product.html', **locals())
    
    

app.run()

 