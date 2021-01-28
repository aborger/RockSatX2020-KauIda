# Master Control of RPi
import threading
from RPiMaster.detect import *
from RPiMaster.device import *
from time import sleep

NUM_EXTENSIONS = 5
EXTENSION_PERIOD = 1

# Initializing detects
te1 = Detect('TE1', 16, 19) #16, 19
door = Detect('Door Shut', 27, -1)

# Initializing devices
gopro = Gopro('Gopro')
rf = Rf('rf')
battery = battery('battery')
ricoh = ricoh('ricoh')
boom = Boom(5)
door_lock = Lock()

# Setup threads
Rf_setup = threading.Thread(target=rf.setup)
Gopro_setup = threading.Thread(target=gopro.activate)

# Main threads
Battery = threading.Thread(target=battery.activate)
Ricoh = threading.Thread(target=ricoh.activate)

# deactivate threads
Rf_deactivate = threading.Thread(target=rf.deactivate)
Gopro_deactivate = threading.Thread(target=gopro.deactivate)

# daemons
Battery.daemon = True
Ricoh.daemon = True

#-----------------------------------------------#
#			Setup			#
#-----------------------------------------------#
Rf_setup.start()
Gopro_setup.start()

Rf_setup.join()
Gopro_setup.join()

# Continues after TE1 is detected
te1.wait_for_detect()
#-----------------------------------------------#
#			Main			#
#-----------------------------------------------#
Battery.start()
Ricoh.start()

# Extend boom and take rf measurements
extension = 0
print('Extending boom...')
while extension < NUM_EXTENSIONS:
	RF = threading.Thread(target=rf.activate)
	RF.daemon = True
	RF.start()
	boom.activate(EXTENSION_PERIOD)
	extension += 1

# Retract and take measurements
print('Holding at extension...')
sleep(2)
print('Retracting boom...')
while extension > 0:
	RF = threading.Thread(target=rf.activate)
	RF.daemon = True
	RF.start()
	boom.deactivate(EXTENSION_PERIOD)
	extension -= 1

# Continues after door shuts
door.wait_for_detect()
door_lock.activate()
#-------------------------------------------------------#
#			Deactivate			#
#-------------------------------------------------------#
boom.shutdown()
ricoh.deactivate()
Gopro_deactivate.start()
Rf_deactivate.start()