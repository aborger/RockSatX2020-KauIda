"""

* The TE_detect class unlatches a backup battery and allows the mission_control program to continue

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""

import RPi.GPIO as GPIO
import config.pins as pins



class TE_detect:

    def wait_for_detect(self):
        GPIO.wait_for_edge(pins.TE_INPUT_PIN, GPIO.RISING)	# Pauses until detection is detected

        GPIO.output(pins.TE_LATCH_PIN, GPIO.LOW)		# Unlatches battery
