'''
This script sends rssi and other possible sensor data through telemetry back to NASA
Must complete Interface Control Documents (ICDs)

RF experiminent data is sent through wallop's 16 parallel lines

Parallel read strobe line procedure:
1 uS: HIGH (Start of cycle)
5.333 uS: LOW (read data)
100.333 uS: LOW (Lag-time/refresh time)
1 uS: HIGH (Start of next cycle)
'''
