#-*-coding:utf-8-*-

import requests
#經由IFTTT送訊息到LINE
def send_message(v1):
    url = ('https://maker.ifttt.com/trigger/toline/with/key/cFsZqhoUldpnHtMk-D5G52'+'?value1='+str(v1))
    x=requests.get(url)
    print("already send message to line ")
    return
#獲得感測器的各種值，送出並插入資料庫欄位中
def send_sensor_value(id,temperture,water,light,water_level):
    sensor_value ={'id':id,'temperture':temperture,'water':water,'light':light,"water_level":water_level}    
    r = requests.get('http://163.17.9.117/insert_data_from_ras.php',params=sensor_value)
    
    if r.status_code == 200:
        return 1
    else:
        return 0

    
