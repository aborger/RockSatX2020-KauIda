# Master Control of RPi
# Sets up each event in a thread
import threading
from RPiMaster.detect import Detect
import RPiMaster.device

gse = Detect(15, 18)
te1 = Detect(16, 19)

gopro = device.Gopro()
rf = device.Rf()
imu = device.IMU()
battery = device.Battery()
ricoh = device.Ricoh()
boom = device.Boom()


def setup()
	rf.setup()
	gopro.setup()
	
def GSE():
	gse.wait_for_detect()
	# Continues after GSE is detected
	Gopro.activate()
	imu.activate()

def TE1():
	# Continues after TE1 is detected
	te1.wait_for_detect()
	battery.activate()
	ricoh.activate()
	rf.activate()
	wait(5)
	boom.activate()
	wait(154)
	boom.deactivate()
	wait(40)
	ricoh.deactivate()
	transfer_video()
	rf.deactivate()
	
if __name__ == "__main__":
	GSE_detect = threading.Thread(target=GSE)
	TE1_detect = threading.Thread(target=TE1)
	
	GSE_detect.start()
	TE1_detect.start()
	
	GSE_detect.join()
	TE1_detect.join()
	
	print('Mission Complete')
