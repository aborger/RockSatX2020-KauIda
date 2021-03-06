"""

* The RF class communicates with the Bluetooth chip and outputs the data.

* The Adafruit Bluefruit library must be used in a thread

* Each method inherited from device calls a private method that will be run in a thread

* mission_control.py also uses threads, but creating another thread in rf.py maintains encapsulation

* Author: Aaron Borger <aborger@nnu.edu, (307)534-6265>

"""

# Ill probably need to include telem

from devices.device import Device
from devices.rf_experiment import telemetry

import os
import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART
import uuid
import dbus


class RF(Device):

    def __init__(self):
        self.sensor_values = [0, 0, 0, 0, 0]	# The values of the sensors that are edited by __unwrap and written to telemetry and rfOutput.csv
        self.ble = None

        os.system("devices/rf_experiment/bluetoothON.sh")		# Ensures the bluetoothctl adapter is on


    # Formats data transmitted from bluetooth into a string
    def __unwrap(self, sensor_val, sensor_ID):
        if isinstance(sensor_val, (dbus.Array, list, tuple)):	# Sensor data varies in type, if it is one of these it is unwrapped again to get raw dbus.Byte value
            unwrapped_str = ''
            for item in sensor_val:
                unwrapped_str += self.__unwrap(item, sensor_ID)

            unwrapped_str = unwrapped_str.replace('=', '')	# If the value is smaller than normal, the bluetooth module places an '=' in the extra digits
            return unwrapped_str

        if isinstance(sensor_val, dbus.Byte):		# The sensor value is type dbus.Byte so just return the string version
            if sensor_ID != -1:			# The gas sensor does not need to be converted
                try:				# Occasionally data is messed up, so that data is skipped
                    return str(sensor_val)
                except Exception as e:
                    print(e)
            return ''

    # Adafruit_BluefruitLE must be run in threads
    # To ensure encapsulation and ease of reading the main script the setup, activation and deactivation thread methods are required
    def __setup_thread(self):
        # Bluetooth UUIDs
        SENSE_SERVICE_UUID = uuid.UUID('00006969-6969-6969-6969-696969696969')
        RSSI_CHAR_UUID    = uuid.UUID('00000420-0000-1000-8000-00805f9b34fb')
        TEMP_CHAR_UUID    = uuid.UUID('00000421-0000-1000-8000-00805f9b34fb')
        PRESS_CHAR_UUID   = uuid.UUID('00000422-0000-1000-8000-00805f9b34fb')
        HUM_CHAR_UUID     = uuid.UUID('00000423-0000-1000-8000-00805f9b34fb')
        GAS_CHAR_UUID     = uuid.UUID('00000424-0000-1000-8000-00805f9b34fb')
        ALT_CHAR_UUID     = uuid.UUID('00000425-0000-1000-8000-00805f9b34fb')

        self.ble.clear_cached_data()

        adapter = self.ble.get_default_adapter()
        adapter.power_on()

        self.ble.disconnect_devices()

        try:
            print('Scanning for devices...')
            adapter.start_scan()
            self.device = UART.find_device()
            if self.device is None:
                 raise RuntimeError('Failed to find UART device!')

        finally:
            adapter.stop_scan()

        self.device.connect()

        # Discover Bluetooth services and characteristics
        self.device.discover([SENSE_SERVICE_UUID], [RSSI_CHAR_UUID,
                              TEMP_CHAR_UUID, PRESS_CHAR_UUID,
                              HUM_CHAR_UUID, GAS_CHAR_UUID, ALT_CHAR_UUID])

        # Find Bluetooth services and characteristics
        sensors = self.device.find_service(SENSE_SERVICE_UUID)
        self.chars = {
	    "rssi":     sensors.find_characteristic(RSSI_CHAR_UUID),
	    "temp":     sensors.find_characteristic(TEMP_CHAR_UUID),
	    "pressure": sensors.find_characteristic(PRESS_CHAR_UUID),
	    "humidity": sensors.find_characteristic(HUM_CHAR_UUID),
	    "gas":      sensors.find_characteristic(GAS_CHAR_UUID),
	    "alt":      sensors.find_characteristic(ALT_CHAR_UUID)
	}

        # Setup rfOutput.csv
        output_file = open("rfOutput.csv", "w")
        output_file.write('RSSI (dB),TEMP (*C),PRESSURE (hPa),HUMIDITY (%),GAS (KOhms),ALT (m)\n')
        output_file.close()


    def __activate_thread(self):
        self.sensor_values = [0, 0, 0, 0, 0]	# Reset sensor values

        # Read sensors and unwrap.
        rssi     = str(self.__unwrap(self.chars["rssi"].read_value(), 0))
        temp     = str(self.__unwrap(self.chars["temp"].read_value(), 1))
        pressure = str(self.__unwrap(self.chars["pressure"].read_value(), 2))
        humidity = str(self.__unwrap(self.chars["humidity"].read_value(), 3))
        gas      = str(self.__unwrap(self.chars["gas"].read_value(), -1))
        alt	 = str(self.__unwrap(self.chars["alt"].read_value(), 4))

        # Output data through standard output, .csv, and telemetry
        output_file = open("rfOutput.csv", "a")
        print(' ' + rssi + '    ' + temp + '   ' + pressure + '    ' + humidity + '    ' + gas + '    ' + alt)
        output_file.write(rssi + ',' + temp + ',' + pressure + ',' + humidity + ',' + gas + ',' + alt + '\n')
        output_file.close()
        telemetry.write(self.sensor_values)

    def __deactivate_thread(self):
        self.device.disconnect()

    # These methods are inherited from device.py and are called in the main mission_control.py script
    def setup(self):
        self.ble = Adafruit_BluefruitLE.get_provider()
        self.ble.initialize()
        self.ble.run_mainloop_with(self.__setup_thread)

    def activate(self):
        self.ble.run_mainloop_with(self.__activate_thread)

    def deactivate(self):
        self.ble.run_mainloop_with(self.__deactivate_thread)

    def shutdown(self):
        return
