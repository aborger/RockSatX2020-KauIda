"""

* The Lock class controls multiple servos to latch the door shut before the rocket spins up.

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""

from device import Device


class Lock(Device):

    def setup(self, servo_pin):
        GPIO.setup(pin, GPIO.OUT)
        self.servo = GPIO.PWM(servo_pin, 50)	# Sets servo to use PWM on servo_pin at 50 Hz
        self.servo.start(2.5)
        self.servo.ChangeDutyCycle(2.5)		# Sets servo to starting position

    def activate(self):
        self.servo.ChangeDutyCycle(12.5)	# Rotates servo to 90 degrees position

    def deactivate(self):
        self.servo.ChangeDutyCycle(2.5)		# Sets servo to starting position
