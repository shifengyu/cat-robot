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
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setwarnings(False)
    def light(a):
        if a == "open":
            GPIO.output(18, GPIO.LOW)
        if a == "close":
            GPIO.output(18, GPIO.HIGH)
except:
    print("台灯插件异常")
    logging.warning("台灯插件异常")
