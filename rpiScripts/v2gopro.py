from time import sleep
import RPi.GPIO as GPIO
import numpy as np

GPIO.setmode(GPIO.BCM)

POWER = 21
GP_ENABLE = 13

GPIO.setup(POWER, GPIO.OUT)
GPIO.setup(GP_ENABLE, GPIO.OUT)

#GPIO.output(GP_ENABLE, 0)

for i in np.arange(0, 5, 1):
	print('on')
	GPIO.output(POWER, 1)
	sleep(i)
	print('Off')
	GPIO.output(POWER, 0)
	sleep(i)


GPIO.cleanup()
