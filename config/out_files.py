
class Files:

    OUT_DIR = '/home/pi/output/'

    OUT_LOG = 'config/out_log.txt'

    def iterate():
        out_log = None

        try:
            out = open(Files.OUT_LOG, "r")
        except FileNotFoundError:
            out = open(Files.OUT_LOG, "w")
            out.write('0')
            out.close()
            out = open(Files.OUT_LOG, "r")
        except Exception as e:
            print (e)

        mission_num = out.read()
        out.close()
        log = open(Files.OUT_LOG, "w")
        next_mission = int(mission_num) + 1
        log.write(str(next_mission))
        log.close()

    def get_mission_num():
        out_log = open(Files.OUT_LOG, "r")

        mission_num = out_log.read()
        out_log.close()

        return mission_num
