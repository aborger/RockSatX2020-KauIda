import RPi.GPIO as GPIO
from devices.lock import Lock
import config.pins as pins
from time import sleep
from config.timing import Timing
from util import Log

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Device Control')
    parser.add_argument("device", metavar="<command>", help="any of the devices")
    parser.add_argument("function", metavar="<command>", help="'activate' or 'deactivate'")

    args = parser.parse_args()

    device = None
    pins.setup()
    log = Log()

    if args.device == 'boom':
        from devices.boom import Boom
        device = Boom()

    elif args.device == 'lock':
        from devices.lock import Lock
        device = Lock()
    elif args.device == 'rf':
        import threading
        from devices.rf_experiment.rf import RF
        device = RF(log)
        rf_usb = threading.Thread(target=device.power_usb)
        rf_pitooth = threading.Thread(target=device.start_pitooth)
        rf_go = threading.Thread(target=device.go)

        rf_usb.start()
        rf_pitooth.start()

        rf_usb.join()
        rf_pitooth.join()

        sleep(Timing.RF_CONNECT_DELAY)

        rf_go.start()




    elif args.device == 'ricoh':
        from devices.ricoh import Ricoh
        device = Ricoh(log)
    elif args.device == 'arducam':
        from devices.arducam import ArduCam
        device = ArduCam(log)
    elif args.device == 'pre-launch':
        from devices.pre_launch import Pre_launch
        print('is active: ', Pre_launch.is_active())

    else:
        raise ValueError

    try:
      if args.function == 'activate':
          device.activate()
          if args.device == 'boom':
              sleep(10)
      elif args.function == 'deactivate':
           device.deactivate()
           if args.device == 'boom':
               sleep(10)
      elif args.function == 'shutdown':
            device.shutdown()
      elif args.function == 'setup':
            device.setup()
      else:
            raise ValueError
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as e:
        print(e)

#GPIO.cleanup()
