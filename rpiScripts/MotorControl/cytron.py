import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

AN1 = 12
AN2 = 13
DIG1 = 26
DIG2 = 24

sleep(1)


GPIO.setup(AN1, GPIO.OUT)
GPIO.setup(AN2, GPIO.OUT)
GPIO.setup(DIG1, GPIO.OUT)
GPIO.setup(DIG2, GPIO.OUT)

p1 = GPIO.PWM(AN1, 100)

GPIO.output(DIG1, GPIO.HIGH)

print ("Start")
p1.start(100)
sleep(2)

print ("Backwards")

GPIO.output(DIG1, GPIO.LOW)
p1.start(100)
sleep(2)

print ("Stop")
GPIO.output(DIG1, GPIO.LOW)
p1.start(0)
