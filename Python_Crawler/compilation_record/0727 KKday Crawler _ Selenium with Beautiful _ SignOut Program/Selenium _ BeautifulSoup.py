# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver

from bs4 import BeautifulSoup

import time


driverpath = "C:/Users/opjoh/OneDrive/桌面/VScode/Python_Crawler_Selenium/chromedriver.exe"
driver = webdriver.Chrome(driverpath)

url = "https://tw.buy.yahoo.com/search/product?p=apple"

# 背景等待時間 X 秒 implicitly_wait(X)
driver.implicitly_wait(3)

driver.get(url)
    
height = 800

for i in range(5):
    # 抓JaveScript 指令window.scrollTo 從 0 開始
    driver.execute_script('window.scrollTo(0,{})'.format(height))
    time.sleep(1)
    height += 800
    
soup = BeautifulSoup(driver.page_source,'html.parser')


goods = soup.find_all('a',class_='sc-1drl28c-1 hcbDur')

for item in goods:
    
    link = item.get('href')    
    title = item.find('img').get('alt')
    
    allprice = item.find('div',class_='sc-1ap2njs-0 dPpkAj')
    
    price = allprice.find_all('span',class_='eCzBYn')
    
    #for pr in price:
    #    print(pr.text)
    
    #print('特價：',price[0].text)
    intprice = price[0].text.replace('$','')
    intprice = intprice.replace(',','')
    
    
    print('特價：',intprice)
    if len(price) == 2:
        print('原價：',price[1].text)
    
    print(link)
    print(title)
    print()