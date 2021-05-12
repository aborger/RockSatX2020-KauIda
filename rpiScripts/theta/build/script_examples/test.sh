#!/usr/bin/bash

echo test completed on
date

echo Tested on
echo $OSTYPE



export PATH=.:$PATH

echo version of this app
theta app --version
echo ---
echo firmware version
theta info --firmware
echo camera mode
theta info --model
echo testing takePicture with check to make sure camera is ready for next command
theta takeAndReady
echo testing take and save to local storage
theta takeAndDownload
echo image download complete
echo testing thumbnail
theta download --thumb=last
echo basic test complete
