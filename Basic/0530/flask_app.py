from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('PNoucwTbPu7JhKJ9d+gDf/XSytg0stJvVoXIjEBdeCgkbU8W6pGxLsMDe59J/y85HxOAeYFF1MLiMKeO3COezDgOQGPGU8iiXDUDpl/7RtKZR6T2kuXZSBhcwX6u0Aqo8bdADsu+niNaiYp9zAA4rQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('17813cf14a46f6e612c99d8ed1462fa2')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'




def getInfo(word):
    content = {'蘋果':'醫生遠離我', '皮衣':'有名的黃先生', '聯城':'電腦補習班'}
    return content.get(word, '無法理解')




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    # 接收line傳過來的訊息
    linemsg = event.message.text

    if '空氣' in linemsg:
        response = getBike()
    
    elif '圖片' in linemsg:
        response = '圖片尋找中請稍後'    

    else:
        response = getInfo(linemsg)

    message = TextSendMessage(text=response)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
from ntpBike import getBike
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
