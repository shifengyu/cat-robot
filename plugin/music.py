import json
import requests
import os
import sys
sys.path.append("../")
from robot.playmusic import *
FILEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/temp/music.mp3'
url='https://api.sfy18178.com.cn/music/'
form={
    'input':'卡农',
    'filter': 'name',
    'type': 'kugou',
    'page': '1'
    }

header={
    'authority': 'https://api.sfy18178.com.cn',
    'method': 'POST',
    'path': '/',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7',
    'content-length': '83',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://api.sfy18178.com.cn',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

def get_music(s):
    form['input']=s
    r=requests.post(url,data=form,headers=header)
    if r.json()['code']==200:
        link=r.json()['data'][0]['url']
        mr=requests.get(link)
        with open(FILEPATH,'wb') as f:
            f.write(mr.content)
        return r.json()['data'][0]['author']+'的'+r.json()['data'][0]['title']
    else:
        return ''

def play_music(s):
    s=get_music(s)
    if s=='':
        return
    
    play(FILEPATH,'play')


    
