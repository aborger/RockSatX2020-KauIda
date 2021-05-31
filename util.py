import time

LOG = '/home/pi/output/mission.log'

class Log:
    def __init__(self):
        print('------------------- Log --------------------', file=open(LOG, "w"))
        self.TE_epoch = time.time()
        self.TE_occur = False

    def set_epoch(self):
        self.TE_epoch = time.time()
        self.TE_occur = True

    def log(self, log_str):
        print(log_str)
        print('[', self.since_epoch(), ']', log_str, file=open(LOG, "a"))

    def since_epoch(self):
        time_since = time.time() - self.TE_epoch
        if not self.TE_occur:
            time_since *= -1
        return str(format(time_since, '.4f'))
