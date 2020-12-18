import os

from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = settings.LINE_CHANNEL_ACCESS_TOKEN

def send_flex_message(reply_token, msg_to_rep):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, 
        msg_to_rep
    ) 

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, 
        TextSendMessage(text = text)
    )

def send_image_url(reply_token, msg_to_rep):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, 
        msg_to_rep
    )

'''
def send_button_message(id, text, buttons):
    pass
'''
