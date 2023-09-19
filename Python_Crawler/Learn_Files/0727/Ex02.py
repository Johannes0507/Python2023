# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:27:28 2023

@author: USER
"""

import json
import requests

header = {

'authority':
'www.kkday.com',
'method':'GET',
'path':'/zh-tw/area_api/ajax_get_recommend_top_products?areaCode=A01-001-00019',
'scheme':'https',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-TW,zh;q=0.9',
'Cache-Control':'max-age=0',
'Cookie':'csrf_cookie_name=ccc8df3f6f678be987b03fb85a8c69a4; KKWEB=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%226ae20ca1664d7a4d6abd6f5e86522d51%22%3Bs%3A7%3A%22channel%22%3Bs%3A5%3A%22GUEST%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1690460457%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D34357e1ad0a3616cceb7720bf9d45bf5; country_lang=zh-tw; currency=TWD; KKUD=6ae20ca1664d7a4d6abd6f5e86522d51; _gcl_au=1.1.161287515.1690460459; _gid=GA1.2.1324816924.1690460463; _fbp=fb.1.1690460464028.949654893; _hjFirstSeen=1; _hjSession_628088=eyJpZCI6IjgyNTk3NzAwLTMyM2UtNGY5NC1hZTZlLTFjOWUyNjhhOGU5NyIsImNyZWF0ZWQiOjE2OTA0NjA0NjQzMzksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; rskxRunCookie=0; rCookie=45z55pyvc9fqzh7n5f6walkl4iivk; _ga_RJJY5WQFKP=GS1.1.1690460461.1.1.1690460490.31.0.0; _ga=GA1.2.1304817443.1690460462; _hjSessionUser_628088=eyJpZCI6IjcwOTMxZDhhLTg2MzYtNTc5Ni05ZWYzLTUyODJiMGFmMzUxZSIsImNyZWF0ZWQiOjE2OTA0NjA0NjQzMTksImV4aXN0aW5nIjp0cnVlfQ==; lastRskxRun=1690460493683; datadome=5EsbP_eVKPy70eXkA8yipoz7pmsDoZ2ZGI_e2_JxnktwzwAntoCOnbfSKQTK9oDXc98a1lz77VMwxwMOCAC_81u-sNSDIRCc4uKn1NhdTkEb636TXCuCsT7kv9W4Nrb4; _dd_s=rum=2&id=22956949-3e3b-4ab1-860b-76745573df6a&created=1690460457812&expire=1690461821408',
'Sec-Ch-Device-Memory':'8',
'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
'Sec-Ch-Ua-Arch':'"x86"',
'Sec-Ch-Ua-Full-Version-List':'"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.110", "Chromium";v="115.0.5790.110"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'document',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'


    }
    
url = "https://www.kkday.com/zh-tw/area_api/ajax_get_recommend_top_products?areaCode=A01-001-00019"    


data = requests.get(url,headers=header).text
travel = json.loads(data)

travel = travel['data']

for row in travel:
    title = row['name']
    info = row['introduction']
    photo = row['img_url']
    price = row['display_sale_price']
    
    
    print(title)
    print(info)
    print(photo)
    print(price)
    print()
