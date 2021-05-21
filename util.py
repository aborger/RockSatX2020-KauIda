import time

LOG = '/home/pi/output/mission.log'

def start_log():
    print('------------------- Log --------------------', file=open(LOG, "w"))

def log(log_str):
    print('[', time.asctime(time.localtime(time.time())), ']', log_str, file=open(LOG, "a"))

