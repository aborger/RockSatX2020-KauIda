#pragma once


extern "C" {
  void write_sense(int rssi, int temp, int hum, int pres, int alt);
}
