import RPi.GPIO as GPIO
import config.pins as pins

TEST_MODE_PWR = 24
TEST_MODE_DETECT = 25

def is_test():
    GPIO.setup(pins.TEST_MODE_PWR)
    GPIO.output(pins.TEST_MODE_PWR, 1)

    GPIO.setup(pins.TEST_MODE_DETECT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN

    if GPIO.input(pins.TEST_MODE_DETECT) == 1:
        test_mode()


def test_mode():
    from devices.rf_experiment.rf import RF
    rf = RF()

    rf_setup = threading.Thread(target=rf.setup)
    rf_deactivate = threading.Thread(target=rf.deactivate)
    rf_activate = threading.Thread(target=rf.activate)

    os.system("sudo /usr/local/sbin/start-rf.sh")
    turn on rpi bluetooth

    rf_setup.start()
    rf_setup.join()

    rf_activate.start()

    os.system("ptpcam -D")
    os.system("rf-kill")
