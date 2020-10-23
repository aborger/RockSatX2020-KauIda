import RPi.GPIO as GPIO

class Detect:
	def __init__(self, input, latch):
		GPIO.setup(input, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(latch, GPIO.OUT)
		self.input = input
		self.latch = latch
		
	def wait_for_detect():
		GPIO.wait_for_edge(self.input, GPIO.RISING)
		print('GSE on')
		GPIO.output(self.latch, GPIO.LOW)