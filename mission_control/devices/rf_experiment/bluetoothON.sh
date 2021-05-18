#!/usr/bin/expect -f
# must first install with $ sudo apt install expect
set prompt "#"

spawn sudo bluetoothctl
expect -re $prompt
send "power on\r"
sleep 1

expect -re $prompt
send "agent on\r"
sleep 1

expect -re $prompt
send "exit\r"
sleep 1

expect eof
