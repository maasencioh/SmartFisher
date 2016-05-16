import RPi.GPIO as GPIO
import time

led = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)
time.sleep(5)
GPIO.output(led, 0)
GPIO.cleanup()
