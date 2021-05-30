import RPi.GPIO as GPIO
import config.pins as pins
from time import sleep


def is_test():
    GPIO.setup(pins.TEST_MODE_PWR)
    GPIO.setup(pins.PRE_LAUNCH_PWR)

    GPIO.output(pins.TEST_MODE_PWR, 1)
    GPIO.output(pins.PRE_LAUNCH_PWR, 1)

    GPIO.setup(pins.TEST_MODE_DETECT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(pins.PRE_LAUNCH_DETECT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    if GPIO.input(pins.TEST_MODE_DETECT) == 1:
        from devices.rf_experiment.rf import RF

        rf = RF()

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

        sleep(RF_CONNECT_DELAY)

        rf_setup.start()
        rf_setup.join()

        rf_activate.start()


        while True:
            sleep(1) # Doesnt continue with mission_control script
    elif GPIO.input(pins.PRE_LAUNCH_DETECT) == 1:

        # if limit switch is pressed pre-launch will begin
        os.system('sudo /usr/local/sbin/kill-rf.sh')
        os.system("sudo ptpcam -D")

        # arm battery
        out = open('config/launch_armed.txt', "w")
        out.write('1')
        out.close()


