#!/usr/bin/bash
# example settings for development

# we don't want camera to turn off during development
# disable offDelay
./theta offDelay --off
echo auto power off disabled

# disable sleepDelay
./theta sleepDelay --off
echo auto sleep disabled

# turn on shutter to make sure picture was taken
./theta shutterVolume --medium
echo shutter volume set to medium

# turn off hdr as it will be 2 seconds faster to take each picture
./theta hdr --no-enable
echo hdr and all filters turned off

# set mode to image
./theta setModeImage
echo set to still image mode

# show battery level
./theta state --battery

# show firmware
./theta info --firmware
