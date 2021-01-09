import requests
import sys
sys.path.append("../")
from robot.read_json import *
import json
def dialogue(text):
    try:
        global appid1
        appid1 = str(appid())
        register_data = {"cmd": "chat", "appid": appid1, "userid": appid1 , "text": text, "location": ""}
        url = "http://idc.emotibot.com/api/ApiKey/openapi.php"
        r = requests.post(url, params=register_data)
        response = json.dumps(r.json(), ensure_ascii=False)
        jsondata = json.loads(response)
        datas = jsondata.get("data")
        for data in datas:
            result = data.get('value')
            return result
    except:
        print("你还没有说话呢")
