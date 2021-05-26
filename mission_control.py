"""
* This is the main script

"""
import RPi.GPIO as GPIO
import threading
import time
import os

os.chdir('/home/pi/RockSatX2020-KauIda/')

from config.timing import Timing
import util

from detectors.TE_detector import TE_detect
from detectors.limit import Limit

from devices.boom import Boom
from devices.lock import Lock
from devices.ricoh import Ricoh
from devices.rf_experiment.rf import RF
from devices.arducam import ArduCam

import config.pins as pins


NUM_EXT = Timing.EXTEND_TIME / Timing.EXTEND_PERIOD	# The number of RF datapoints taken

util.start_log()
util.log('Initializing...')

pins.setup()

# Initializing detects
te1 = TE_detect()
limit = Limit()

# Initializing devices
boom = Boom()
lock = Lock()
ricoh = Ricoh()
rf = RF()
arduCam = ArduCam()

# Setting up threads
rf_setup = threading.Thread(target=rf.setup)
rf_deactivate = threading.Thread(target=rf.deactivate)
rf_usb = threading.Thread(target=rf.power_usb)
rf_pitooth = threading.Thread(target=rf.start_pitooth)
ardu_activate = threading.Thread(target=arduCam.activate)
ricoh_activate = threading.Thread(target=ricoh.activate)


util.log('Setup Complete')

ardu_activate.start()


util.log('Waiting for TE...')

te1.wait_for_detect()
# =============== Main ===============
rf_usb.start()
rf_pitooth.start()

rf_usb.join()
rf_pitooth.join()
print('usb and pitooth on')

rf_setup.start()
ricoh_activate.start()

rf_setup.join()
ricoh_activate.join()
lock.deactivate()

# Extend boom and take rf measurements
extension = 0
util.log('Extending boom...')

while extension < NUM_EXT:
    rf_activate = threading.Thread(target=rf.activate)
    rf_activate.daemon = True
    rf_activate.start()

    boom.activate()
    extension += 1


util.log('Holding boom at extension...')

time.sleep(Timing.TIME_AT_EXTENSION)


# Retract and take measurements
util.log('Retracting boom...')

while not limit.doorShut():
    rf_activate = threading.Thread(target=rf.activate)
    rf_activate.daemon = True
    rf_activate.start()
    boom.deactivate()

util.log('Door shut detected...')
extension = 5
while extension > 0:
    boom.deactivate()
    extension -= 1
#=============== Cleanup ==================
#time.sleep(5)
lock.activate()
boom.shutdown()
ricoh.deactivate()
rf_deactivate.start()

GPIO.cleanup()		# Resets all output pins to input to avoid issues
os.system('sudo /usr/local/sbin/kill-rf.sh')

util.log('Success')

