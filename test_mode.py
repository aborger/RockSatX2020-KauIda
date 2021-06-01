import RPi.GPIO as GPIO
import config.pins as pins
from time import sleep
import threading
from config.timing import Timing
import os

def is_test(log):
    GPIO.setmode(GPIO.BCM)
    pins.setup()

    log.log('Checking test mode')
    GPIO.setup(pins.TEST_MODE_PWR, GPIO.OUT)
    GPIO.setup(pins.PRE_LAUNCH_PWR, GPIO.OUT)

    GPIO.output(pins.TEST_MODE_PWR, 1)
    GPIO.output(pins.PRE_LAUNCH_PWR, 1)

    GPIO.setup(pins.TEST_MODE_DETECT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(pins.PRE_LAUNCH_DETECT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    if GPIO.input(pins.PRE_LAUNCH_DETECT) == 1 and GPIO.input(pins.TEST_MODE_DETECT) == 1:
        print('enable wifi')
        log.log('Enabling wifi')
        os.system('sudo systemctl enable wpa_supplicant')
        while True:
            sleep(10)
    elif GPIO.input(pins.TEST_MODE_DETECT) == 1:
        log.log("RF test mode activated")
        from devices.rf_experiment.rf import RF

        rf = RF(log)

        # setup threads
        rf_setup = threading.Thread(target=rf.setup)
        rf_deactivate = threading.Thread(target=rf.deactivate)
        rf_activate = threading.Thread(target=rf.activate)
        rf_usb = threading.Thread(target=rf.power_usb)
        rf_pitooth = threading.Thread(target=rf.start_pitooth)

        rf_usb.start()
        rf_pitooth.start()

        rf_usb.join()
        rf_pitooth.join()

        sleep(Timing.RF_CONNECT_DELAY)

        rf_setup.start()
        rf_setup.join()

        rf_activate.start()


        while GPIO.input(pins.TEST_MODE_DETECT) == 1:
            sleep(1) # Doesnt continue with mission_control script
        os.system('sudo /usr/local/sbin/kill-rf.sh')
        sleep(5)
        os.system('sudo shutdown -h now')

    elif GPIO.input(pins.PRE_LAUNCH_DETECT) == 1:
        print('Pre-launch mode activated')
        log.log("Pre-Launch mode activate")
        from devices.lock import Lock

        # if limit switch is pressed pre-launch will begin
        lock = Lock()
        lock.deactivate()

        os.system('sudo /usr/local/sbin/start-rf.sh')
        sleep(10)
        os.system('sudo /usr/local/sbin/kill-rf.sh')
        sleep(10)
        os.system('sudo /usr/local/sbin/start-rf.sh')
        sleep(10)

        #os.system('sudo /usr/local/sbin/kill-rf.sh')
        os.system("sudo ptpcam -D")

        # arm battery
        out = open('config/launch_armed.txt', "w")
        out.write('1')
        out.close()



        os.system('sudo /usr/local/sbin/kill-rf.sh')

        sleep(2)

        lock.activate()
        sleep(1)
        os.system('sudo shutdown -h now')
    else:
        print('Test mode not activated')
        log.log("Test mode not activate")
