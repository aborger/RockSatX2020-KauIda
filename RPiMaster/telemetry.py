# This file contains the python wrapper for the Telem class made in c++
import ctypes

lib = ctypes.cdll.LoadLibrary('./RPiMaster/libtelem.so')

class Telem(object):
	def __init__(self):
		# note these comments are wrong af
		lib.Telem_new.argtypes = [ctypes.c_void_p] # Telem_new parameter types of (int[len(sensorPin)], int)
		lib.Telem_new.restype = ctypes.c_void_p # Telem_new returns void

		lib.Telem_write.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int] # Telem_write parameter type of uint8[5] 5 corelates to number of sensors
		lib.Telem_write.restype = ctypes.c_void_p # Telem_write returns void

		lib.Telem_shutdown.argtypes = [ctypes.c_void_p] # Telem_shutdown has no parameters
		lib.Telem_shutdown.restype = ctypes.c_void_p # Telem_shutdown returns void

		lib.Telem_delete.argtypes = [ctypes.c_void_p] # Telem_delete has no parameters
		lib.Telem_delete.restype = ctypes.c_void_p # Telem_delete returns vo
		self.obj = lib.Telem_new(1)

	def write(self, sval):
		lib.Telem_write(int(sval[0]), int(sval[1]), int(sval[2]), int(sval[3]), int(sval[4]))

	def shutdown(self):
		lib.Telem_shutdown()
