#-*-coding:utf-8-*-

import time
import datetime
import requests

#othersensorPY
import bh1750 
import dht22
import send_message
import turwater
import fourwayswitch as switch

id=''
while True:
    try:
        time=datetime.datetime.now().strftime("%Y%m%d%H%M")
        hour=datetime.datetime.now().strftime("%H")
        lL=bh1750.getlightlevel()#燈
        id, temperture , water=dht22.getDHT22()#ID,溫度,濕度
        waterLV=turwater.dat()#水的足夠或不足夠
             
        send_message.send_sensor_value(id,temperture,water,lL,waterLV)
        time.sleep(3)        
        if  19>=hour>=6:
            switch.open_light()
        else:
            switch.close_light()
        time.sleep(3)         
    except KeyboardInterrupt:
        print("關閉程式")
        break
    except :
        print('上傳失敗')
        send_message.send_message(time)
        time.sleep(60)
