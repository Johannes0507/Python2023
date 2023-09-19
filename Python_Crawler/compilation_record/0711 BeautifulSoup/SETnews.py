# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup


url = "https://www.setn.com/ViewAll.aspx?PageGroupID=0&utm_source=setn.com&utm_medium=menu&utm_campaign=hotnews&pk_vid=cfeaaa34106a8b051689075379ec10c6"

header = {
    
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

}
    
data = requests.get(url,headers=header).text

soup = BeautifulSoup(data,'html.parser')

news = soup.find(id="NewsList") 

allNews = news.find_all('h3')

for item in allNews:

    link = item.find('a').get('href')
    
    if not( 'http' in link):
        link = "https://www.setn.com/" + link
    
    
    title = item.find('a').text
    print(link)
    print(title)
    print()
