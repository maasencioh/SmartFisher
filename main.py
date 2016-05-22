import RPi.GPIO as GPIO
import time
import picamera

sensor = 4
camera = picamera.PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)

id = 1

while True:
    if GPIO.input(sensor) == False:
        print "Presence detected:" + str(id)
        camera.capture('imgs/blue_'+str(id)+'.jpg')
        id += 1
        time.sleep(0.5)


GPIO.cleanup()
