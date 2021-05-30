import RPi.GPIO as GPIO
import config.pins as pins
from time import sleep


def is_test():
    GPIO.setup(pins.TEST_MODE_PWR)
    GPIO.output(pins.TEST_MODE_PWR, 1)

    GPIO.setup(pins.TEST_MODE_DETECT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN

    if GPIO.input(pins.TEST_MODE_DETECT) == 1:
        from devices.boom import Boom
        from devices.rf_experiment.rf import RF

        rf = RF()
        boom = Boom()

        # setup threads
        rf_setup = threading.Thread(target=rf.setup)
        rf_deactivate = threading.Thread(target=rf.deactivate)
        rf_activate = threading.Thread(target=rf.activate)
        rf_usb = threading.Thread(target=rf.power_usb)
        rf_pitooth = threading.Thread(target=rf.start_pitooth)
        pre_launch = threading.thread(target=pre_launch_setup)

        rf_usb.start()
        rf_pitooth.start()

        rf_usb.join()
        rf_pitooth.join()

        rf_setup.start()
        rf_setup.join()

        rf_activate.start()
        boom.activate()
        sleep(10)
        pre_launch.start()

        while True:
            sleep(1) # Doesnt continue with mission_control script


def pre_launch_setup():
    while not limit.doorShut():
        sleep(.1)

    # if limit switch is pressed pre-launch will begin
    os.system('sudo /usr/local/sbin/kill-rf.sh')
    os.system("sudo ptpcam -D")

    # arm battery
    out = open('config/battery_armed.txt', "w")
    out.write('1')
    out.close()


