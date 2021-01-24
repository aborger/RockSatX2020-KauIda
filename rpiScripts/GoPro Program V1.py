from gpiozero import LED
from time import sleep
led = LED(13)
led2 = LED(26)
led3 = LED(20)

while True:
    led3.on()
    print('on')
    sleep (1)
    led3.off()
    print('off')
    sleep (1)
    
