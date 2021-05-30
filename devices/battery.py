import RPi.GPIO as GPIO

LATCH_PIN = 19


class Battery:
    def activate(self):
        out = open('config/battery_armed.txt', "r")
        armed = out.read()
        if armed == 1:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(LATCH_PIN, GPIO.OUT)
            GPIO.output(LATCH_PIN, GPIO.LOW)
        else:
            print('Battery is not armed!')
