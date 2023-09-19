# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:14:43 2023

@author: USER
"""

from selenium import webdriver

from bs4 import BeautifulSoup

import time

driverpath = "c:\Chrome\chromedriver.exe"
driver = webdriver.Chrome(driverpath)

url = "https://tw.buy.yahoo.com/search/product?p=switch"

driver.implicitly_wait(3)

driver.get(url)

height = 800

for i in range(5):
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



