"""

* Timing contains all the timing values

* Note: All timing units are in seconds

* Author: Aaron Borger <aborger@nnu.edu (307)534-6265>

"""

class Timing:

    # Boom Timing
    EXTEND_TIME = 45 # 60		# Time it takes for the boom to completely extend or descend

    TIME_AT_EXTENSION = 25	# Amount of time the boom stays fully extended

    BOOM_OVER_DRIVE = 1    # time boom keeps going after limit switch

    BOOM_POWER = 100	#90	# Percentage of power given to the motor

    BOOM_DELAY = 5

    RF_FREQUENCY = 2		# Rate at which rf data is taken (per second)

    RF_ACTIVATE_TIME =  2*(EXTEND_TIME + TIME_AT_EXTENSION) - 5

    RF_CONNECT_DELAY = 8


    ARDU_RECORD_TIME = 362 * 1000  # TE recording: 2000*(EXTEND_TIME + 2*TIME_AT_EXTENSION) + 7000




    DOWNLOAD_TIMEOUT = 30
