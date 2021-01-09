import sys
sys.path.append("../")
from robot.read_json import *
from robot.random_name import *
from plugin.NeteaseMusic import *
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/temp/music'
import os
import sys
def player():
    if os.path.exists(dir_path):
        if os.path.exists(dir_path+'/56.mp3') == False:
            play_ID = NeteaseMusic()  
            get_neteasemusic(play_ID)
        else:
            s = os.path.abspath(os.curdir)
            v = str(s) + str(dir_path+'/music/')
            count = 0
            for file in os.listdir(v):
                count = count+1
            m = new_random(count)
            a = str(v) + str(m) + str('.mp3')
            play(a,'play')

    else:
        os.mkdir(dir_path)
    
