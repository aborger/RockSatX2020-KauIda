"""

* The Boom class controls a motor through a Cytron HAT-MDD10 Motor Controller

* The boom extends and descends in steps to allow the rf experiment to log signal strength at known distances

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""
from devices.device import Device
from timing import Timing
import RPi.GPIO as GPIO
import time
import config.pins as pins


class Boom(Device):

    def __init__(self):
        self.motor = GPIO.PWM(pins.BOOM_PWM_PIN, 100) 	# Sets motor to use PWM_PIN at 100 Hz

    def setup(self):
        return

    # Extends the boom
    def activate(self):
        GPIO.output(pins.BOOM_DIR_PIN, GPIO.HIGH)
        self.motor.start(Timing.BOOM_POWER)	# Activates motor in forward direction
        time.sleep(Timing.EXTEND_PERIOD)
        self.motor.start(0)			# Pauses motor for an un-noticable amount of time

    # Descends the boom
    def deactivate(self):
        GPIO.output(pins.BOOM_DIR_PIN, GPIO.LOW)	# Reverses motor
        self.motor.start(Timing.BOOM_POWER)	# Activates motor which now goes in reverse
        time.sleep(Timing.EXTEND_PERIOD)
        self.motor.start(0)			# Stops motor because power is 0

    def shutdown(self):
        self.motor.start(0)			# Stops motor because power is 0

