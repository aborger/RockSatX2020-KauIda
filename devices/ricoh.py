"""
* The Ricoh class communicates with the ricoh camera when to start and stop recording

* Authors: Aaron Borger <aborger@nnu.edu (307)534-6265>

           KuaIda KCC team <purvinis@hawaii.edu>

"""

from devices.device import Device
import os
from time import sleep
from config.out_files import Files
import subprocess
from config.timing import Timing

class Ricoh(Device):

    def __init__(self, log):
        self.log = log

    def setup(self):
        subprocess.call('sudo ptpcam --set-property=0x5003 --val="3840x1920"', shell=True)
        #subprocess.call('sudo ptpcam --set-property=0x5003 --val="1920x960"', shell=True)



    def go(self):
        # Recording 1
        self._activate()
        sleep(Timing.EXTEND_TIME/2)
        self._deactivate()
        # Recording 2
        self._activate()
        sleep(Timing.EXTEND_TIME/2 - Timing.RICOH_PAUSE)
        self._deactivate()
        # Recording 3
        self._activate()
        sleep(Timing.TIME_AT_EXTENSION/2 + 1)
        self._deactivate()
        # Recording 4
        self._activate()
        sleep(Timing.TIME_AT_EXTENSION/2 - 1)
        self._deactivate()
        # Recording 5
        self._activate()
        sleep(Timing.EXTEND_TIME/2)
        self._deactivate()

        sleep(5)

        mission_num = Files.get_mission_num()
        os.chdir('../output/ricoh')
        os.mkdir('mission' + mission_num)
        os.chdir('mission' + mission_num)
        self._download_all()
        self.log.log('Ricoh download complete!')

    def activate(self):
        #self._wake_up()
        #time.sleep(10)
        try:
            subprocess.call("sudo ptpcam -R 0x101c,0,0,1", shell=True)		# Starts recording
        except:
            self.log.log("rpi didnt turn on until TE")
            time.sleep(1)
            subprocess.call("sudo ptpcam -R 0x101c,0,0,1", shell=True)
        #self._turn_on()

    def delete(self):
        subprocess.call("sudo ptpcam -D", shell=True)

    def deactivate(self):
        subprocess.call("sudo ptpcam -R 0x1018,0xFFFFFFFF", shell=True)

    def _deactivate(self):
        try:
            subprocess.call("sudo ptpcam -R 0x1018,0xFFFFFFFF", shell=True)	# Stops recording
        except Exception as e:
            self.log.log('Ricoh did not deactivate:')
            self.log.log(e)
        #time.sleep(4)

        # Get ricoh videos
        #os.system("sudo adb pull /sdcard/DCIM/100RICOH/ " + OUTPUT_FILE)	# Downloads video
        """
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
        """

        self.log.log("Ricoh recording complete")
        #time.sleep(1)
        #self._sleep()

    def download(self):
        mission_num = Files.get_mission_num()
        os.chdir('../output/ricoh')
        os.mkdir('mission' + mission_num)
        os.chdir('mission' + mission_num)
        self.log.log('Downloading Ricoh videos...')
        try:
            subprocess.call('sudo ptpcam --get-all-files', shell=True, timeout=Timing.DOWNLOAD_TIMEOUT)
        except subprocess.TimeoutExpired as e:
            self.log.log(e)
            self.log.log('Retrying ricoh video!')
            subprocess.call('sudo ptpcam --get-all-files', shell=True)
            sleep(5)
            try:
                subprocess.call('sudo ptpcam --get-all-files', shell=True, timeout=Timing.DOWNLOAD_TIMEOUT)
            except subprocess.TimeoutExpired as e:
                self.log.log(e)
                self.log.log('Retrying ricoh video!')
                subprocess.call('sudo ptpcam --get-all-files', shell=True)
                sleep(5)
                subprocess.call('sudo ptpcam --get-all-files', shell=True)
        self.log.log('Ricoh videos downloaded!')

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
