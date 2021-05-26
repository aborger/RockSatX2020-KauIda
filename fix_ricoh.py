import os
import subprocess
from time import sleep

"""
while not ricoh_working():
  sleep()
  os.system("sudo reboot")
  troubleshoot()
"""

def try_lsusb():
  proc = subprocess.Popen(["lsusb"], stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  out = out.decode('utf-8')
  out = out.split('\n')[0]
  print(out)
  out = out.split(' ')[6]
  if out == 'Ricoh':
    print('lsusb: success')
  else:
    print('lsusb: reboot')
    #os.system('sudo reboot')
def try_adb():
  proc = subprocess.Popen(["adb shell ls"], stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  err = err.decode('utf-8')
  if err == 'error: no devices/emulators found\n':
    print('adb: cannot find ricoh, reboot')
    #os.system('sudo reboot')
  else:
    print('adb: success:', err)

def try_ptp():
  proc = subprocess.Popen(["sudo ptpcam -l"], stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  err = err.decode('utf-8')
  out = out.decode('utf-8')
  if err == '':
    print('PTP: retrying...')
    try_ptp()

  err = err.split('\n')
  if err[0] == "ERROR: Could not open session!":
    print('PTP: cant open session')
    os.system('sudo ptpcam --reset')
    os.system('sudo ldconfig')
    print('PTP: Trying again')
    try_ptp()
  else:
    print('PTP: success')
    print('Output: ', out)
    print('Error: ', err)






  """
  if ADB == 'no permission':
    kill-server
    sudo start-server
    replug()
  if PTPcam == 'could not open session':
    ptpcam --reset
    sudo ldconfig
  """
def ricoh_working():
  ricoh.activate()
  ricoh.deactivate()
  check_for_file()

try_lsusb()
try_adb()
try_ptp()
