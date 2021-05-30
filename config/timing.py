"""

* Timing contains all the timing values

* Note: All timing units are in seconds

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""

class Timing:

    # Boom Timing
    EXTEND_TIME = 60 # 60		# Time it takes for the boom to completely extend or descend

    TIME_AT_EXTENSION = 10  #60	# Amount of time the boom stays fully extended

    BOOM_OVER_DRIVE = 5    # time boom keeps going after limit switch

    BOOM_POWER = 90	#90	# Percentage of power given to the motor


    RF_FREQUENCY = 1		# Rate at which rf data is taken (per second)

    RF_ACTIVATE_TIME =  2*EXTEND_TIME + TIME_AT_EXTENSION

    RF_CONNECT_DELAY = 10

    # ArduCam Timing
    RECORD_TIME = (15 + EXTEND_TIME * 2 + TIME_AT_EXTENSION) * 1000 #60 seconds, Not final


