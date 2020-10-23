#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_UART.h"
#include "BluefruitConfig.h"

#if SOFTWARE_SERIAL_AVAILABLE
  #include <SoftwareSerial.h>
#endif

    #define FACTORYRESET_ENABLE         0
    #define MINIMUM_FIRMWARE_VERSION    "0.6.6"
    #define MODE_LED_BEHAVIOUR          "MODE"
/*=========================================================================*/

// Create the bluefruit object, either software serial...uncomment these lines

SoftwareSerial bluefruitSS = SoftwareSerial(BLUEFRUIT_SWUART_TXD_PIN, BLUEFRUIT_SWUART_RXD_PIN);

Adafruit_BluefruitLE_UART ble(bluefruitSS, BLUEFRUIT_UART_MODE_PIN,
                      BLUEFRUIT_UART_CTS_PIN, BLUEFRUIT_UART_RTS_PIN);

int check = 6;



void setup(void)
{
  delay(500);
  pinMode(check, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(check, HIGH); // checks low is actually high

  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  //Serial.begin(115200);
  //Serial.println(F("------------------------------------------------"));
  digitalWrite(LED_BUILTIN, HIGH);
  /* Initialise the module */
  //Serial.print(F("Initialising the Bluefruit LE module: "));

  if ( !ble.begin(VERBOSE_MODE) )
  {
    //error(F("Couldn't find Bluefruit, make sure it's in CoMmanD mode & check wiring?"));
  }
  //Serial.println( F("OK!") );
  digitalWrite(check, LOW);

  ble.echo(true);

  /*Serial.println(F("Waiting for connection..."));
  while (!ble.isConnected()) {
      delay(500);
  }*/
  ble.setMode(BLUEFRUIT_MODE_COMMAND);
  //
  ble.sendCommandCheckOK("AT+BLEUARTFIFO");
  delay(2000);
  digitalWrite(LED_BUILTIN, LOW);

  // May want to do one at a time
  //Serial.println("Setting up GATT services:");
  /* Print Bluefruit information */
  //ble.sendCommandCheckOK("AT+GATTLIST");
  //ble.sendCommandCheckOK("AT+GATTCLEAR");
  //ble.sendCommandCheckOK("AT+GATTADDSERVICE=UUID128=00-00-69-69-69-69-69-69-69-69-69-69-69-69-69-69");
  //ble.sendCommandCheckOK("AT+GATTADDCHAR=UUID=0x0420,PROPERTIES=0X02,MIN_LEN=2,MAX_LEN=4,VALUE=0,DATATYPE=1");
  //ble.sendCommandCheckOK("AT+GATTADDCHAR=UUID=0x0421,PROPERTIES=0X02,MIN_LEN=5,VALUE=0,DATATYPE=1");
  //ble.sendCommandCheckOK("AT+GATTADDCHAR=UUID=0x0422,PROPERTIES=0X02,MIN_LEN=6,VALUE=0,DATATYPE=1");
  //ble.sendCommandCheckOK("AT+GATTADDCHAR=UUID=0x0423,PROPERTIES=0X02,MIN_LEN=5,VALUE=0,DATATYPE=1");
  //ble.sendCommandCheckOK("AT+GATTADDCHAR=UUID=0x0424,PROPERTIES=0X02,MIN_LEN=6,VALUE=0,DATATYPE=1");
  //ble.sendCommandCheckOK("AT+GATTADDCHAR=UUID=0x0425,PROPERTIES=0X02,MIN_LEN=6,VALUE=0,DATATYPE=1");

  //ble.sendCommandCheckOK("AT+GATTLIST");
  
  digitalWrite(check, HIGH);
  
  
  //Serial.print(F("Done"));

}
// values to format sending rssi
char value_string[5] = {""};
int current = 0;
char c;
void loop(void)
{
  ble.println("AT+BLEUARTRX");
  while (ble.available() ) {
    c = ble.readline();
    value_string[current] = c;
    current++;
  }
  current = 0;
  ble.print("AT+BLUEARTTX=");
  ble.println(atoi(value_string));

}
