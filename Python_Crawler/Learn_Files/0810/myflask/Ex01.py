# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:04 2023

@author: USER
"""

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/news")
def news():
    return "it is news"


app.run()

 