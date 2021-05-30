import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SERVO_PIN = 14

ZERO = 2.5
NINETY = 7.5
ONE_EIGHTY = 12.5

GPIO.setup(SERVO_PIN, GPIO.OUT)


servo = GPIO.PWM(SERVO_PIN, 50)       # Sets servo to use PWM on servo_pin at 50 Hz
servo.start(ZERO)
sleep(1)
servo.ChangeDutyCycle(ONE_EIGHTY)          # Rotates servo to 90 degrees position
sleep(1)
servo.ChangeDutyCycle(ZERO)                # Sets servo to starting position
sleep(1)
GPIO.cleanup()
