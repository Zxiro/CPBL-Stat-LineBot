import datetime as dt
import requests as req
import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from transitions.extensions import GraphMachine
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextSendMessage, TextMessage, FlexSendMessage, ImageSendMessage
from pandas.plotting import table 
from .utils import send_text_message, send_image_url, send_flex_message, get_player_stat, get_team_stat
from .msg_temp import show_pic, main_menu, table, plot, show_team

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def back_league(self, event):
        text = event.message.text
        print('back_league', text)
        return text.lower() == 'league'

    def back_team_year(self, event):
        text = event.message.text
        print('back_team_year', text)
        return True

    def back_team(self, event):
        text = event.message.text
        print('back_team', text)
        return text.lower() == 'team'

    def back_start(self, event):
        text = event.message.text
        print('back_start', text)
        return text.lower() == 'start'

    def back_player(self, event):
        text = event.message.text
        print('back_player', text)
        return True

    def back_player_name(self, event):
        text = event.message.text
        print('back_player_name', text)
        return True
    
    def back_player_year(self, event):
        text = event.message.text
        print('back_player_year', text)
        return True

    def on_enter_start(self, event):
        reply_token = event.reply_token
        msg = main_menu()
        msg_to_rep = FlexSendMessage('開啟主選單', msg)
        send_flex_message(reply_token, msg_to_rep)
        return True

    def going_fsm(self, event):
        text = event.message.text
        print('going_fsm', text)
        return text.lower() == 'fsm'

    def on_enter_fsm(self, event):
        reply_token = event.reply_token
        msg = show_pic()
        msg_to_rep = FlexSendMessage('fsm', msg)
        send_image_url(reply_token, msg_to_rep)
        return True
    
    def going_player(self, event):
        text = event.message.text
        print('going_player', text)
        return text.lower() == 'player'

    def on_enter_player(self, event): #Input the player name
        send_text_message(event.reply_token, '請輸入球員名稱')
        text = event.message.text
        return text.lower() == 'player'

    def going_player_name(self, event):
        text = event.message.text
        print('going_player_name', text)
        return True

    def on_enter_player_name(self, event): #Input the player name
        text = event.message.text
        stat_ = get_player_stat(text)
        stat_ = 0
        if(type(stat_) == int):
            send_text_message(event.reply_token, '查無此人, 請輸入正確名稱!')
            return text.lower() == 'player_name'
        return text.lower() == 'player_name'

    def going_player_year(self, event):
        text = event.message.text
        print('going_player', text)
        return text.lower() == 'player_year'

    def on_enter_player_year(self, event): #Input the player name
        name = event.message.text
        send_text_message(event.reply_token, '請輸入球季年分')
        year = event.message.text
        if (type(year)== str):
            send_text_message(event.reply_token, '錯誤年分')
            return text.lower() == 'back_player_year'
        ddd = (name, year) 
        print('enter_player', text)
        print(ddd)
        return True
        stat_ = get_player_stat(text)
        if(type(stat_) == int):
            send_text_message(event.reply_token, '查無此人, 請輸入正確名稱!')
            return text.lower() == 'back_player_name'
        else:
            message = table()
            for i in range(18):
                message["body"]["contents"][2]["contents"][i]["contents"][1]["text"] = stat_[i]
            msg_to_rep = FlexSendMessage(text + "數據", message)
            send_flex_message(event.reply_token, msg_to_rep)
    
    def going_player_stat(self, event):
        text = event.message.text
        print('going_player_stat', text)
        return text.lower() == 'player_stat'

    def on_enter_player_stat(self, event): #Select player stats type
        text = event.message.text
        print('enter_player_stat', text)
        send_text_message(event.reply_token, text)
        
    def going_att(self, event):   
        text = event.message.text
        print('going_att', text)
        return text.lower() == 'att'

    def on_enter_att(self, event): #Get the players att
        text = event.message.text
        print('enter_att', text)
        send_text_message(event.reply_token, text)

    def going_def(self, event):   
        text = event.message.text
        print('going_def', text)
        return text.lower() == 'def'

    def on_enter_def(self, event): #Get the players att
        text = event.message.text
        print('enter_def', text)
        send_text_message(event.reply_token, text)  
    
    def going_team(self, event):
        text = event.message.text
        print('enter_team', text)
        return text.lower() =='team'

    def on_enter_team(self, event): #Choose which year's stat
        send_text_message(event.reply_token, '請輸入球季年分')
        text = event.message.text 
        return text.lower() =='team'

    def going_team_year(self, event):
        text = event.message.text
        print('enter_team_year', text)
        return True

    def on_enter_team_year(self, event): #Show team stat
        text = event.message.text
        print('enter_team_year', text)
        stat_ = get_team_stat(text) #Imgur Link
        if(type(stat_)== int and stat_ == 1):
            send_text_message(event.reply_token, '請輸入正確年份')
            return text.lower() == 'team_year'
        if(type(stat_)== int and stat_ == 2):
            send_text_message(event.reply_token, '查無資料, 請重新輸入!')
            return text.lower() == 'team_year'
        stat_.drop(['Rank', 'PCT', 'GB', 'Home', 'Away'], inplace = True,  axis=1)
        message = show_team()
        for i in range(4):
            tmp_list = stat_.loc[i].tolist()
            print(tmp_list)
            data = {
                "type": "box",
                "layout": "horizontal",
                "contents": []
             }
            for j in range(len(tmp_list)):
                detail_data = {
                    "type": "text",
                    "text": tmp_list[j],
                    "size": "sm",
                    "color": "#555555",
                    "flex": 1,
                    "margin": "md"
                } 
                data['contents'].append(detail_data)
            message["body"]["contents"][4]["contents"].append(data)
        msg_to_rep = FlexSendMessage("球隊戰績", message)
        send_flex_message(event.reply_token, msg_to_rep) 

    def going_league(self, event):
        text = event.message.text
        print('enter_league', text)
        return text.lower() == 'league' 

    def on_enter_league(self, event): #
        text = event.message.text
        print('enter_league', text)
        send_text_message(event.reply_token, text)     

    def going_league_yt(self, event):
        text = event.message.text
        print('enter_league_yt', text)
        return text.lower() == 'league_yt' 

    def on_enter_league_yt(self, event): #Show team stat
        text = event.message.text
        print('enter_league_yt', text)
        send_text_message(event.reply_token, text)

    
