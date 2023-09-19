# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:36:07 2023

@author: 李旻恩
"""

def displayScore(**score):
    print("成績：",score)

displayScore(eng = 72,python = 5)

def showScore(name,**score):
    print(name)
    print(score)
    
showScore('JOhn',eng =  23)
    