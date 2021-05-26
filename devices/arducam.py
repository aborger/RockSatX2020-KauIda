"""

* The ArduCam class controls the ArduCam

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""
from devices.device import Device
from config.timing import Timing
import os
from util import log

OUTPUT_FILE = '/home/pi/output/arducam/ArduCam_recording'
LOG_FILE = '/home/pi/RockSatX2020-KauIda/config/arduLog.txt'

class ArduCam(Device):

    def activate(self):
        log('Arducam recording')
        arduLog = None
        try:
            arduLog = open(LOG_FILE, "r")
        except FileNotFoundError:
            arduLog = open(LOG_FILE, "w")
            arduLog.write('0')
            arduLog.close()
            arduLog = open(LOG_FILE, "r")
        except Exception as e:
            raise e

        mission_num = arduLog.read()
        arduLog.close()
        arduLog = open(LOG_FILE, "w")
        next_mission = int(mission_num) + 1
        arduLog.write(str(next_mission))
        arduLog.close()
        os.system("raspivid -t " + str(Timing.RECORD_TIME) + " -o " + OUTPUT_FILE + mission_num + '.h264')

    def deactivate(self):
        return

