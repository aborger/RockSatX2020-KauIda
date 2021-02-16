# a new version of mission control using a state machine
from RPiMaster.device import *
import os
import RPi.GPIO as GPIO
import threading
from time import sleep

# Start bluetooth
os.system("./bluetoothON.sh")

# Initialize devices
gopro = Gopro()
rf = Rf()
ricoh = Ricoh()
boom = Boom(5)
door_lock = Lock()

TE1 = 16
LIMIT = 27
HIGH = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(TE1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LIMIT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(HIGH, GPIO.OUT)
GPIO.output(HIGH, 1)

rf_setup = threading.Thread(target=rf.setup)
rf_activate = threading.Thread(target=rf.activate)

class StateMachine:
	def __init__(self):
		self.state = 'Setup'
		self.States = { 'Setup': self.setup,
				'TE1_Detect': self.te1_detect,
				'Extend': self.extend,
				'Retract': self.retract,
				'Deactivate': self.deactivate,
				'Stop': self.stop }

	def setup(self):
		gopro.setup()
		boom.setup()
		rf_setup.start()

		gopro.activate()
		self.state = 'TE1_Detect'

	def te1_detect(self):
		if GPIO.input(TE1):
			self.state = 'Extend'
		sleep(.1)
		#elif GPIO.input(LIMIT):
			#self.state = 'Stop'

	def extend(self):
		#if not rf_activate.is_alive():


		boom.activate(1)
		if not GPIO.input(LIMIT):
			self.state = 'Retract'


	def retract(self):
		rf.activate()
		boom.deactivate()
		self.state = 'Stop'

	def deactivate(self):
		door_lock.activate()
		boom.shutdown()
		ricoh.deactivate()
		rf.deactivate()
		gopro.deactivate()

	def stop(self):
		boom.shutdown()
		ricoh.deactivate()
		rf.deactivate()
		gopro.deactivate()
		GPIO.cleanup()
		#quit()

	def error(self):
		print('Error going to ' + self.state)
		quit()

	def next_state(self):
		print('Next state: ' + self.state)
		state_func = self.States.get(self.state, self.error)
		state_func()

sm = StateMachine()

while True:
	sm.next_state()
