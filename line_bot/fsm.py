import requests as req
import pandas as pd
from abc import ABC, abstractmethod
from transitions.extensions import GraphMachine
from bs4 import BeautifulSoup
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextSendMessage, TextMessage, FlexSendMessage
from .utils import send_text_message, send_image_url, send_flex_message
from .msg_temp import show_pic, main_menu, table

def get_player_stat(name):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'}
    res = req.get(
        'http://www.cpbl.com.tw/players.html?&offset=0&status=&teamno=&keyword='+name, 
        headers = headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    player_href = soup.find_all('a')
    get = 0
    for a in player_href:
        #print(a)
        if(a.getText() == name): #find the html of playername
            print(a.getText())
            player_stat_herf = a.get('href')
            get = 1
            break
    if get == 0 :
        return 0
    else:
        #print(player_stat_herf)
        soup = BeautifulSoup(req.get('http://www.cpbl.com.tw'+ player_stat_herf).content, 'html.parser')# Into players stat page
        tables = soup.find_all('table', {'class':'std_tb mix_x'})
        table = tables[:3]
        col = ['年分', '隊伍', '出賽場數', '打席', '打數', '打點', '得分', '安打', '一壘安打', '二壘安打', '三壘安打', '全壘打', '壘打','被三振', '保送', 'OBP', 'SLG', 'AVG']
        data = []
        df = pd.DataFrame(columns = col)
        #print(table)
        for t in table: #T1 att, T2 def 13 non-req data
            detail_table = t.find_all('tr')
            i = 0
            for d_t in detail_table:
                print(d_t)
                data = []
                stat = d_t.find_all('td', {'align':'center'})
                print(stat)
                if(len(stat)-13 == len(col)):
                    for j in range(len(col)):
                        data.append(stat[j].text)
                    df.loc[i] = data
                i += 1
                print(df)
                
            print(df)
            break
        print(df)
        return(df)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def back_league(self, event):
        text = event.message.text
        print('back_league', text)
        return text.lower() == 'league'

    def back_league_year(self, event):
        text = event.message.text
        print('back_league_year', text)
        return text.lower() == 'league_year'

    def back_year(self, event):
        text = event.message.text
        print('back_year', text)
        return text.lower() == 'year'        

    def back_team_year(self, event):
        text = event.message.text
        print('back_year', text)
        return text.lower() == 'team_year'

    def back_team(self, event):
        text = event.message.text
        print('back_team', text)
        return text.lower() == 'team'

    def back_start(self, event):
        text = event.message.text
        print('back_start', text)
        return text.lower() == 'start'

    def back_options(self, event):
        text = event.message.text
        print('back_options', text)
        return text.lower() == 'options'

    def back_player(self, event):
        text = event.message.text
        print('back_player', text)
        return text.lower() == 'player'

    def going_fsm(self, event):
        text = event.message.text
        print('going_fsm', text)
        return text.lower() == 'fsm'

    def on_enter_start(self, event):
        reply_token = event.reply_token
        msg = main_menu()
        msg_to_rep = FlexSendMessage('開啟主選單', msg)
        send_flex_message(reply_token, msg_to_rep)
        return text.lower() == 'start'

    def on_enter_fsm(self, event):
        reply_token = event.reply_token
        msg = show_pic()
        msg_to_rep = FlexSendMessage('fsm', msg)
        send_image_url(reply_token, msg_to_rep)
        return text.lower() == 'start'
    
    def going_option(self, event):
        text = event.message.text
        print('going_option', text)
        return text.lower() == 'options'

    def on_enter_options(self, event): #Choose to player/Team/League
        text = event.message.text
        print('enter_option', text)
        send_text_message(event.reply_token, text)
        return True

    def going_player_name(self, event):
        text = event.message.text
        print('going_player', text)
        return text.lower() == 'player_name'

    def on_enter_player_name(self, event): #Input the player name
        send_text_message(event.reply_token, '請輸入球員名稱')
        text = event.message.text 
        return text

    def going_player(self, event):
        text = event.message.text
        print('going_player', text)
        return True

    def on_enter_player(self, event): #Input the player name
        text = event.message.text
        print('enter_player', text)
        stat_ = get_player_stat(text)
        if(type(stat_) == int):
            send_text_message(event.reply_token, '請輸入正確名稱')
            return text.lower() == 'player_name'
        else:
            message = table()
            for i in range(18):
                message["body"]["contents"][2]["contents"][i]["contents"][1]["text"] = stat_[i]
            msg_to_rep = FlexSendMessage("查詢即時值", message)
            send_flex_message(event.reply_token, msg_to_rep)
    
    def going_year(self, event):
        text = event.message.text
        print('going_year', text)
        return text.lower() == 'year'
    
    def on_enter_year(self, event): #Input the player name
        text = event.message.text
        print('enter_year', text)
        send_text_message(event.reply_token, text) 
    
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
        return text.lower() == 'team' 

    def on_enter_team(self, event): #Choose which team
        text = event.message.text
        print('enter_team', text)
        send_text_message(event.reply_token, text) 

    def going_team_year(self, event):
        text = event.message.text
        print('enter_team_year', text)
        return text.lower() == 'team_year' 

    def on_enter_team_year(self, event): #Choose team year
        text = event.message.text
        print('enter_team_year', text)
        send_text_message(event.reply_token, text)

    def going_team_stat(self, event):
        text = event.message.text
        print('enter_team_stat', text)
        return text.lower() == 'team_stat' 

    def on_enter_team_stat(self, event): #Show team stat
        text = event.message.text
        print('enter_team_stat', text)
        send_text_message(event.reply_token, text)

    def going_league(self, event):
        text = event.message.text
        print('enter_league', text)
        return text.lower() == 'league' 

    def on_enter_league(self, event): #
        text = event.message.text
        print('enter_league', text)
        send_text_message(event.reply_token, text)     

    def going_league_year(self, event):
        text = event.message.text
        print('enter_league_year', text)
        return text.lower() == 'league_year' 

    def on_enter_league_year(self, event): #Show team stat
        text = event.message.text
        print('enter_league_year', text)
        send_text_message(event.reply_token, text)  

    def going_league_stat(self, event):
        text = event.message.text
        print('enter_league_stat', text)
        return text.lower() == 'league_stat' 

    def on_enter_league_stat(self, event): #Show team stat
        text = event.message.text
        print('enter_league_stat', text)
        send_text_message(event.reply_token, text)

    def going_league_yt(self, event):
        text = event.message.text
        print('enter_league_yt', text)
        return text.lower() == 'league_yt' 

    def on_enter_league_yt(self, event): #Show team stat
        text = event.message.text
        print('enter_league_yt', text)
        send_text_message(event.reply_token, text)

    
