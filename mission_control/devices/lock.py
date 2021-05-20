"""

* The Lock class controls multiple servos to latch the door shut before the rocket spins up.

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""

from devices.device import Device
import RPi.GPIO as GPIO

SERVO_PIN = 14
ZERO = 2.5
NINETY = 7.5
ONE_EIGHTY = 12.5


class Lock(Device):

    def __init__(self):
        #GPIO.setup(SERVO_PIN, GPIO.OUT)
        self.servo = GPIO.PWM(SERVO_PIN, 50)	# Sets servo to use PWM on servo_pin at 50 Hz
        self.servo.start(ZERO)
        self.servo.ChangeDutyCycle(ZERO)	# Sets servo to starting position

    def activate(self):
        self.servo.ChangeDutyCycle(NINETY)	# Rotates servo to 90 degrees position

    def deactivate(self):
        self.servo.ChangeDutyCycle(ZERO)	# Sets servo to starting position

    def shutdown(self):
        return
