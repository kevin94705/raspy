import RPi.GPIO as GPIO
import time

def open_light(RELAY_PIN):          
    GPIO.output(RELAY_PIN, GPIO.HIGH)    
    return "ON"
def close_light(RELAY_PIN):            
    GPIO.output(RELAY_PIN, GPIO.LOW)    
    return "OFF"
