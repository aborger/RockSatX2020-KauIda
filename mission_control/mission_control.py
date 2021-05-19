"""
* This is the main script

"""
import RPi.GPIO as GPIO
import threading
import time

from timing import Timing

from detectors.TE_detector import TE_detect
from detectors.limit import Limit

from devices.boom import Boom
from devices.lock import Lock
from devices.ricoh import Ricoh
from devices.rf_experiment.rf import RF
from devices.arducam import ArduCam

NUM_EXT = Timing.EXTEND_TIME / Timing.EXTEND_PERIOD	# The number of RF datapoints taken

print('Initializing...')

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

# Setting up rf
rf_setup.start()
rf_setup.join()

print('Setup Complete')
print('Waiting for TE...')

# =============== Main ===============
ricoh.activate()

# Extend boom and take rf measurements
extension = 0
print('Extending boom...')

while extension < NUM_EXT:
    rf_activate = threading.Thread(target=rf.activate)
    rf_activate.daemon = True
    rf_activate.start()

    boom.activate()
    extension += 1


print('Holding boom at extension...')

time.sleep(Timing.TIME_AT_EXTENSION)


# Retract and take measurements
print('Retracting boom...')

while not limit.doorShut():
    rf_activate = threading.Thread(target=rf.activate)
    rf.daemon = True
    rf.start()
    boom.deactivate(Timing.TIME_AT_EXTENSION)
    extension -= 1


#=============== Cleanup ==================
lock.activate()
boom.shutdown()
ricoh.deactivate()
rf_deactivate.start()




GPIO.cleanup()		# Resets all output pins to input to avoid issues

print('Success')

