import os
os.system("sudo rfkill block wifi")
os.system("systemctl disable wpa_supplicant")

# uncomment last line int /boot/config.txt
# sudo systemctl disable dhcpcd.service

os.system("sudo shutdown -h now")

