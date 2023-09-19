# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 21:14:40 2023

@author: USER
"""

import requests

from bs4 import BeautifulSoup


url = "https://member.lccnet.com.tw/"

param = {
'Account': '105126234',
'Password': '0976151638',
'RememberMe': 'false',
'__RequestVerificationToken': 'rEGxyIoCelbJN-5WsgZvdb1lUm1BY70fAuqo3SQ4lUINosq7uUgsgCR3aO67ME07jjjcwG9CT1PvYhhXkhSDDIEo7eNQ47wfpPnQjsZ1Usw1'
    
    }

header = {
    
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',

'Cookie':
'_ga_DT40ENJ9ZN=GS1.1.1672394509.1.0.1672394509.0.0.0; _gcl_au=1.1.155622957.1689848222; _cuid=4124f6b5-27cf-463b-a48c-90cf462cca3c; _cuserid=; _cusertrait=%7B%7D; _ctrait=%7B%7D; _cgrpid=; _cgrptrait=%7B%7D; _gid=GA1.3.78357257.1689848222; _ss_pp_id=e80b2f3ee64cccf86b01689819422381; _fbp=fb.2.1689848222391.1950675279; script_flag=fd13385c-97e5-4e21-ac73-ac7f33c5bbc8; pid=https://www.lccnet.com.tw/lccnet; _hjSessionUser_1446807=eyJpZCI6IjdmNWFkMGY3LTZmMjItNTc0Ni05MmI4LWVkNGJlY2U4NGU3MCIsImNyZWF0ZWQiOjE2NzIzOTQ1MDg2MzMsImV4aXN0aW5nIjp0cnVlfQ==; _td=d7898dc8-d6b7-43f4-8758-8a6e22e6dc6f; _uetsid=91c383f026e611eebf0a53931b785647; _uetvid=f9e5dd80882811ed967dfb443307621a; _ga_WGDWSKHG77=GS1.3.1689848804.1.1.1689848812.52.0.0; _ga_QY8DQDPMSR=GS1.1.1689848222.2.1.1689848852.60.0.0; _ga_TDP4KNDS80=GS1.1.1689848222.5.1.1689848852.60.0.0; __RequestVerificationToken=Ug_3aQ0EpdQvSlV1sM8w-Vg9eoj9By51uyDceZWdnnu2N9iTmBuHb5f6mBmwZlM4hVWMD-7YYVG5J6eNNX7WEEYRUtUcXSonVXmpoxY3wd41; _ga=GA1.1.1947480842.1672394509; _ga=GA1.4.1947480842.1672394509; _gid=GA1.4.78357257.1689848222; adgeek_lccnet_user_id=25-1101215196; _dc_gtm_UA-8399363-4=1; _ga_RV6BDWB9GV=GS1.1.1689858163.1.1.1689858857.0.0.0'
    
    }
    

session_requests = requests.session()

content = session_requests.post(url,headers=header,data=param).text

url2 = "https://member.lccnet.com.tw/Booking"  

less = session_requests.get(url2).text


soup = BeautifulSoup(less,'html.parser')

main = soup.find('ul',class_='courseListWrapper')    

alli = main.find_all('li')

print(alli[0])
    
    
    
    
    