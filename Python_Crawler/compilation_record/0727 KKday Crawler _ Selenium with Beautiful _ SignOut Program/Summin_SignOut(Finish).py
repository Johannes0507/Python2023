# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:37:29 2023

@author: USER
"""

import requests

url = "https://member.lccnet.com.tw/signout/LearningRecord.aspx"

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

param = {
'關鍵字': '105664962',
'評價分數': '10',
'Item加強項目s[0].Value': 'false',
'Item加強項目s[0].Key': '1',
'Item加強項目s[1].Value': 'false',
'Item加強項目s[1].Key': '2',
'Item加強項目s[2].Value': 'false',
'Item加強項目s[2].Key': '3',
'Item加強項目s[3].Value': 'false',
'Item加強項目s[3].Key': '4',
'Item加強項目s[4].Value': 'false',
'Item加強項目s[4].Key': '5',
'Item加強項目s[5].Value': 'false',
'Item加強項目s[5].Key': '99',
'Is與我聯絡': 'false',
'授課堂數': '8',
'班級編號': '820221018212141'

    }

data = requests.post(url, headers=header, params=param).text
print(data)