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
#include <iostream>

#define DELAY_A		50 // Start of cyle time
#define DELAY_B		75 // Read Data time
#define DELAY_C		200 // Refresh time
#define NUM_BITS	8

using namespace std;

class Telem {

  public:
    Telem(int[], int);
    void write(unsigned char*); // Called by python script, paramater is an array containing hex data for each sensor from one reading
    void shutdown();
  private:
    int* sensorPins; // Pin number corellated to each sensor
    int prsPin = 10; // Pin for Parallel Read Strobe (tells nasa when a new bit is being sent)
    int NUM_SENSORS; // Number of sensors
    unsigned char* vals; // Contains byte for each sensor that will be sent
    unsigned char mask; // A mask for which bit is being sent
    void set(); // writes a bit to nasa for each sensor
    void write_bit(void); // runs procedure to send a bit of data
};

// Constructor
Telem::Telem(int sensorPins[], int prsPin) {
  this->sensorPins = sensorPins;
  this->prsPin = prsPin;
  this->NUM_SENSORS = sizeof(sensorPins)/sizeof(sensorPins[0]);
  this->vals = new unsigned char[NUM_SENSORS];
  this->mask = 0x0001;

  wiringPiSetup(); // sets up wiringPi library
  // set each pin to output and make sure its turned off
  pinMode(prsPin, OUTPUT);
  for(int pin = 0; pin < NUM_SENSORS; pin++) {
    pinMode(sensorPins[pin], OUTPUT);
    digitalWrite(sensorPins[pin], LOW);
  }
}


void Telem::set() {
  // sets bit for each sensor
  for(int sen = 0; sen < NUM_SENSORS; sen++) {
    // if bit currently being sent is high
    //cout << (int)vals[sen] << " " << (int)mask << " " << (vals[sen] & mask) << endl; //debug
    if(vals[sen] & mask) {
      digitalWrite(sensorPins[sen], HIGH); // sets that sensor pin high
    } else {
      digitalWrite(sensorPins[sen], LOW); // sets that sensor pin low
    }
  }
  mask *= 2;
}


void Telem::write(unsigned char* new_vals) {
  vals = new_vals;
  mask = 0x0001;
  // set lines with first bit
  set();
  delay(DELAY_C);


  for(int bit = 0; bit < NUM_BITS; bit++) {
    write_bit();

  }
}

void Telem::write_bit() {
  // tell NASA a bit is coming
  digitalWrite(prsPin, HIGH);
  delay(DELAY_A);
  digitalWrite(prsPin, LOW);
  delay(DELAY_B); // NASA reads bit

  // setting lines to next bit
  set();
  delay(DELAY_C);
}

void Telem::shutdown() {
  for(int pin = 0; pin < NUM_SENSORS; pin++) {
    digitalWrite(sensorPins[pin], LOW);
  }
}
int main (void) {
  int sensor_pins[1] = {15};
  int prs = 6;
  Telem telem(sensor_pins, prs);

  unsigned char *val;
  val = new unsigned char[1];
  for (int i = 0; i < 255; i++) {
    //unsigned char i = 0xC8;
    //cout << "Val = " << i << endl;
    val[0] = i;
    telem.write(val);
  }
  return 0;
}
