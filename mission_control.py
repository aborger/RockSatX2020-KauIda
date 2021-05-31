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
from util import Log

from detectors.TE_detector import TE_detect
from detectors.limit import Limit

from devices.boom import Boom
from devices.lock import Lock
from devices.ricoh import Ricoh
from devices.rf_experiment.rf import RF
from devices.arducam import ArduCam
from devices.pre_launch import Pre_launch

import config.pins as pins

log = Log()
log.log('Initializing...')


Files.iterate()

pins.setup()

# Initializing detects
te1 = TE_detect()
limit = Limit()

# Initializing devices
boom = Boom()
lock = Lock()
ricoh = Ricoh(log)
rf = RF(log)
arduCam = ArduCam(log)

# Setting up threads
rf_go = threading.Thread(target=rf.go)
rf_deactivate = threading.Thread(target=rf.deactivate)
rf_usb = threading.Thread(target=rf.power_usb)
rf_pitooth = threading.Thread(target=rf.start_pitooth)
ardu_activate = threading.Thread(target=arduCam.activate)
ricoh_download = threading.Thread(target=ricoh.download)

log.log('Setup Complete')


log.log('Waiting for TE...')

te1.wait_for_detect()
log.set_epoch()
log.log('TE has been detected')
# =============== Main ===============
ardu_activate.start()
rf_usb.start()
rf_pitooth.start()

rf_usb.join()
rf_pitooth.join()
log.log('usb and pitooth on')

#ricoh_activate.start()

rf_go.start()

# Extend boom and take rf measurements
time.sleep(Timing.BOOM_DELAY)

log.log('Extending boom...')
# Video 1
ricoh.activate()
lock.deactivate()
boom.activate()
time.sleep(Timing.EXTEND_TIME/2)
boom.shutdown()
ricoh.deactivate()
log.log('First video complete')

# Video 2
ricoh.activate()
boom.activate()
time.sleep(Timing.EXTEND_TIME/2)

log.log('Holding boom at extension...')
boom.shutdown()
ricoh.deactivate()
log.log('Second video complete')

# Video 3
ricoh.activate()
time.sleep(Timing.TIME_AT_EXTENSION/2)
ricoh.deactivate()
log.log('Third video complete')

# Video 4
ricoh.activate()
time.sleep(Timing.TIME_AT_EXTENSION/2)
ricoh.deactivate()
log.log('Fourth video complete')

# Retract and take measurements
log.log('Retracting boom...')

# Video 5
ricoh.activate()
boom.deactivate()
time.sleep(Timing.EXTEND_TIME/2)
boom.shutdown()
ricoh.deactivate()
log.log('Fifth video complete')

# Video 6
ricoh.activate()
boom.deactivate()


while not limit.doorShut():
    time.sleep(.1)

log.log('Door shut detected...')
log.log('Overdriving...')

ricoh.deactivate()
log.log('Sixth and final video complete')
ricoh_download.start()

time.sleep(Timing.BOOM_OVER_DRIVE)
boom.shutdown()


#=============== Cleanup ==================
lock.activate()

rf_go.join()
rf_deactivate.start()

ricoh_download.join()
rf_deactivate.join()
GPIO.cleanup()		# Resets all output pins to input to avoid issues

if os.getcwd() != '/home/pi/RockSatX2020-KauIda':
    os.chdir('../../../RockSatX2020-KauIda/')
print('os.getcwd()')

if Pre_launch.is_active():
    ricoh.activate()
else:
    ricoh.delete()
    os.system('sudo /usr/local/sbin/kill-rf.sh')


log.log('Success')

