# Master Control of RPi
import threading
from RPiMaster.detect import *
from RPiMaster.device import *
from time import sleep


te1 = detect('TE1', 5, 19) #16, 19
door = detect('Door Shut', 5)

Gopro = gopro('Gopro')
rf = rf('rf')
battery = battery('battery')
ricoh = ricoh('ricoh')
boom = Boom(5)
door_lock = lock('Door Lock')

Battery = threading.Thread(target=battery.activate)
Ricoh = threading.Thread(target=ricoh.activate)
Rf = threading.Thread(target=ricoh.activate)

Battery.daemon = True
Ricoh.daemon = True
Rf.daemon = True

Gopro.activate()
# Continues after TE1 is detected
te1.wait_for_detect()
Battery.start()
Ricoh.start()
Rf.start()
sleep(1) # 5
boom.activate()
sleep(5) # 154
boom.retract()
door.wait_for_detect()
door_lock.activate()
boom.deactivate()
ricoh.deactivate()
rf.deactivate()

