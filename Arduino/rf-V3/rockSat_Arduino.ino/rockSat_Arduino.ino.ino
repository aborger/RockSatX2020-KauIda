/* Programmed by Aaron Borger
 * Takes sensor data and rssi and outputs to bluetooth peripherals on Bluefruit LE UART Friend
 * To be used with Pro Tinker 3V, pins vary on other boards
 * BlueFruit pins: 
 * CTS: 11
 * TX0: 10
 * RX1: 9
 * VIN: 5V
 * GND: GND
 * 
 * BME sensor pins:
 * VIN: 5V
 * GND: GND
 * SCK: A5
 * SDI: A4
 */

#include <Arduino.h>
#include <SPI.h>
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_SPI.h"
#include "Adafruit_BluefruitLE_UART.h"
#include "BluefruitConfig.h"

#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"


// Bluefruit uses Serial (RX and TX pins)
//Adafruit_BluefruitLE_UART ble(Serial, -1);

SoftwareSerial bluefruitSS = SoftwareSerial(BLUEFRUIT_SWUART_TXD_PIN, BLUEFRUIT_SWUART_RXD_PIN);

Adafruit_BluefruitLE_UART ble(bluefruitSS, BLUEFRUIT_UART_MODE_PIN, BLUEFRUIT_UART_CTS_PIN, BLUEFRUIT_UART_RTS_PIN);

//                   Setup Sensor
/*=====================================================*/
#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME680 bme; // uses I2C
/*======================================================*/

int check = 6; // used for debug
int bluetoothPower = 5;

//                    Setup
/*=======================================================*/
void setup() {
  // Set debug pins to output
  pinMode(check, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(bluetoothPower, OUTPUT);

  delay(4000);

  digitalWrite(bluetoothPower, HIGH);
  

  // If bluefruit is not found, onboard led is constantly on
  if(!ble.begin(false)) {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  // Turn onboard led off
  digitalWrite(LED_BUILTIN, LOW);

  // If sensor is not found, debug pin is constantly on
  if(!bme.begin()) {
    digitalWrite(check, HIGH);
    while(1);
  }

  // while no device is connected flash onboard led
  
  while (!ble.isConnected()) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    delay(500);
  }
  
  digitalWrite(LED_BUILTIN, HIGH);
}
/*======================================================*/

// values to format sending rssi
char value_string[5] = {""};
int current = 0;
char c;


/*=======================================================*/
void loop() {
  // debug pin will flash if sending data
  digitalWrite(check, HIGH); 

  //                                     RSSI
  //************************************************************************************//
  ble.println(F("AT+BLEGETRSSI")); // rssi from bluefruit is sent to TX
  while ( ble.available() )
  {
    c = ble.read(); // read individual rssi character
    // if character is number add to current char in char array
    if (c >= '0' && c <= '9') {
      value_string[current] = c;
      current++;
     }
  } 
  current = 0; // set current back to 0

  // set rssi characteristic to new value
  ble.print(F("AT+GATTCHAR=1,"));
  ble.println(atoi(value_string));

  // empty char array
  for (int a = 0; a < 5; a++) {
    value_string[a] = "";
  }

  //                                   Sensors
  //*********************************************************************************/
  // Sets all sensor characteristics to their respective values
  // Temp
  ble.print(F("AT+GATTCHAR=2,"));
  ble.println(int(bme.temperature*100));
  // Pressure
  ble.print(F("AT+GATTCHAR=3,"));
  ble.println(bme.pressure);
  // Humidity
  ble.print(F("AT+GATTCHAR=4,"));
  ble.println(int(bme.humidity*100));
  // Gas
  ble.print(F("AT+GATTCHAR=5,"));
  ble.println(bme.gas_resistance/10);
  // Altitude
  ble.print(F("AT+GATTCHAR=6,"));
  ble.println(int(bme.readAltitude(SEALEVELPRESSURE_HPA)*100));

  //**********************************************************************************/
  // flashes debug led
  digitalWrite(check, LOW);
  delay(500);
}
/*=====================================================================================*/
