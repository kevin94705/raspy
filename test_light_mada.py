import RPi.GPIO as GPIO
import control
import time

light_BCM = 8
mada_BCM = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(light_BCM, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(mada_BCM, GPIO.OUT, initial=GPIO.LOW)

lightswitch.open_light(light_BCM)
lightswitch.open_light(mada_BCM)
print("ON")                            
time.sleep(2)

lightswitch.close_light(light_BCM)
lightswitch.close_light(mada_BCM)
print("off")
time.sleep(2)
