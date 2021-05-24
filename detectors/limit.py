
"""

* The Limit class detects when a limit switch is pressed.

* Power is sent through one wire and when the connection is completed, doorShut() returns true.

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>
"""

import RPi.GPIO as GPIO
import config.pins as pins


class Limit:
    def doorShut(self):
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, 1)


        GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        #def doorShut(self):
        #print(GPIO.input(27))
        
        if GPIO.input(pins.LIMIT_DETECT_PIN) == 1:
            print("Door is not shut")
            return False
        else:
            print("Door shut detected!")
            return True
        
