"""
* The Ricoh class communicates with the ricoh camera when to start and stop recording

* Authors: Aaron Borger <aborger@nnu.edu (307)534-6265>

           KuaIda KCC team <purvinis@hawaii.edu>

"""

from devices.device import Device
import os
import time
from util import log
import subprocess

OUTPUT_FILE = '/home/pi/output/ricoh'


class Ricoh(Device):

    def activate(self):
        #self._wake_up()
        time.sleep(5)
        try:
            subprocess.call("sudo ptpcam -R 0x101c,0,0,1", shell=True)		# Starts recording
        except:
            log("rpi didnt turn on until TE")
            time.sleep(5)
            subprocess.call("sudo ptpcam -R 0x101c,0,0,1", shell=True)
        #self._turn_on()

    def deactivate(self):
        subprocess.call("sudo ptpcam -R 0x1018,0xFFFFFFFF", shell=True)	# Stops recording
        #time.sleep(5)

        # Get ricoh videos
        #os.system("sudo adb pull /sdcard/DCIM/100RICOH/ " + OUTPUT_FILE)	# Downloads video
        log("Transferring Ricoh footage...")
        files = []
        listFiles = subprocess.Popen(["sudo", "ptpcam", "-L"], stdout=subprocess.PIPE)

        for line in listFiles.stdout.readlines():
            files.append(line.rstrip())

        lastLine = files[len(files) - 2].decode().split(" ")
        lastVid = lastLine[0][:-1]
        ptpcmd = 'sudo ptpcam --get-file=' + lastVid

        os.chdir('../output/ricoh')
        subprocess.call(ptpcmd, shell=True)


        log("Ricoh Video Transfer Complete")
        #time.sleep(1)
        #self._sleep()

    def _turn_off(self):
        os.system("sudo ptpcam -R 0x1013")

    def _turn_on(self):
        os.system("sudo /usr/local/sbin/cycle-power.sh")

    def _wake_up(self):
        #os.system("adb shell input keyevent KEYCODE_POWER")
        os.system("adb shell input keyevent KEYCODE_WAKEUP")


    def _sleep(self):
        os.system("sudo ptpcam --set-property=0xd80e --val=0x01")
        #os.system("adb shell input keyevent KEYCODE_POWER")

    def shutdown(self):
        return
