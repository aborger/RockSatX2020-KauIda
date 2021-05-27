"""

* The ArduCam class controls the ArduCam

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""
from devices.device import Device
from config.timing import Timing
from config.out_files import Files
import os
from util import log


class ArduCam(Device):

    def activate(self):
        log('Arducam recording')

        mission_num = Files.get_mission_num()

        os.system("raspivid -t " + str(Timing.RECORD_TIME) + " -o " + Files.OUT_DIR + 'arducam/mission' + mission_num + '.h264')

    def deactivate(self):
        return

