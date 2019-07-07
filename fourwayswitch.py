import RPi.GPIO as GPIO
import time

RELAY_PIN = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.HIGH)

try:
    while True:
        print("Relay is on")
        GPIO.output(RELAY_PIN, GPIO.LOW)
        time.sleep(10)
        print("Relay is off")
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        time.sleep(10)
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
finally:
    GPIO.cleanup()
def open_light():
    GPIO.output(RELAY_PIN, GPIO.LOW)
    GPIO.cleanup()
    return True
def close_light():
    GPIO.output(RELAY_PIN, GPIO.HIG)
    GPIO.cleanup()
    return False