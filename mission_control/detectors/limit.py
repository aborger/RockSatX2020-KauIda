
"""

* The Limit class detects when a limit switch is pressed.

* Power is sent through one wire and when the connection is completed, doorShut() returns true.

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>
"""

import RPi.GPIO as GPIO

POWER_PIN = 22
DETECT_PIN = 27

class Limit:

    def setup(self):
        GPIO.setup(POWER_PIN, GPIO.OUT)
        GPIO.output(POWER_PIN, 1)
        GPIO.(DETECT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def doorShut(self):
        return not GPIO.input(DETECT_PIN)
