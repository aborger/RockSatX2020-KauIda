"""

* Timing contains all the timing values

* Note: All timing units are in seconds

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""

class Timing:

    # Boom Timing
    EXTEND_TIME = 5 # 60		# Time it takes for the boom to completely extend or descend

    EXTEND_PERIOD = 1		# Rate at which RF data is taken

    TIME_AT_EXTENSION = 10 #60	# Amount of time the boom stays fully extended

    BOOM_POWER = 50		# Percentage of power given to the motor


    # ArduCam Timing
    RECORD_TIME = 60	# Not final
