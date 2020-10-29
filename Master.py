# Master Control of RPi
# Sets up each event in a thread
import threading
from RPiMaster.detect import Detect
import RPiMaster.device as device
from time import sleep
import sys

gse = Detect('GSE', 1, 18) #15, 18
te1 = Detect('TE1', 5, 19) #16, 19
door = Detect('Door Shut', 15, 20)

Gopro = device.gopro('Gopro')
rf = device.rf('rf')
battery = device.battery('battery')
ricoh = device.ricoh('ricoh')
boom = device.Boom(3)
door_lock = device.lock('Door Lock')


def setup():
	rf.setup()
	Gopro.setup()

	
def GSE():
	gse.wait_for_detect()
	# Continues after GSE is detected
	Gopro.activate()


def TE1():

	# Continues after TE1 is detected
	te1.wait_for_detect()
	battery.activate()
	ricoh.activate() # Turn on
	rf.activate()
	sleep(1) # 5
	boom.activate()
	sleep(5) # 154
	boom.deactivate()
	sleep(4) # 40
	ricoh.deactivate()
	rf.deactivate()

		
def Door_Lock():
	door.wait_for_detect()
	door_lock.activate()

	
	
if __name__ == "__main__":
	try:
		Setup = threading.Thread(target=setup)
		GSE_detect = threading.Thread(target=GSE)
		TE1_detect = threading.Thread(target=TE1)
		Door_lock = threading.Thread(target=Door_Lock)
		
		Setup.daemon = True
		GSE_detect.daemon = True
		TE1_detect.daemon = True
		Door_Lock.daemon = True


		Setup.start()
		GSE_detect.start()
		TE1_detect.start()
		Door_lock.start()

		'''
		Setup.join()
		GSE_detect.join()
		TE1_detect.join()
		Door_lock.join()
		'''
		while True: sleep(100)
	except (KeyboardInterrupt, SystemExit):
		print('STOPPPPP')
	


	
	print('Mission Complete')
