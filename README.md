# RockSatX2020-KauIda
Mission control and test software for use on the KauIda RockSat-X 2020 mission.

The software is split into two parts, the software for the arduino which runs the RF experiment, and the software for the Raspberry Pi in charge of the mission control.

# Arduino and RF experiment
The arduino (Pro Tinker) is connected to an Adafruit Bluefruit LE UART Friend, and an Adafruit BME680 sensor.
The connections are as follows:

| Pro Tinker | Bluefruit |    | Pro Tinker | BME680 |
|:----------:|:---------:|----|:----------:|:------:|
| Vin        | 5V        |    | Vin        | 5V     |
| GND        | GND       |    | GND        | GND    |
| CTS        | GND       |    | SCK        | A5     |
| TX0        | RX0       |    | SDI        | A4     |
| RX1        | TX1       |

The Pro Tinker is powered by a 5v button cell battery.

The Bluefruit's bluetooth services and characteristics must be setup before it is operational. The rockSat_Arduino_setup script can be ran to set it up. This script adds a service for the sensor data, and adds a characteristic for each individual sensor (RSSI, temperature, pressure, humidity, gas resistance, and altitude).

Once setup the rockSat_ArduinoV2 program can be uploaded and ran on the Arduino. This program waits for a connection and then repeatedly writes the sensor data to the bluetooth characteristics until powered off.

# Raspberry Pi and Mission Control
The Raspberry Pi must control many different devices such as (The Gopro, RF receiver, Ricoh 360 degree camera, Scissor Boom, and door lock). These devices all inherit from the Device class which is found in ```RPiMaster/device.py``` The Device class demonstrates the structure each child class follows. The device class is as follows:

```python
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
 ```
 
As seen each device has a name and three methods (activate, deactivate, and emergency). Each child may override these methods. These methods are the only public methods, they are the methods called in the Mission Control script. Some devices contain other private supporting methods.


 
