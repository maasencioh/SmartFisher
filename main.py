import RPi.GPIO as GPIO
import time

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)
while True:
    if GPIO.input(sensor) == False:
        print("Presence detected")
    else:
        print("Presence not detected")
GPIO.cleanup()
