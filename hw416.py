from machine import Pin #allows us to work with invidual pins of Pico
from time import sleep

pir = Pin(15, Pin.IN, Pin.PULL_DOWN)
#give the sensor time to settle
sleep(1)
print("Ready!")

while True:
    if pir.value():
        print("Motion detected!")
        sleep(1)