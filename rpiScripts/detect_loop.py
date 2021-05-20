import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

TE_PIN = 16

LIMIT_POWER_PIN = 27
LIMIT_DETECT_PIN = 22


GPIO.setup(LIMIT_POWER_PIN, GPIO.OUT)
GPIO.output(LIMIT_POWER_PIN, 1)


GPIO.setup(LIMIT_DETECT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
	while True:
		GPIO.wait_for_edge(LIMIT_DETECT_PIN, GPIO.RISING)
		print('yes')

except KeyboardInterrupt:
	GPIO.cleanup()


GPIO.cleanup()

