/*
This script sends rssi and other possible sensor data through telemetry back to NASA
Must complete Interface Control Documents (ICDs)

RF experiminent data is sent through wallop's 16 parallel lines

Parallel read strobe line procedure:
1 uS: HIGH (Start of cycle)
5.333 uS: LOW (read data)
100.333 uS: LOW (Lag-time/refresh time)
1 uS: HIGH (Start of next cycle)
*/

#include <stdio.h>
#include <wiringPi.h>

#define DELAY_A		50
#define DELAY_B		75
#define DELAY_C		200
#define NUM_SENSORS 	1
#define NUM_BITS	4


const unsigned char sensor_pins[1] = {15};
const unsigned char strobe_pin = 16;
const unsigned char new_bit_pin = 17;
unsigned char vals[1] = {0x00};

void set(unsigned char *mask) {
  for(int sen = 0; sen < NUM_SENSORS; sen++) {
    if(vals[sen] & *mask) {
      digitalWrite(sensor_pins[sen], HIGH);
    } else {
      digitalWrite(sensor_pins[sen], LOW);
    }
  }
  *mask *= 2;
}


void write() {
  unsigned char mask = 0x01;

  // set lines with first bit
  set(&mask);
  delay(DELAY_C);

  for(int bit = 0; bit < NUM_BITS; bit++) {


void write_bit() {
    // tell NASA a bit is coming
    digitalWrite(strobe_pin, HIGH);
    delay(DELAY_A);
    digitalWrite(strobe_pin, LOW);

    delay(DELAY_B); // NASA reads bit

    // setting lines to next bit
    set(&mask);
    delay(DELAY_C);
}

void new_bit() {
  for (int sens = 0; sens < NUM_SENSORS; sens++) {


  }

}

int main (void) {

  // setup
  wiringPiSetup();
  for(int pin = 0; pin < NUM_SENSORS; pin++) {
    pinMode(sensor_pins[pin], OUTPUT);
    digitalWrite(sensor_pins[pin], LOW);
  }

  for(int num = 0; num < 16; num++) {
    vals[0] = num;
    write();
  }

  // shutdown
  for(int pin = 0; pin < 2; pin++) {
    digitalWrite(sensor_pins[pin], LOW);
  }
  return 0;
}
