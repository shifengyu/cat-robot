import socket
def getip():
    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname)
    return ip