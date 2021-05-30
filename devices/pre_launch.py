import RPi.GPIO as GPIO


class Pre_launch:
    def is_active(cls):
        out = open('config/launch_armed.txt', "r")
        armed = out.read()
        if armed == 1:
            return True
        else:
            return False
            print('pre-launch is not armed!')
