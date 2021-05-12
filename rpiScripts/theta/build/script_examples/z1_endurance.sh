#!/usr/bin/bash
# tested on WSL2 theta is in the same folder as this script
# endurance test for Z1 with firmware 1.60.1
# prior to test
# * pictures deleted with ./theta deleteAll
# * camera settings were reset with ./theta reset 
# IMPORTANT: The two commands above will delete all your media and settings


# disable offDelay
./theta offDelay --off

# disable sleepDelay
./theta sleepDelay --off

# you may want to have commands in here to delete existing pictures
# and free up camera space. It's not here in the example for safety

# turn off self timer
./theta exposureDelay --seconds=0

# turn off shutter volume "beep"
./theta shutterVolume --low

# confirm settings
./theta getOptions

# set exposureCompensation to -2.0
./theta exposureCompensation --value=-2.0

# take test picture and download to local computer
# it will be in the same directory as theta
./theta takeAndDownload

# set exposureCompensatio to 2.0
./theta exposureCompensation --value=2.0

# take picture and download second test image
./theta takeAndDownload

# set exposureCompensatio to 0
./theta exposureCompensation --value=0.0

# take picture and download second test image
./theta takeAndDownload

# from this point onward, the images are left on camera
# you will need to download the images for inspection

echo start endurance loop test
# example of loop to take  pictures for timelapse or testing
# increase the number below to 300 to take 300 pictures
# example {1..300}
for counter in {1..500}
do
    ./theta takeAndReady
    echo that was picture $counter
    ((counter++))
    # waiting 1 second just in case camera is overheading
    echo waiting 1 seconds for the next shot
    sleep 1s

done
echo finished endurance test

# grab all the thumbnails and write to local storage
./theta download --thumb=all
echo thumbnail download test completed
echo thumbnails are in local storage for inspection
