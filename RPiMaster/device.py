class Device:
	def __init__(self):
		pass
		
	def setup(self):
		pass
		
	def activate(self):
		pass
		
	def deactivate(self):
		pass
		
#---------------------------------------------------------------#
#								GoPro							#
#---------------------------------------------------------------#
class Gopro(Device):
	def setup(self):
		from gpiozero import LED
		from time import sleep
		self.sleep = sleep


		self.power = LED(21)
		self.rec = LED(26)
		self.gp_enable = LED(13)

		self.power.off()
		self.rec.off()
		self.gp_enable.off()

		self.gp_enable.on()	#high, closes relay
		
	def activate(self):
		self.power.on()	#turn on Q3 so GPPower goes to  gnd
		self.sleep(1)
		self.power.off()	#turn off Q3 so GPPower floats
		self.sleep(1)

		#This section starts recording and stops recording
		#A falling edge starts/stop recording

		self.rec.off()	#turn OFF Q1 so GPRec now floats
		self.sleep(5)	#GoPro seems to need this set up time
		self.rec.on()	#turn ON Q1 so GPRec goes to gnd falling edge starts record
		self.sleep(4)	#record time
		self.rec.off()
		self.sleep(2)	#still recording
		self.rec.on()	#Q1 on, GPRec go low and stops recording
		self.sleep(2)
		
	def deactivate(self):
		self.power.on()
		self.sleep(5)
		self.power.off()
		self.sleep(1)
		self.gp_enable.off()

		print("GoPro done")
		
#---------------------------------------------------------------#
#								RF								#
#---------------------------------------------------------------#
class Rf(Device):

class IMU(Device):

class Battery(Device):

class Ricoh(Device):

class Boom(Device):