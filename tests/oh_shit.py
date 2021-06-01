
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PRE_LAUNCH_PWR = 10
PRE_LAUNCH_DETECT = 9

LIMIT_POWER_PIN =  15 # Red works and gets power (pin 22)
LIMIT_DETECT_PIN =  22


GPIO.setup(LIMIT_POWER_PIN, GPIO.OUT)
GPIO.output(LIMIT_POWER_PIN, 0)


#GPIO.setup(LIMIT_DETECT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
	while True:
		#print(GPIO.input(LIMIT_DETECT_PIN))
                print(1)

except KeyboardInterrupt:
	GPIO.cleanup()


GPIO.cleanup()
