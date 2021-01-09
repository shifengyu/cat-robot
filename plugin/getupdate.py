import requests
def get_update():
    r = requests.get('https://api.sfy18178.com.cn/cat-update.php')
    r.encoding='utf-8'
    a =r.json()
    s = a['versioninfo']['version']
    return s
