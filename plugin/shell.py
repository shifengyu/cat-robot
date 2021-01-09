import os
def minecraft_server():
    os.system('nohup sh start_minecraft_server.sh > minecraft.log 2>&1 &')
def stop_apache():
    os.system('sudo /etc/init.d/apache2 stop')
def restart_apache():
    os.system('sudo /etc/init.d/apache2 restart')
def start_apache():
    os.system('sudo /etc/init.d/apache2 start')
