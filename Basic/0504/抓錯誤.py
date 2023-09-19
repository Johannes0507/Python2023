# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:08:19 2023

@author: USER
"""



from datetime import datetime
import sys
import traceback    

def writeLog(errMsg):
    now = datetime.now()
    happen = now.strftime('%H:%M:%S')
    fileName = now.strftime('%Y %m %d') + ".log"
    with open(fileName,'a',encoding = 'utf-8') as fObj:
        fObj.write(happen + " " + errMsg + '\n')
    
data = ['Python','Java','聯成電腦']
try:
    print(data[0])
    print(data[3])

except Exception as ex:
    # writeLog(ex.args[0]) # args裡面有很多狀態可以抓
    cl,exc,tb = sys.exc_info()    
    lastCallStack = traceback.extract_tb(tb)[-1] # 抓最後一筆錯誤的資料
    
    fileName = lastCallStack[0]
    linenum = lastCallStack[1]  
    fucName = lastCallStack[2]
    
    msg = ex.args[0]
    error = "File：{},Line：{},Detail：{}".format(fileName,linenum,msg)
    writeLog(error) 