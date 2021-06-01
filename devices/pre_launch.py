import RPi.GPIO as GPIO
import os

class Pre_launch:
    def is_active():
        print(os.getcwd())
        out = open('config/launch_armed.txt', "r")
        armed = out.read()
        if armed == '1':
            return True
        else:
            return False
            print('pre-launch is not armed!')
