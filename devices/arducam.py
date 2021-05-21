"""

* The ArduCam class controls the ArduCam

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""
from devices.device import Device
from timing import Timing
import os

OUTPUT_FILE = '/home/pi/output/ArduCam_recording.h264'

class ArduCam(Device):

    def activate(self):
        os.system("raspivid -t " + Timing.RECORD_TIME + " -o " + OUTPUT_FILE)

    def deactivate(self):
        return

