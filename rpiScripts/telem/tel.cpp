#include "tel.h"
#include <stdio.h>
#include <wiringPi.h>
#include <iostream>
#include <unistd.h>

#define DELAY_A		1 // Start of cyle time
#define DELAY_B		5 // Read Data time
#define DELAY_C		100 // Refresh time
#define NUM_BITS	8



using namespace std;

int sensorPins[5] = {3, 4, 15, 17, 18};
int prsPin = 2;
int NUM_SENSORS = 5;
unsigned char mask;
unsigned char vals[5];

void set() {
  // sets bit for each sensor
  wiringPiSetup();
  for(int sen = 0; sen < NUM_SENSORS; sen++) {

    // if bit currently being sent is high
    //cout << (int)vals[sen] << " " << (int)mask << " " << (vals[sen] & mask) << endl; //debug
    pinMode(sensorPins[sen], OUTPUT);
    if(vals[sen] & mask) {
      digitalWrite(sensorPins[sen], HIGH); // sets that sensor pin high
    } else {
      digitalWrite(sensorPins[sen], LOW); // sets that sensor pin low
    }
  }
  mask *= 2;
}


void write_bit() {
  // tell NASA a bit is coming
  wiringPiSetup();
  pinMode(prsPin, OUTPUT);
  digitalWrite(prsPin, HIGH);
  usleep(DELAY_A);
  digitalWrite(prsPin, LOW);
  usleep(DELAY_B); // NASA reads bit

  // setting lines to next bit
  set();
  usleep(DELAY_C);
}



void write_sense(int rssi, int temp, int hum, int pres, int alt) {
  vals[0] = (unsigned char) rssi;
  vals[1] = (unsigned char) temp;
  vals[2] = (unsigned char) hum;
  vals[3] = (unsigned char) pres;
  vals[4] = (unsigned char) alt;

  mask = 0x0001;
  // set lines with first bit
  set();
  usleep(DELAY_C);

  for(int bit = 0; bit < NUM_BITS; bit++) {
    write_bit();
  }
}


