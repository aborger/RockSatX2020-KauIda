# Master Control of RPi
import threading
from RPiMaster.detect import *
from RPiMaster.device import *
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

os.system("./bluetoothON.sh")


NUM_EXTENSIONS = 5
EXTENSION_PERIOD = 1

# Initializing detects
te1 = Detect('TE1', 16, 19, 'r') #16, 19
limit = Limit(22, 27)

# Initializing devices
gopro = gopro('gopro')
rf = Rf()
ricoh = Ricoh()
boom = Boom(5, 75)
lock = Lock(14)
readyLight = ReadyLight(11)

# Setup threads
Rf_setup = threading.Thread(target=rf.setup)


# deactivate threads
Rf_deactivate = threading.Thread(target=rf.deactivate)
Gopro_deactivate = threading.Thread(target=gopro.deactivate)


#-----------------------------------------------#
#			Setup			#
#-----------------------------------------------#
Rf_setup.start()


Rf_setup.join()

# Continues after TE1 is detected
readyLight.activate()
te1.wait_for_detect()
readyLight.deactivate()
#-----------------------------------------------#
#			Main			#
#-----------------------------------------------#
ricoh.activate()

# Extend boom and take rf measurements
extension = 0
print('Extending boom...')
while extension < NUM_EXTENSIONS:
	RF_activate = threading.Thread(target=rf.activate)
	RF_activate.daemon = True
	RF_activate.start()
	boom.activate(EXTENSION_PERIOD)
	extension += 1


# Hold at extension
print('Holding boom at extension...')
sleep(3)


readyLight.activate()
# Retract and take measurements
print('Retracting boom...')
while not limit.doorShut():
	RF = threading.Thread(target=rf.activate)
	RF.daemon = True
	RF.start()
	boom.deactivate(EXTENSION_PERIOD)
	extension -= 1


#------#
readyLight.deactivate()
lock.activate()
boom.shutdown()
ricoh.deactivate()
Gopro_deactivate.start()
Rf_deactivate.start()
lock.deactivate()
GPIO.cleanup()
