import subprocess

#ptpcam --show-property=0x5001

# Get Battery
proc = subprocess.Popen(["ptpcam", "--show-property=0x5001"], stdout=subprocess.PIPE)
(out, err) = proc.communicate()

# Parse result
battery = int(out[50:len(out) - 1])
print('Battery Level: ' + str(battery))


# Check video mode
proc = subprocess.Popen(["ptpcam", "--show-property=0x5013"],  stdout=subprocess.PIPE)
(out, err) = proc.communicate()

mode = int(out[57:len(out) - 10])

isVideoMode = mode==8002


print(isVideoMode)
