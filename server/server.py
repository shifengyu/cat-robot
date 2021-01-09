import tornado.ioloop
import tornado.web
import threading
import hashlib
import asyncio
import json
import sys
import os
sys.path.append("../")
from robot import read_json
from robot import soft
TOP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
gethistory_s_r = None
jineng_s_r = None
readlog_s_r = None
readlog_s_r = None
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    
    def get(self):
        global history
        history = None
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('index.html')


class LogHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('log.html', log=readlog_s_r.getlog())

class ConfigHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('config.html')
class softHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('soft.html')
class DhHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('dh.html',history=gethistory_s_r.getHistory())

class HistoryHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
        else:
            res = {'code': 0, 'message': 'ok', 'history': json.dumps(gethistory_s_r.getHistory())}
        self.write(json.dumps(res))
        self.finish()

class GetLogHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
        else:
            res = {'code': 0, 'message': 'ok', 'log': readlog_s_r.getlog()}
        self.write(json.dumps(res))
        self.finish()

class ChatHandler(BaseHandler):
    def post(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
            print('chl1..........')
        else:
            global xiaobai_s_r
            query = self.get_argument('query', '')
            sc_s = str(query)
            xiaobai_s_r.xiaobai(sc_s)
            print(sc_s)
            res = {'code': 0, 'message': 'ok'}
        self.write(json.dumps(res))
        self.finish()


class LoginHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.redirect('/')
            return
        self.render('login.html')
    def post(self):

        if hashlib.md5(str(self.get_argument('password', default='')).encode('utf-8')).hexdigest()==read_json.getpwssword():
            self.set_secure_cookie("user", self.get_argument("name"))
            self.redirect("/")
        else:
            self.write('用户名或密码错误，请尝试重新输入')
            pass
class GetReturnHandler(BaseHandler):
    def post(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
            print('chl1..........')
        else:
            global readsetting_s_r
            option = self.get_argument('option', '')
            option_s = str(option)
            data = readsetting_s_r.read(option_s)
        self.write(json.dumps(data))
        self.finish()
class SaveConfigHandler(BaseHandler):
    def post(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
            print('chl1..........')
        else:
            global readsetting_s_r
            data_s = self.get_argument('data', '')
            readsetting_s_r.write(data_s)
            res = {'code': 0, 'message': 'ok'}
        self.write(json.dumps(res))
        self.finish()
class restartConfigHandler(BaseHandler):
    def post(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
            print('chl1..........')
        else:
            global readsetting_s_r
            data_s = self.get_argument('data', '')
            if data_s == "1":
                readsetting_s_r.restart_program()
            res = {'code': 0, 'message': 'ok'}
        self.write(json.dumps(res))
        self.finish()

class softlistHandler(BaseHandler):
    def post(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
            print('chl1..........')
        else:
            data_s = self.get_argument('data', '')
            if data_s == "1":
                soft_s_r = soft.soft()
                soft_list_data = soft_s_r.getsoftlist()
            res = {'data': soft_list_data}
        self.write(json.dumps(res))
        self.finish()

class softinstallHandler(BaseHandler):
    def post(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
            print('chl1..........')
        else:
            install_data_s = self.get_argument('install_data', '')
            soft_s_r = soft.soft()
            soft_s_r.softinstall(install_data_s)
            res = {'code': 0, 'message': 'ok'}
        self.write(json.dumps(res))
        self.finish()

settings = {
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "template_path": "server/template",
    "debug":False
}

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/log", LogHandler),
        (r"/dh", DhHandler),
        (r"/history",HistoryHandler),
        (r"/chat",ChatHandler),
        (r"/getlog",GetLogHandler),
        (r"/config",ConfigHandler),
        (r"/getreturn",GetReturnHandler),
        (r"/saveconfig",SaveConfigHandler),
        (r"/restartconfig",restartConfigHandler),
        (r"/soft",softHandler),
        (r"/softlist",softlistHandler),
        (r"/softinstall",softinstallHandler)
        
    ], **settings)

app = make_app()

def start_server():
    asyncio.set_event_loop(asyncio.new_event_loop())
    app.listen(int(read_json.getpost()))
    tornado.ioloop.IOLoop.current().start()

def run(xiaobai_r,gethistory_r,readlog_r,readsetting_r):
    global xiaobai_s_r
    global gethistory_s_r
    global readlog_s_r
    global readsetting_s_r
    xiaobai_s_r = xiaobai_r
    gethistory_s_r = gethistory_r
    readlog_s_r = readlog_r
    readsetting_s_r = readsetting_r
    threading.Thread(target=start_server).start()

def hread(readlog_r):
    global readlog_s_r
    readlog_s_r = readlog_r
