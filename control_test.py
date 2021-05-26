import RPi.GPIO as GPIO
from devices.lock import Lock
import config.pins as pins

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Device Control')
    parser.add_argument("device", metavar="<command>", help="any of the devices")
    parser.add_argument("function", metavar="<command>", help="'activate' or 'deactivate'")

    args = parser.parse_args()

    device = None
    pins.setup()

    if args.device == 'boom':
        from devices.boom import Boom
        device = Boom()

    elif args.device == 'lock':
        from devices.lock import Lock
        device = Lock()
    elif args.device == 'rf':
        from devices.rf_experiment.rf import RF
        device = RF()
    elif args.device == 'ricoh':
        from devices.ricoh import Ricoh
        device = Ricoh()
    elif args.device == 'arducam':
        from devices.arducam import ArduCam
        device = ArduCam()

    else:
        raise ValueError

    try:
      if args.function == 'activate':
            device.activate()
      elif args.function == 'deactivate':
            device.deactivate()
      else:
            raise ValueError
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as e:
        print(e)

GPIO.cleanup()
