
"""

* The Limit class detects when a limit switch is pressed.

* Power is sent through one wire and when the connection is completed, doorShut() returns true.

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>
"""

import RPi.GPIO as GPIO
import config.pins as pins


class Limit:

    def doorShut(self):
        if GPIO.input(pins.LIMIT_DETECT_PIN) == 1:
            print("Door is not shut")
            return False
        else:
            print("Door shut detected!")
            return True
