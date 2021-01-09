# -*- coding: utf-8 -*-
import logging
import os
filenamea=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/static/service.log"
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
logging.basicConfig(level=logging.DEBUG,
format=LOG_FORMAT,
datefmt = DATE_FORMAT ,
filename=filenamea
)
try:
    import serial
    serialPort = "/dev/ttyACM0"
    baudRate = 9600
    ser = serial.Serial(serialPort, baudRate, timeout=0.5)
    print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))
    def rgb(c):
        demo1=b"w"
        demo2=b"b"
        demo3=b"a"
        demo4=b"s"
        c=ord(c)
        if(c==119):
            ser.write(demo1)
        if(c==98):
            ser.write(demo2)
        if(c==97):
            ser.write(demo3)
        if(c==115):
            ser.write(demo4)
except:
    print("rgb模块异常")
    logging.warning("rgb模块异常")
