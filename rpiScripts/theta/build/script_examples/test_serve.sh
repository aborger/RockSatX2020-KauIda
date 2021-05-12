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
echo testing file access
theta download --files=last
echo starting python server on port 8000
echo CTRL-C will stop server

python3 -m http.server
