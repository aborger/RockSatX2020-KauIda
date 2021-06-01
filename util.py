import time
from config.out_files import Files


class Log:
    def __init__(self):
        mission_num = str(int(Files.get_mission_num()) + 1)
        self.LOG = Files.OUT_DIR + 'mission_logs/mission' + mission_num + '.log'
        try:
            print('------------------- Log --------------------', file=open(self.LOG, "w"))
        except:
            print('cant open log')
        self.TE_epoch = time.time()
        self.TE_occur = False


    def set_epoch(self):
        self.TE_epoch = time.time()
        self.TE_occur = True

    def log(self, log_str):
        print('[', self.since_epoch(), ']', log_str)
        try:
            print('[', self.since_epoch(), ']', log_str, file=open(self.LOG, "a"))
        except:
            print('cant write to file')

    def since_epoch(self):
        time_since = time.time() - self.TE_epoch
        if not self.TE_occur:
            time_since *= -1
        return str(format(time_since, '.4f'))
