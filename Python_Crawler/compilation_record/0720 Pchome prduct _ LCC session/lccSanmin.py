# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 21:15:07 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://member.lccnet.com.tw/'

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'Cookie': '_gcl_au=1.1.902886812.1689850094; _fbp=fb.2.1689850094745.1226075973; _ss_pp_id=78a76817559b58868421689821294845; _gid=GA1.3.99585577.1689850095; _cuid=43bfe389-ad80-45c5-9d77-6e4b9ddad734; _cuserid=; _cusertrait=%7B%7D; _ctrait=%7B%7D; _cgrpid=; _cgrptrait=%7B%7D; script_flag=fd13385c-97e5-4e21-ac73-ac7f33c5bbc8; pid=https://www.lccnet.com.tw/lccnet; _td=178c7ca4-6dc5-465a-b58f-9ed7ab3b04d8; _hjSessionUser_1446807=eyJpZCI6ImQzZTNiNWI5LTcwYjAtNWFiNC1iNzY3LTNlNTRkZDQxNGJhYSIsImNyZWF0ZWQiOjE2ODk4NTAwOTU4MzgsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1446807=eyJpZCI6IjNmOWY4ZWM1LWU1NDAtNGRmMi04YTRmLWI1NTRmODcxNmFiOCIsImNyZWF0ZWQiOjE2ODk4NTgyMDcxNzUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _uetsid=ee69e9f026ea11ee9da137e4f4489bb4; _uetvid=ee6a060026ea11eeaa42b74f11265ec4; __RequestVerificationToken=aMm_QCzveeuLo9NZtUga5566CiM-lSvQx_ZeTWr3d8Q0YPG69cNbW5Ix1SP_iJ4yTIvBhp2IpVo5KsZjozxaLDAsewWmkRZM7E0Lc5MnJwE1; _ga_QY8DQDPMSR=GS1.1.1689858206.3.0.1689858210.56.0.0; _ga_TDP4KNDS80=GS1.1.1689858206.5.0.1689858210.56.0.0; _ga=GA1.4.1192311302.1689850095; _gid=GA1.4.99585577.1689850095; _ga=GA1.1.1192311302.1689850095; adgeek_lccnet_user_id=48-1120105004; _dc_gtm_UA-8399363-4=1; _ga_RV6BDWB9GV=GS1.1.1689858210.1.1.1689858806.0.0.0'  
}

param = {
'Account': '105664962',
'Password': 'N125744452',
'RememberMe': 'false',
'__RequestVerificationToken': '7zP6Dhz63p8oeCu7z7wCqqfm_jOSOt9ZPK0WsnWcOvtdoZvjFgCAzSSiYrrTEw9Z3hqP1lvnrbLqlgOkAyvqXQS6D8sLV7b3TawtjgTaAmY1'
    }

# 記錄使用者的cookie   
session_requests = requests.session()
# 抓取資料
content = session_requests.post(url, headers=header, data=param).text

# 登入過後進入竟課程頁面
url2 = 'https://member.lccnet.com.tw/Booking'

less = session_requests.get(url2).text

print(less)

# 1.寫簽退的爬蟲　2.抓課程頁面內容
