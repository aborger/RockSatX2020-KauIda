#!/usr/bin/bash
# tested on WSL2 theta is in the same folder as this script
# in actual use, we expect people to run the bash script
# on a Raspberry Pi with ./theta and not ./theta

sleep 2s

# confirm settings
./theta getOptions

sleep 2s

# set exposureCompensation to -2.0
./theta exposureCompensation --value=-2.0

sleep 2s

# take picture and download to local computer
# it will be in the same directory as theta
./theta takeAndDownload

sleep 2s

# set exposureCompensation to -1.0
./theta exposureCompensation --value=-1.0

sleep 2s

# take picture and download to local computer
# it will be in the same directory as theta
./theta takeAndDownload

sleep 2s

# set exposureCompensation to 0.0
./theta exposureCompensation --value=0.0

sleep 2s

# take picture and download to local computer
# it will be in the same directory as theta
./theta takeAndDownload

sleep 2s

# set exposureCompensation to 1.0
./theta exposureCompensation --value=1.0

sleep 2s

# take picture and download to local computer
# it will be in the same directory as theta
./theta takeAndDownload

sleep 2s

# set exposureCompensatio to 2.0
./theta exposureCompensation --value=2.0

sleep 2s

# take picture and leave on camera
./theta takeAndDownload

