import Adafruit_DHT
import datetime
import RPi.GPIO as GPIO

GPIO_PIN = 4

def getDHT22():    
    h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, GPIO_PIN)
    if h is not None and t is not None :
        id=datetime.datetime.now().strftime("%Y%m%d%H%M")
        return id,t,h
    else:
        print('dht22 讀取失敗。')
        return False

