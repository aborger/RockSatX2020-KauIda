from detectors.limit import Limit
from devices.boom import Boom
import RPi.GPIO as GPIO

from config.pins import setup

setup()

boom = Boom()
limit = Limit()

boom.activate()
boom.deactivate()

print(limit.doorShut())


