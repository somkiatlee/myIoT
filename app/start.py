from machine import Pin
from time import sleep

print('Version 2 installed using USB V2')

led = Pin(2, Pin.OUT)

while True:
    led.value(1)
    sleep(0.4)
    led.value(0)
    sleep(0.4)
    led.value(1)
    sleep(0.4)
    led.value(0)
    sleep(0.4)
    led.value(1)
    sleep(2)