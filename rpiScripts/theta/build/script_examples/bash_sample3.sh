#!/usr/bin/bash
# Built to test @pixel's timing of 7 bracketed images and how long
# it takes to complete a command before moving on to a next one

# set exposureProgram to 1
./theta exposureProgram --value=1

# set ISO, Aperature and Color Temperature one time
./theta setOption --name=iso --value=100

./theta setOption --name=aperture --value=2.1

./theta setOption --name=_colorTemperature --value=2500

# set shutter speed
./theta setShutter --speed=0.625

# take a picture
./theta takeAndReady

# set shutter speed
./theta setShutter --speed=0.16666666

# take a picture
./theta takeAndReady

# set shutter speed
./theta setShutter --speed=0.04

# take a picture
./theta takeAndReady

# set shutter speed
./theta setShutter --speed=0.01

# take a picture
./theta takeAndReady

# set shutter speed
./theta setShutter --speed=0.0025

# take a picture
./theta takeAndReady

# set shutter speed
./theta setShutter --speed=0.000625

# take a picture
./theta takeAndReady

# set shutter speed
./theta setShutter --speed=0.00015625

# take a picture
./theta takeAndReady
