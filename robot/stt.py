from aip import AipSpeech
import sys
sys.path.append("../")
from robot.read_json import *
APP_ID = APP_ID()
API_KEY = API_KEY()
SECRET_KEY = SECRET_KEY()
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/temp/audio.wav'
 

def listen():
    # 读取录音文件
    with open(path, 'rb') as fp:
        voices = fp.read()
    try:
        result = client.asr(voices, 'wav', 16000, {'dev_pid': 1537, })
        result_text = result["result"][0]
        print("you said: " + result_text)
        return result_text
    except KeyError:
        print("KeyError")
