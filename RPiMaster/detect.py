import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class Detect:
	def __init__(self, name, input, latch=-1):
		self.name = name
		GPIO.setup(input, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(latch, GPIO.OUT)
		self.input = input
		self.latch = latch
		
	def wait_for_detect(self):
		print('Waiting to detect ' + self.name)
		GPIO.wait_for_edge(self.input, GPIO.RISING)
		print(self.name + ' has been detected')
		if self.latch is not -1:
			GPIO.output(self.latch, GPIO.LOW)

class detect:
	def __init__(self, name, input, latch=-1):
		self.name = name
		self.wait_time = input

	def wait_for_detect(self):
		print('Waiting to detect ' + self.name)
		sleep(self.wait_time)
		print(self.name + ' has been detected')
