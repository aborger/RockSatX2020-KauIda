import RPi.GPIO as GPIO
from devices.lock import Lock
import config.pins as pins
from time import sleep

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
        import threading
        from devices.rf_experiment.rf import RF
        device = RF()
        rf_usb = threading.Thread(target=device.power_usb)
        rf_pitooth = threading.Thread(target=device.start_pitooth)
        rf_setup = threading.Thread(target=device.setup)

        rf_usb.start()
        rf_pitooth.start()

        rf_usb.join()
        rf_pitooth.join()

        sleep(8)

        rf_setup.start()
        rf_setup.join()



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
          if args.device == 'rf':
              rf_activate = threading.Thread(target=device.activate)
              rf_activate.start()
          else:
              device.activate()
      elif args.function == 'deactivate':
            device.deactivate()
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