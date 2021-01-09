from aip import AipSpeech
import sys
sys.path.append("../")
from robot.read_json import *
from robot.playmusic import *
import os
FILEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/temp/audio.mp3'
APP_ID = APP_ID()
API_KEY = API_KEY()
SECRET_KEY = SECRET_KEY()
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def audio(audio):
    result  = client.synthesis(audio, 'zh', 1, {
    'vol': 5,
    })

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(FILEPATH, 'wb') as f:
            f.write(result)
    play(FILEPATH,'play')
