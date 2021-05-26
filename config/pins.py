import RPi.GPIO as GPIO


LIMIT_POWER_PIN = 22
LIMIT_DETECT_PIN = 27

BOOM_PWM_PIN = 12
BOOM_DIR_PIN = 26

TE_INPUT_PIN = 16
TE_LATCH_PIN = 19

SERVO_PIN = 14

TEST_MODE_PWR = 24
TEST_MODE_DETECT = 25


def setup():

    GPIO.setmode(GPIO.BCM)

    #GPIO.setup(LIMIT_POWER_PIN, GPIO.OUT)
    #GPIO.output(LIMIT_POWER_PIN, 1)
    #GPIO.setup(LIMIT_DETECT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    GPIO.setup(BOOM_PWM_PIN, GPIO.OUT)
    GPIO.setup(BOOM_DIR_PIN, GPIO.OUT)

    GPIO.setup(TE_INPUT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(TE_LATCH_PIN, GPIO.OUT)

    GPIO.setup(SERVO_PIN, GPIO.OUT)
