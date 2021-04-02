from time import sleep
import RPi.GPIO as GPIO
from RPiMaster.diablo import *
import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART
import uuid
import dbus
import os
#from RPiMaster.telemetry import Telem

class Device:
	def __init__(self, name):
		self.name = name

	def setup(self):
		print('Setting up ' + self.name + '...')

	def activate(self):
		print('Activating ' + self.name + '...')

	def deactivate(self):
		print('Deactivating ' + self.name + '...')

	def shutdown(self):
		print('Shutting down ' + self.name + '...')

#---------------------------------------------------------------#
#				GoPro				#
#---------------------------------------------------------------#
class gopro(Device):
	pass
class Gopro(Device):
	def __init__(self):
		super().__init__('GoPro')

	def setup(self):
		super().setup()
		from gpiozero import LED
		from time import sleep
		self.sleep = sleep


		self.power = LED(20)
		self.rec = LED(26)
		self.gp_enable = LED(13)

		self.power.off()
		self.rec.off()
		self.gp_enable.off()


	def activate(self):
		super().activate()

		self.gp_enable.on()
		# Power on
		self.power.on()
		self.sleep(1)
		self.power.off()
		self.sleep(1)

		# Record
		self.rec.off()
		self.sleep(5)
		self.rec.on()

	def deactivate(self):
		super().deactivate()
		# stop record
		self.rec.off()
		self.sleep(2)
		self.rec.on()
		self.sleep(2)

		# power off
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
	def __init__(self):
		super().__init__('RF')
		self.SENSOR_PINS = [15, 16, 1, 4, 5]
		self.PRS_PIN = 6
		self.telem = None
		self.sensor_values = [0, 0, 0, 0, 0]

	def __unwrap(self, val, sensorID):
		if isinstance(val, (dbus.Array, list, tuple)):
			unwrapped_str = ''
			for x in val:
				unwrapped_str = unwrapped_str + self.__unwrap(x, sensorID)
			return unwrapped_str
		if isinstance(val, dbus.Byte):
			if sensorID != -1:
				self.sensor_values[sensorID] = int(val)
			return str(val)

	def __setup_thread(self):
		# Service and Character UUID's
		#self.telem = Telem()
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
		file.close()
		print('rf setup')

	def setup(self):
		super().setup()
		self.ble = Adafruit_BluefruitLE.get_provider()
		self.ble.initialize()
		self.ble.run_mainloop_with(self.__setup_thread)

	def __activate_thread(self):
		# reset sensor values
		self.sensor_values = [0, 0, 0, 0, 0]

		rssi     = str(self.__unwrap(self.chars["rssi"].read_value(), 0))
		temp     = str(self.__unwrap(self.chars["temp"].read_value(), 1))
		pressure = str(self.__unwrap(self.chars["pressure"].read_value(), 2))
		humidity = str(self.__unwrap(self.chars["humidity"].read_value(), 3))
		gas      = str(self.__unwrap(self.chars["gas"].read_value(), -1))
		alt	 = str(self.__unwrap(self.chars["alt"].read_value(), 4))
		file = open("rfOutput.csv", "a")
		print(' ' + rssi + '    ' + temp + '   ' + pressure + '    ' + humidity + '    ' + gas + '    ' + alt)
		file.write(rssi + ',' + temp + ',' + pressure + ',' + humidity + ',' + gas + ',' + alt + '\n')
		file.close()
		os.system("./rpiScripts/telem/telem")
		#self.telem.write(self.sensor_values)

	def activate(self):
		self.ble.run_mainloop_with(self.__activate_thread)

	def __deactivate_thread(self):
		self.device.disconnect()

	def deactivate(self):
		super().deactivate()
		self.ble.run_mainloop_with(self.__deactivate_thread)



#---------------------------------------------------------------#
#			Ricoh					#
#---------------------------------------------------------------#
class Ricoh(Device):
	def __init__(self):
		super().__init__('Ricoh')

	def activate(self):
		super().activate()
		os.system("ptpcam -R 0x101c,0,0,1")

	def deactivate(self):
		super().deactivate()
		os.system("ptpcam -R 0x1018,0xFFFFFFFF")
		sleep(5)
		os.system("sudo adb pull /sdcard/DCIM/100RICOH/ /home/pi/Videos")
		print("Transfer Complete")
		os.system("ptpcam -D")

class ricoh(Device):
	def deactivate(self):
		super().deactivate()
		print('Transfering video...')
#---------------------------------------------------------------#
#				BOOM				#
#---------------------------------------------------------------#
class Boom(Device):
	def __init__(self, extend_time):
		super().__init__('Boom')
		self.extend_time = extend_time

	def setup(self):
		self.PWM_PIN = 12
		self.DIR_PIN = 26

		GPIO.setup(self.PWM_PIN, GPIO.OUT)
		GPIO.setup(self.DIR_PIN, GPIO.OUT)
		sleep(1)
		self.motor = GPIO.PWM(self.PWM_PIN, 100)

	def activate(self, step):
		GPIO.output(self.DIR_PIN, GPIO.HIGH)
		self.motor.start(100)
		#sleep(step)
		#self.motor.start(0)

	def deactivate(self, step):
		GPIO.output(self.DIR_PIN, GPIO.LOW)
		self.motor.start(100)
		#sleep(step)
		#self.motor.start(0)

	def shutdown(self):
		self.motor.start(0)

class Boom_diablo(Device):
	def __init__(self, extend_time):
		super().__init__('Boom')
		self.extend_time = extend_time

	def setup(self):
		super().setup()
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

	def deactivate(self, step):
		self.DIABLO.SetMotor1(-1.0)
		sleep(step)
		self.DIABLO.SetMotor1(0.0)

	def shutdown(self):
		super().shutdown()
		self.DIABLO.SetMotor1(0.0) # Turn off motor
		print('Boom retracted...')



class boom(Device):
	def __init__(self):
		super().__init__('boom')

	def setup(self, extend_time):
		super.setup()
		self.extend_time = extend_time

	def activate(self):
		super.activate()
		sleep(self.extend_time)
		print('Holding boom at extension...')

	def deactivate(self):
		super.deactivate()

	def shutdown(self):
		super.shutdown()

#---------------------------------------------------------------#
#				Lock				#
#---------------------------------------------------------------#
class lock(Device):
	pass


if __name__ == '__main__':
	from diablo import *
	import argparse
	parser = argparse.ArgumentParser(description='Control Devices')
	parser.add_argument("command", metavar="<command>", help="'gopro', 'rf', 'ricoh', 'boom', 'lock'")
	parser.add_argument("--sig", help = "'set', 'on', 'off', '!'")

	args = parser.parse_args()

	controller = None

	if args.command == 'gopro':
		controller = Gopro()

	elif args.command == 'rf':
		controller = Rf()

	elif args.command == 'ricoh':
		controller = Ricoh()

	elif args.command == 'boom':
		controller = Boom()

	elif args.command == 'lock':
		controller = Lock()

	controller.setup()

	if args.sig == 'on':
		controller.activate()

	elif args.sig == 'off':
		controller.deactivate()

	elif args.sig == '!':
		controller.shutdown()
