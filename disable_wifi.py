import os
os.system("sudo rfkill block wifi")
os.system("systemctl disable wpa_supplicant")
os.system("sudo shutdown -h now")
