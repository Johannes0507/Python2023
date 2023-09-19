# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:04 2023

@author: USER
"""

from flask import Flask , render_template
from ctsnews import GetNews

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/news")
def news():
    
    allnews = GetNews()
    return render_template('news.html', **locals())
        
app.run()

 