# This file contains the python wrapper for the Telem class made in c++
import ctypes

lib = ctypes.cdll.LoadLibrary('devices/rf_experiment/libtelem.so')


lib.write_sense.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int] # Telem_write parameter type of uint8[5] 5 corelates to number of sensors
lib.write_sense.restype = ctypes.c_void_p # Telem_write returns void



def write(sval):
	lib.write_sense(int(sval[0]), int(sval[1]), int(sval[2]), int(sval[3]), int(sval[4]))

