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
    time.sleep(0.5)
    if GPIO.input(sensor) == False:
        print "Presence detected:" + str(id)
        camera.capture('imgs/red_'+str(id)+'.jpg')
        id += 1


GPIO.cleanup()
