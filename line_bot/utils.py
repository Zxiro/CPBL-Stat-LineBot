import os
import pyimgur
import datetime as dt
import matplotlib.pyplot as plt
import requests as req
import pandas as pd
import dataframe_image as dfi
from bs4 import BeautifulSoup
from django.conf import settings
from pandas.plotting import table 
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = settings.LINE_CHANNEL_ACCESS_TOKEN


def get_player_stat(name):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'}
    res = req.get(
        'http://www.cpbl.com.tw/players.html?&offset=0&status=&teamno=&keyword='+name, 
        headers = headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    player_href = soup.find_all('a')
    get = 0
    for a in player_href:
        if(a.getText() == name): #find the html of playername
            print(a.getText())
            player_stat_herf = a.get('href')
            get = 1
            break
    if get == 0 :
        return 0
    else:
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

def get_team_stat(year):
    if int(year)> dt.datetime.now().year or year.isdigit()==False or len(year) < 4:
        return 1
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'}
    res = req.get(
        'http://www.cpbl.com.tw/standing/year/'+year+'.html?&game_no=01&year='+year, 
        headers = headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    tables = soup.find_all('table', {'class':'std_tb mix_x'}) #Get three team stat table
    if (len(tables) != 3):
        return 2
    stat_table  = tables[2] #Last table
    col = ['Rank', 'Team', 'Game', 'W-T-L', 'PCT', 'GB', 'Fubon', 'Lamigo', 'Brothers', 'Uni-lion', 'Home', 'Away']
    data = []
    stat_data = stat_table.find_all('td', {'align':'center'})
    df = pd.DataFrame(columns = col)
    i = 0
    for s in stat_data:
        data.append(s.text)
        if(len(data) == len(col)):
            df.loc[i] = data
            data = []
            i += 1
    print(df)
    return df

def get_game_stat(date):
    pass

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

