import RPi.GPIO as GPIO
from time import sleep
import os

GPIO.setmode(GPIO.BCM)

class Detect:
	# edge is 'r' for rising or 'f' for falling
	def __init__(self, name, input=16, latch=-1, edge='r'):
		self.name = name
		self.input = input
		self.latch = latch
		if edge == 'r':
			self.edge = GPIO.RISING
		elif edge == 'f':
			self.edge = GPIO.FALLING
		else:
			raise ValueError("Edge not recognized")
		GPIO.setup(self.input, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		if self.latch is not -1:
			GPIO.setup(self.latch, GPIO.OUT)


	def wait_for_detect(self):
		print('Waiting to detect ' + self.name)
		GPIO.wait_for_edge(self.input, self.edge)
		print(self.name + ' has been detected')
		if self.latch is not -1:
			GPIO.output(self.latch, GPIO.LOW)

class detect:
	def __init__(self, name, input=5, latch=-1):
		self.name = name
		self.wait_time = input

	def wait_for_detect(self):
		print('Waiting to detect ' + self.name)
		sleep(self.wait_time)
		print(self.name + ' has been detected')

class Limit:
	def __init__(self, power, detect):
		self.detect = detect
		GPIO.setup(power, GPIO.OUT)
		GPIO.output(power, 1)
		GPIO.setup(self.detect, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

	def doorShut(self):
		if GPIO.input(self.detect) == 1:
			return False
		else:
			print("Door shut detected!")
			return True
