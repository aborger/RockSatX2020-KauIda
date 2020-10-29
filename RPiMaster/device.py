from time import sleep
#import RPi.GPIO as GPIO
#from diablo import *

class Device:
	def __init__(self, name):
		self.name = name
		
	def setup(self):
		print('Setting up ' + self.name + '...')
		
	def activate(self):
		print('Activating ' + self.name + '...')
		
	def deactivate(self):
		print('Deactivating ' + self.name + '...')
		
	def emergency(self):
		print(self.name + 'stopped immediately!')
		
#---------------------------------------------------------------#
#								GoPro							#
#---------------------------------------------------------------#
class gopro(Device):
	pass
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
class rf(Device):
	pass
class battery(Device):
	pass
class ricoh(Device):
	def deactivate(self):
		super().deactivate()
		print('Transfering video...')
#---------------------------------------------------------------#
#							BOOM								#
#---------------------------------------------------------------#
class boom(Device):
	def __init__(self, extend_time):
		print('Setting up boom...')
		self.name = name
		self.extend_time = extend_time
		GPIO.setup(24, GPIO.IN) 
		GPIO.setup(23, GPIO.IN)
		
		
		self.DIABLO = Diablo()        # Create a new Diablo object
		self.DIABLO.Init()                       # Set the board up (checks the board is connected)
		if not DIABLO.foundChip:
			boards = ScanForDiablo()
			if len(boards) == 0:
				print('No Diablo found, check you are attached :)')
			else:
				print('No Diablo at address %02X, but we did find boards:' % (DIABLO.i2cAddress))
				for board in boards:
					print('    %02X (%d)' % (board, board))
				print('If you need to change the I2C address change the set-up line so it is correct, e.g.')
				print('DIABLO.i2cAddress = 0x%02X' % (boards[0]))
			exit()
		#DIABLO.SetEpoIgnore(True)          # Uncomment to disable EPO latch, needed if you do not have a switch / jumper
		self.DIABLO.ResetEpo()                   # Reset the stop switch (EPO) state
											# if you do not have a switch across the two pin header then fit the jumper
											
	def activate(self):
		print('Extending boom...')
		self.DIABLO.SetMotor1(-1.0) # Motor turns on and boom starts extending
		sleep(self.extend_time)
		self.DIABLO.SetMotor1(0.0) # Motor turns off and boom stays extended
		print('Holding boom at extension...')
		
	def deactivate(self):
		print('Retracting boom...')
		self.DIABLO.SetMotor1(+1.0) # Activate the motor in a cw direction (from back of motor)
		sleep(self.extend_time) # wait until closed
		self.DIABLO.SetMotor1(0.0) # Turn off motor
		print('Boom retracted...')
		
	def emergency(self):
		self.DIABLO.MotorsOff()
		
class Boom(Device):
	def __init__(self, extend_time):
		print('Setting up boom...')
		self.extend_time = extend_time
		
	def activate(self):
		print('Extending boom...')
		sleep(self.extend_time)
		print('Holding boom at extension...')
		
	def deactivate(self):
		print('Retracting boom...')
		sleep(self.extend_time)
		print('Boom retracted...')
		


class lock(Device):
	pass