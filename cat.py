# -*- coding: utf-8-*-
from robot import rec
from robot import tts
from robot import stt
from robot import dialogue
from plugin import light
from plugin import music
from plugin import shell
from plugin import rgb
from plugin import ip
from plugin import getupdate
from plugin import player
from robot import read_json
from server import server
from robot import playmusic
from robot import snowboydecoder
import uuid
import sys
import signal
import fire
import hashlib
import base64
import requests
import json
import os
import socket
from robot.process_bar import *
TOP_DIR = os.path.dirname(os.path.abspath(__file__))
filelog=os.path.dirname(os.path.abspath(__file__))+"/static/service.log"
data_file = os.path.dirname(os.path.abspath(__file__)) + '/static/'
start_main_s = None
log_text = None
data_file1 = ''
global history
class History():

    def __init__(self):
        self.history = []

    def getHistory(self):
        return self.history

    def appendHistory(self, type, text):
        if type in (0,1) and text != '':
            self.history.append({'type': type, 'text': text, 'uuid': str(uuid.uuid1())})

history = History()
class setting_config():
    def read(self,a):
        try:
            global data_file1
            data_file1 = a
            with open(data_file+a,"r",encoding='utf-8') as f:
                self.text = json.load(f)
                f.close()
            return self.text
        except:
            print("无法打开文件喔")
            return "I can't find the file"
    def write(self,b):
        try:
            global data_file1
            a = data_file1
            with open(data_file+a,"w") as f:
                f.write(b)
                f.close()
        except:
            print("无法写入文件喔")
    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
class log_text():
    def getlog(self):
        with open(filelog,"r",encoding='utf-8') as f:
            self.text = f.read()
            f.close()
        return self.text
class xiaobai():
    print('''
    ********************************************************
    *          cat-robot - 语音聊天机器人                  *
    *          (c) 2020 爱因斯坦猫                         *
    ********************************************************

                后台管理端：http://{}:{}

    '''.format(ip.getip(), read_json.getpost()))
    def xiaobai(self,s):
        version =str('5.0')
        newversion=str(getupdate.get_update())
        if newversion > version:
            tts.audio('cat-robot已推出最新款，请去官网更新')
        a = "start"
        history.appendHistory(0,s)
        if s == "网易云音乐歌单。":
            a='stop'
            player.player()
        if s == "启动我的世界服务器。":
            a='stop'
            shell.minecraft_server()
        if s =="启动网站服务器。":
            a='stop'
            shell.start_apache()
        if s =="重启网站服务器。":
            a='stop'
            shell.restart_apache()
        if s =="关闭网站服务器。":
            a='stop'
            shell.stop_apache()
        if s == '打开灯带为变色模式。':
            a='stop'
            rgb.rgb('a')
        if s == '打开灯带为蹦迪模式。':
            a='stop'
            rgb.rgb('s')
        if s == '打开灯带为白色。':
            a='stop'
            rgb.rgb('w')
        if s == '关闭灯带。':
            a='stop'
            rgb.rgb('b')
        if s == "打开台灯。":
            a = "stop"
            light.light("open")
        if s == "停止播放。" or s == "停止播放":
            a = "stop"
            playmusic.play('','stop')
        if s == "关闭台灯。":
            a = "stop"
            light.light("close")
        if s[:2]=='播放':
            a = "stop"
            music.play_music(s[2:])
        if a == "start" :
            output = dialogue.dialogue(s)
            history.appendHistory(1, output)
            tts.audio(output)
    def help(self):
        print("""=====================================================================================
        python3 cat.py [命令]
        可选命令：
          md5                      - 用于计算字符串的 md5 值，常用于密码设置
          update                   - 查看cat-robot版本
        如需更多帮助，请访问：https://doc.sfy18178.com.cn
    =====================================================================================""")

    def md5(self, password):
        return hashlib.md5(str(password).encode('utf-8')).hexdigest()
        def update(self):
            version =str('5.0')
            newversion=str(get_update())
            if newversion > version:
                audio('cat-robot已推出最新款，请去官网更新')
xiaobai_s = xiaobai()
log_texta = log_text()
setting_config_s = setting_config()
interrupted = False
def signal_handler(signal, frame):
    global interrupted
    interrupted = True
def interrupt_callback():
    global interrupted
    return interrupted
def callbacks():
    global detector
    snowboydecoder.play_audio_file()
    rec.my_record()
    data = stt.listen()
    xiaobai_s.xiaobai(data)
    detector.terminate()
    wake_up()

def wake_up():
    global detector
    model = TOP_DIR+"/static/"+read_json.pmdl()
    signal.signal(signal.SIGINT, signal_handler)
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.6)
    print('Listening... please say wake-up word:SnowBoy')
    detector.start(detected_callback=callbacks, 
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    detector.terminate()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        process_bar()
        server.run(xiaobai_s,history,log_texta,setting_config_s)
        wake_up()
    elif '-h' in (sys.argv):
        xiaobai = xiaobai()
        xiaobai.help()
    else:
        fire.Fire(xiaobai)
