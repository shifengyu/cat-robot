import json
import os
import hashlib
TOP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def APP_ID():
    with open(TOP_DIR+"/static/"+'setting.json', 'r') as f:
        data2 = json.load(f)
    APP_ID = data2['APP_ID']
    return APP_ID
def API_KEY():
    with open(TOP_DIR+"/static/"+'setting.json', 'r') as f:
        data3 = json.load(f)
    API_KEY = data3['API_KEY']
    return API_KEY
def SECRET_KEY():
    with open(TOP_DIR+"/static/"+'setting.json', 'r') as f:
        data4 = json.load(f)
    SECRET_KEY = data4['SECRET_KEY']
    return SECRET_KEY
def appid():
    with open(TOP_DIR+"/static/"+'setting.json', 'r') as f:
        data5 = json.load(f)
    appid = data5['appid']
    return appid
def getpwssword():
    with open(TOP_DIR+"/static/"+'setting.json', 'r') as f:
        data7 = json.load(f)
    password = data7['password']
    return password
def getpost():
    with open(TOP_DIR+"/static/"+'setting.json', 'r') as f:
        data6 = json.load(f)
    post = data6['post']
    return post
def pmdl():
    with open(TOP_DIR+"/static/"+'setting.json', 'r') as f:
        data8 = json.load(f)
    pmdl = data8['pmdl']
    return pmdl
