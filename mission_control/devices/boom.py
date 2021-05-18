"""

* The Boom class controls a motor through a Cytron HAT-MDD10 Motor Controller

* The boom extends and descends in steps to allow the rf experiment to log signal strength at known distances

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""
from device import Device

PWM_PIN = 12
DIR_PIN = 26

class Boom(Device):

    def __init__(self):
        self.power = None
        self.motor = None

    def setup(self, power):
        self.power = power

        GPIO.setup(PWM_PIN, GPIO.OUT)
        GPIO.setup(DIR_PIN, GPIO.OUT)
        sleep(1)
        self.motor = GPIO.PWM(PWM_PIN, 100) 	# Sets motor to use PWM_PIN at 100 Hz

    # Extends the boom
    def activate(self, step_time):
        GPIO.output(DIR_PIN, GPIO.HIGH)
        self.motor.start(self.power)		# Activates motor in forward direction
        sleep(step_time)
        self.motor.start(0)			# Pauses motor for an un-noticable amount of time

    # Descends the boom
    def deactivate(self, step_time)
        GPIO.output(self.DIR_PIN, GPIO.LOW)	# Reverses motor
        self.motor.start(self.power)		# Activates motor which now goes in reverse
        sleep(step_time)
        self.motor.start(0)			# Stops motor because power is 0

    def shutdown(self):
        self.motor.start(0)			# Stops motor because power is 0

