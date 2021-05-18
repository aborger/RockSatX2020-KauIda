"""

* The TE_detect class unlatches a backup battery and allows the mission_control program to continue

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

INPUT_PIN = 16
LATCH_PIN = 19

class TE_detect:

    def setup(self):
        GPIO.setup(INPUT_PIIN, GPIO.IN, pull_up_down = GPIO.PUD_DWON)
        GPIO.setup(LATCH_PIN, GPIO.OUT)

    def wait_for_detect(self):
        print('Waiting to detect TE...')
        GPIO.wait_for_edge(INPUT_PIN, GPIO.RISING)	# Pauses until detection is detected

        print('TE has been detected')
        GPIO.output(LATCH_PIN, GPIO.LOW)		# Unlatches battery
