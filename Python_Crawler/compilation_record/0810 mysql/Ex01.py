# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:27 2023

@author: USER
"""

# 輕量型的網站服務
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "這是首頁"

@app.route("/news")
def news():
    return "新聞"

app.run()
    