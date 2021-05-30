
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)



LIMIT_POWER_PIN = 27
LIMIT_DETECT_PIN = 21


GPIO.setup(LIMIT_POWER_PIN, GPIO.OUT)
GPIO.output(LIMIT_POWER_PIN, 1)


GPIO.setup(LIMIT_DETECT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
	while True:
		print(GPIO.input(LIMIT_DETECT_PIN))


except KeyboardInterrupt:
	GPIO.cleanup()


GPIO.cleanup()