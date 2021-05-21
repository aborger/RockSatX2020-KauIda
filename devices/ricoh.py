"""
* The Ricoh class communicates with the ricoh camera when to start and stop recording

* Authors: Aaron Borger <aborger@nnu.edu (307)534-6265>

           KuaIda KCC team <purvinis@hawaii.edu>

"""

from devices.device import Device
import os
import time

OUTPUT_FILE = '/home/pi/output/ricoh'


class Ricoh(Device):

    def activate(self):
        os.system("ptpcam -R 0x101c,0,0,1")		# Starts recording

    def deactivate(self):
        os.system("ptpcam -R 0x1018,0xFFFFFFFF")	# Stops recording
        time.sleep(5)
        os.system("sudo adb pull /sdcard/DCIM/100RICOH/ " + OUTPUT_FILE)	# Downloads video
        print("Ricoh Video Transfer Complete")

    def shutdown(self):
        return
