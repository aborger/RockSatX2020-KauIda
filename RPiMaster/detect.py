#import RPi.GPIO as GPIO
from time import sleep

class Detect:
	def __init__(self, name, input, latch):
		self.name = name
		self.wait_time = input
		#GPIO.setup(input, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		#GPIO.setup(latch, GPIO.OUT)
		#self.input = input
		#self.latch = latch
		
	def wait_for_detect(self):
		#GPIO.wait_for_edge(self.input, GPIO.RISING)
		sleep(self.wait_time)
		print(self.name + ' has been detected')
		#GPIO.output(self.latch, GPIO.LOW)