# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

from bs4 import BeautifulSoup


header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
url = 'https://www.taiwanlottery.com.tw/index_new.aspx'    

bingo = requests.get(url,headers=header).text

soup = BeautifulSoup(bingo,'html.parser')

bingoData = soup.find('div',class_='contents_box01')
yellowB = bingoData.find_all('div',class_='ball_tx ball_yellow')
redB = bingoData.find('div',class_='ball_red')

for row in yellowB:
    print(row.text)    
print(redB.text)    

print('-'*30)
print('雙贏彩')
print()

towin = soup.find('div',class_='contents_box06')
blueB = towin.find_all('div',class_='ball_tx ball_blue')
blueB = blueB[12:]
for row in blueB:
    print(row.text)


print('-'*30)
print('威力彩')
print()

BallWin = soup.find_all('div',class_='contents_box02')

StrongWin = BallWin[0].find_all('div',class_='ball_tx ball_green')

StrongWin = StrongWin[6:]
for row in StrongWin:
    print(row.text)
    
red = BallWin[0].find('div',class_='ball_red').text  
print('紅球：',red)
    

print('-'*30)
print('大樂透')
print()

BigWin = BallWin[2].find_all('div',class_='ball_tx ball_yellow')
BigWin = BigWin[6:]
for row in BigWin:
    print(row.text)
    
red = BallWin[2].find('div',class_='ball_red').text  
print('紅球：',red)    








