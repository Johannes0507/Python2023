# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:07:55 2023

@author: USER
"""

from PIL import Image

import pytesseract

# 先找到要便是文字的圖片檔
fileName = 'download.png'

# r 的意思是裡面如果有特殊符號繼續運行
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

img = Image.open(fileName)

# lang 代表辨識語言 config 1. -c tessdit_char_whitelist白名單判斷 2.--psm X 參數控制識別文本   
text = pytesseract.image_to_string(img, lang='eng', config="-c tessdit_char_whiltelist=0123456789ZXCVBNMASDFGHJKLQWERTYUIOP --psm 10")

print(text.strip())