import os
import pyimgur
import scrapy
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


def search_player(name):
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
        return 0 #Can't get the player data
    return player_stat_herf

def get_player_stat(name, year):
    player_stat_herf = search_player(name)
    soup = BeautifulSoup(req.get('http://www.cpbl.com.tw'+ player_stat_herf).content, 'html.parser')# Into players stat page
    tables = soup.find_all('table', {'class':'std_tb mix_x'})
    table = tables[:3]
    col = ['Year', 'Team']
    data = []
    #print(table)
    for t in table: #T1 att, T2 def 13 non-req data
        col_table = t.find_all('th', {'class':'display_a1'})
        for co in col_table:
            col.append(co.text)
        detail_table = t.find_all('tr')
        i = 0
        df = pd.DataFrame(columns = col)
        for d_t in detail_table:
            stat = d_t.find_all('td', {'align':'center'})
            if len(stat) == 0:
                continue
            for k in range(2):
                data.append(stat[k].text)
            stat = d_t.find_all('td', {'class':'display_a1'})
            if len(stat) == 0:
                data = []
                continue
            for j in range(len(stat)):
                data.append(stat[j].text)
            df.loc[i] = data
            data = []
            i+=1
        break
    df = df.replace('\n','\r', regex=True)
    df = df.replace('\t', regex=True)
    print(df)
    stat_list = df.loc[df['Year'] == year]
    stat_list.reset_index(inplace = True)
    print(stat_list)
    return(stat_list)

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
    #Get home page 
    #Enter date data
    #Press search code
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'}
    res = req.get(
        'https://www.playsport.cc/livescore.php?aid=6&gamedate='+'20201016'+'&mode=1',
        headers = headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    game_box = soup.find_all('div', {'class':'gamebox gamebox_on'})
    table = soup.find('table', {'style':"margin:0 auto;"})
    row = table.find_all('tr')#0 for team name 1 for score
    names = row[0].find_all('span')
    score = row[1].find_all('td', {'class':'big_score'})
    t1 = names[0].text
    t2 = names[1].text
    t1_s = score[0].text
    t2_s = score[1].text
    print(t1, t1_s, t2, t2_s)
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

