#!/usr/bin/python
#coding=utf-8

import RPi.GPIO as GPIO
import time
import send_message
import datetime
PIN = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)
time=datetime.datetime.now().strftime("%Y%m%d%H%M")
def dat():
    if GPIO.input(PIN)==1:
        print("水不足夠" )
        send_message.send_message(time)
        GPIO.cleanup()        
        return 0
    else:
        print("Water enough")
        GPIO.cleanup()
        return 1
    #time.sleep(1)
    
#while True:
    #dat()
    #time.sleep(1)
