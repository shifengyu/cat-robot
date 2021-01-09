import requests,os,urllib.request,zipfile,importlib,ssl
ssl._create_default_https_context = ssl._create_unverified_context
TOP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')
class soft:
    def getsoftlist(self):
        url = "https://download.sfy18178.com.cn/cat-robot/json/softlist.json"
        r = requests.get(url)
        a = r.json()
        c = ''
        for i in a:
            data = ''
            name = a[i]["name"]
            state = a[i]["state"]
            try:
                with open(TOP_DIR+"/plugin_lock/"+name+'.lock', 'r') as f:
                    new = f.read()
                    f.close()
                data = "<a>已安装</a>"
            except:
                data = '<a class="btlink" onclick="softinstall('+"'"+name+"'"+')">安装</a>'
            b= '<tr><td><span>'+name+'</span></td><td><span>'+state+'</span></td><td style="text-align:right">'+data+'</td></tr>'
            c +=b
        return c
    def softinstall(self,name):
        #下载lock文件
        lock_url = "https://download.sfy18178.com.cn/cat-robot/plugin/lock/"+name+".lock"
        urllib.request.urlretrieve(lock_url, '{0}{1}.lock'.format(TOP_DIR+"/plugin_lock/", name))
        #下载json文件
        json_url = "https://download.sfy18178.com.cn/cat-robot/plugin/json/"+name+".json"
        urllib.request.urlretrieve(lock_url, '{0}{1}.json'.format(TOP_DIR+"/static/", name))
        #下载zip文件
        zip_url = "https://download.sfy18178.com.cn/cat-robot/plugin/zip/"+name+".zip"
        urllib.request.urlretrieve(lock_url, '{0}{1}.zip'.format(TOP_DIR+"/temp/", name))
        #解压zip文件
        unzip_file(TOP_DIR+"/temp/"+name+".zip",TOP_DIR+"/plugin/")
        #运行安装
        data = importlib.import_module("plugin."+name)
        data.setup()
        #删除zip文件
        os.remove(TOP_DIR+"/temp/"+name+".zip")
