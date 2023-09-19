# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:27:50 2023

@author: USER
"""

import requests

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

url = "https://member.lccnet.com.tw/%E5%AD%B8%E7%BF%92%E8%A9%95%E5%83%B9Partial?key=105664962"

data = requests.get(url, headers=header).text

print(data)
