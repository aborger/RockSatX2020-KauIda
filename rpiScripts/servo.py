import RPi.GPIO as GPIO
import time

WAIT = 1

ZERO = 2.5
NINETY = 7.5
HALF_TURN = 12.5
servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(ZERO)
try:
	while True:
		p.ChangeDutyCycle(NINETY)
		print('90')
		time.sleep(WAIT)
		p.ChangeDutyCycle(HALF_TURN)
		print('180')
		time.sleep(WAIT)
		p.ChangeDutyCycle(NINETY)
		print('90')
		time.sleep(WAIT)
		p.ChangeDutyCycle(ZERO)
		time.sleep(WAIT)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

