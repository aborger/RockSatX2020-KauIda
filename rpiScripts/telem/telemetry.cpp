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

#define DELAY_A		10 // Start of cyle time
#define DELAY_B		60 // Read Data time
#define DELAY_C		100 // Refresh time
#define NUM_BITS	8

using namespace std;

class Telem {

  public:
    Telem(int);
    void write(int, int, int, int, int); // Called by python script, paramater is an array containing hex data for each sensor from one reading
    void shutdown();
  private:
    int sensorPins[5] = {15, 16, 1, 4, 5}; // Pin number corellated to each sensor
    int prsPin = 6; // Pin for Parallel Read Strobe (tells nasa when a new bit is being sent)
    int NUM_SENSORS = 5; // Number of sensors
    unsigned char* vals; // Contains byte for each sensor that will be sent
    unsigned char mask; // A mask for which bit is being sent
    void set(); // writes a bit to nasa for each sensor
    void write_bit(void); // runs procedure to send a bit of data
};

// Constructor
Telem::Telem(int t) {
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


void Telem::write(int rssi, int temp, int hum, int pres, int alt) {
  vals[0] = (unsigned char) rssi;
  vals[1] = (unsigned char) temp;
  vals[2] = (unsigned char) hum;
  vals[3] = (unsigned char) pres;
  vals[4] = (unsigned char) alt;

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
  wiringPiSetup();
  pinMode(prsPin, OUTPUT);
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

// C wrapper to allow calling from python
extern "C" {
  Telem* Telem_new(int t) {return new Telem(t);}
  void Telem_write(Telem* telem, int rssi, int temp, int hum, int pres, int alt) {return telem->write(rssi, temp, hum, pres, alt);}
  void Telem_shutdown(Telem* telem) {return telem->shutdown();}
  void Telem_delete(Telem* telem) {
    if (telem) {
      delete telem;
      telem = nullptr;
    }
  }
}


int main (void) {
  Telem telem(1);

  telem.write(20, 1, 1, 1, 1);
  return 0;
}
