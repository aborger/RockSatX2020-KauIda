"""
* This is the main script

"""
import RPi.GPIO as GPIO
import threading
import time
import os

os.chdir('/home/pi/RockSatX2020-KauIda/')

from config.timing import Timing
from config.out_files import Files
import util

from detectors.TE_detector import TE_detect
from detectors.limit import Limit

from devices.boom import Boom
from devices.lock import Lock
from devices.ricoh import Ricoh
from devices.rf_experiment.rf import RF
from devices.arducam import ArduCam

import config.pins as pins

util.start_log()
util.log('Initializing...')
Files.iterate()

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
rf_activate = threading.Thread(target=rf.activate)
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
util.log('usb and pitooth on')

ricoh_activate.start()
time.sleep(8)

rf_setup.start()


rf_setup.join()
ricoh_activate.join()
lock.deactivate()

# Extend boom and take rf measurements
util.log('Extending boom...')

rf_activate.start()

boom.activate()

time.sleep(Timing.EXTEND_TIME)


util.log('Holding boom at extension...')
boom.shutdown()


time.sleep(Timing.TIME_AT_EXTENSION)


# Retract and take measurements
util.log('Retracting boom...')

boom.deactivate()

while not limit.doorShut():
    time.sleep(.1)

util.log('Door shut detected...')
util.log('Overdriving...')

time.sleep(Timing.BOOM_OVER_DRIVE)
boom.shutdown()

#=============== Cleanup ==================
#time.sleep(5)
lock.activate()
ricoh.deactivate()
rf_deactivate.start()

GPIO.cleanup()		# Resets all output pins to input to avoid issues
os.system('sudo /usr/local/sbin/kill-rf.sh')

util.log('Success')

