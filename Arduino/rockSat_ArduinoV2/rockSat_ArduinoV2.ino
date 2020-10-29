/* Programmed by Aaron Borger
 * Takes sensor data and rssi and outputs to bluetooth peripherals on Bluefruit LE UART Friend
 * To be used with Pro Tinker 3V, pins vary on other boards
 * BlueFruit pins: 
 * CTS: GND
 * TX0: RX0
 * RX1: TX1
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
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_UART.h"

#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"


SoftwareSerial bluefruitSS = SoftwareSerial(10, 9);

Adafruit_BluefruitLE_UART ble(bluefruitSS, -1, 11, -1);


//                   Setup Sensor
/*=====================================================*/
#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME680 bme; // uses I2C
/*======================================================*/


//                    Setup
/*=======================================================*/
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin(115200);

  // If bluefruit is not found, onboard led is constantly on
  if(!ble.begin(false)) {
    Serial.println("Cant find bluefruit!");
  }

  // If sensor is not found, debug pin is constantly on
  if(!bme.begin()) {
    Serial.println("Sensor not found!");
  }
  else {
    Serial.println("Sensor found!");
  }

  if ( !ble.begin(false) )
  {
    Serial.println("Couldnt find bluefruit!");
  }
  else {
    Serial.println("Bluefruit found!");
  }
  while (!ble.isConnected()) {
    Serial.println("Waiting for connection...");
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
  }
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("Connected!!");
}
/*======================================================*/

// values to format sending rssi
char value_string[5] = {""};
int current = 0;
char c;


/*=======================================================*/
void loop() {
  Serial.println("on loop");
  //                                     RSSI
  //************************************************************************************//
  bool suc = ble.sendCommandCheckOK(F("AT+BLEGETRSSI")); // rssi from bluefruit is sent to TX
  Serial.println(suc);
  while ( ble.available() )
  {
    Serial.println("available");
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
  ble.println(bme.temperature);
  // Pressure
  ble.print(F("AT+GATTCHAR=3,"));
  ble.println(bme.pressure/100.0);
  // Humidity
  ble.print(F("AT+GATTCHAR=4,"));
  ble.println(bme.humidity);
  // Gas
  ble.print(F("AT+GATTCHAR=5,"));
  ble.println(bme.gas_resistance/1000.0);
  // Altitude
  ble.print(F("AT+GATTCHAR=6,"));
  ble.println(bme.readAltitude(SEALEVELPRESSURE_HPA));

  //**********************************************************************************/
  // flashes debug led
  delay(500);
}
/*=====================================================================================*/
