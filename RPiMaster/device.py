from time import sleep 
import RPi.GPIO as GPIO 
from .diablo import *
import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART
import uuid
import dbus

class Device:
	def __init__(self, name):
		self.name = name
		print('Setting up ' + self.name + '...')

	def activate(self):
		print('Activating ' + self.name + '...')

	def deactivate(self):
		print('Deactivating ' + self.name + '...')

	def emergency(self):
		print(self.name + 'stopped immediately!')

#---------------------------------------------------------------#
#				GoPro				#
#---------------------------------------------------------------#
class gopro(Device):
	pass
class Gopro(Device):
	def __init__(self, name):
		super().__init__(name)
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

		self.power.on() #turn on Q3 so GPPower goes to  gnd
		self.sleep(1)
		self.power.off()        #turn off Q3 so GPPower floats
		self.sleep(1)

	def activate(self):
		super().activate()
		#self.power.on()	#turn on Q3 so GPPower goes to  gnd
		#self.sleep(1)
		#self.power.off()	#turn off Q3 so GPPower floats
		#self.sleep(1)

		#This section starts recording and stops recording
		#A falling edge starts/stop recording

		self.rec.off()	#turn OFF Q1 so GPRec now floats
		self.sleep(5)	#GoPro seems to need this set up time
		self.rec.on()	#turn ON Q1 so GPRec goes to gnd falling edge starts record
		#self.sleep(4)	#record time
		#self.rec.off()
		#self.rec.on() #Q1 on, GPRec go low and stops recording
		#self.sleep(2)

	def deactivate(self):
		super().deactivate()
		self.rec.off()
		self.sleep(2) # Waits to stop recording
		self.rec.on() #Q1 on, GPRec go low and stops recording
		self.sleep(2)
		self.power.on()
		self.sleep(5)
		self.power.off()
		self.sleep(1)
		self.gp_enable.off()

#---------------------------------------------------------------#
#			RF					#
#---------------------------------------------------------------#
class rf:
	pass
class Rf(Device):
	def unwrap(self, val):
		if isinstance(val, (dbus.Array, list, tuple)):
			unwrapped_str = ''
			for x in val:
				unwrapped_str = unwrapped_str + self.unwrap(x)
			return unwrapped_str
		if isinstance(val, dbus.Byte):
			return str(val)

	def setup_thread(self):
		# Service and Character UUID's
		UART_SERVICE_UUID = uuid.UUID('6E400001-B5A3-F393-E0A9-E50E24DCCA9E')
		TX_CHAR_UUID      = uuid.UUID('6E400002-B5A3-F393-E0A9-E50E24DCCA9E')
		RX_CHAR_UUID      = uuid.UUID('6E400003-B5A3-F393-E0A9-E50E24DCCA9E')

		SENSE_SERVICE_UUID = uuid.UUID('00006969-6969-6969-6969-696969696969')
		RSSI_CHAR_UUID    = uuid.UUID('00000420-0000-1000-8000-00805f9b34fb')
		TEMP_CHAR_UUID    = uuid.UUID('00000421-0000-1000-8000-00805f9b34fb')
		PRESS_CHAR_UUID   = uuid.UUID('00000422-0000-1000-8000-00805f9b34fb')
		HUM_CHAR_UUID     = uuid.UUID('00000423-0000-1000-8000-00805f9b34fb')
		GAS_CHAR_UUID     = uuid.UUID('00000424-0000-1000-8000-00805f9b34fb')
		ALT_CHAR_UUID     = uuid.UUID('00000425-0000-1000-8000-00805f9b34fb')

		self.ble.clear_cached_data()

		# get adapter and power on
		adapter = self.ble.get_default_adapter()
		adapter.power_on()

		# Disconnect currently connected devices
		self.ble.disconnect_devices()

		# Connect to UART device
		try:
			print('Scanning for devices...')
			adapter.start_scan()
			self.device = UART.find_device()
			if self.device is None:
				raise RuntimeError('Failed to find UART device!')
		finally:
			adapter.stop_scan()

		self.device.connect()

		# Discover Services and Characteristics
		print('Discovering...')
		self.device.discover([SENSE_SERVICE_UUID], [RSSI_CHAR_UUID,
				TEMP_CHAR_UUID, PRESS_CHAR_UUID,
				HUM_CHAR_UUID, GAS_CHAR_UUID, ALT_CHAR_UUID])

		# Find Services and Characteristics
		print('Finding services...')
		sensors  = self.device.find_service(SENSE_SERVICE_UUID)
		self.chars = {
			"rssi":     sensors.find_characteristic(RSSI_CHAR_UUID),
			"temp":     sensors.find_characteristic(TEMP_CHAR_UUID),
			"pressure": sensors.find_characteristic(PRESS_CHAR_UUID),
			"humidity": sensors.find_characteristic(HUM_CHAR_UUID),
			"gas":      sensors.find_characteristic(GAS_CHAR_UUID),
			"alt":      sensors.find_characteristic(ALT_CHAR_UUID)
		}
		file = open("rfOutput.csv", "w")
		file.write('RSSI (dB),TEMP (*C),PRESSURE (hPa),HUMIDITY (%),GAS (KOhms),ALT (m)\n')
		#print('RSSI:  TEMP:  PRESSURE:  HUMIDITY:  GAS:  ALT: ')
		file.close()

	def setup(self):
		self.ble = Adafruit_BluefruitLE.get_provider()
		self.ble.initialize()
		self.ble.run_mainloop_with(self.setup_thread)

	def activate_thread(self):
		rssi     = str(self.unwrap(self.chars["rssi"].read_value()))
		temp     = str(self.unwrap(self.chars["temp"].read_value()))
		pressure = str(self.unwrap(self.chars["pressure"].read_value()))
		humidity = str(self.unwrap(self.chars["humidity"].read_value()))
		gas      = str(self.unwrap(self.chars["gas"].read_value()))
		alt	 = str(self.unwrap(self.chars["alt"].read_value()))
		file = open("rfOutput.csv", "a") 
		print(' ' + rssi + '    ' + temp + '   ' + pressure + '    ' + humidity + '    ' + gas + '    ' + alt)
		file.write(rssi + ',' + temp + ',' + pressure + ',' + humidity + ',' + gas + ',' + alt + '\n')
		file.close()

	def activate(self):
		self.ble.run_mainloop_with(self.activate_thread)

	def deactivate_thread(self):
		self.device.disconnect()

	def deactivate(self):
		super().deactivate()
		self.ble.run_mainloop_with(self.deactivate_thread)


#---------------------------------------------------------------#
#			Battery					#
#---------------------------------------------------------------#
class battery(Device):
	pass
#---------------------------------------------------------------#
#			Ricoh					#
#---------------------------------------------------------------#
class ricoh(Device):
	def deactivate(self):
		super().deactivate()
		print('Transfering video...')
#---------------------------------------------------------------#
#				BOOM				#
#---------------------------------------------------------------#
class Boom(Device):
	def __init__(self, extend_time):
		print('Setting up boom...')
		self.extend_time = extend_time
		GPIO.setup(24, GPIO.IN) 
		GPIO.setup(23, GPIO.IN)


		self.DIABLO = Diablo()        # Create a new Diablo object
		self.DIABLOi2cAddress = '7x37'
		self.DIABLO.Init()                       # Set the board up (checks the board is connected)
		if not self.DIABLO.foundChip:
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
		self.DIABLO.SetEncoderMoveMode(True)
		self.DIABLO.ResetEpo()                   # Reset the stop switch (EPO) state
											# if you do not have a switch across the two pin header then fit the jumper

	def activate(self, step):
		self.DIABLO.SetMotor1(+1.0) # Motor turns on and boom starts extending
		sleep(step) # change to rotation count DIABLO.EncoderMoveMotor
		self.DIABLO.SetMotor1(0.0) # Motor turns off and boom stays extended
		#self.DIABLO.EncoderMoveMotor1(1)

	def retract(self, step):
		self.DIABLO.SetMotor1(-1.0)
		sleep(step)

	def deactivate(self):
		self.DIABLO.SetMotor1(0.0) # Turn off motor
		print('Boom retracted...')

	def emergency(self):
		self.DIABLO.MotorsOff()

class boom(Device):
	def __init__(self, extend_time):
		print('Setting up boom...')
		self.extend_time = extend_time

	def activate(self):
		print('Extending boom...')
		sleep(self.extend_time)
		print('Holding boom at extension...')

	def retract(self):
		print('Retracting boom...')

	def deactivate(self):
		print('Boom retracted...')


#---------------------------------------------------------------#
#				Lock				#
#---------------------------------------------------------------#
class Lock(Device):
	def __init__(self):
		super().__init__('Lock')
		GPIO.setup(22, GPIO.OUT)
		GPIO.output(22, 1)


class lock(Device):
	pass
