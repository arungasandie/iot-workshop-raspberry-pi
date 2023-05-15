from machine import Pin #allows us to work with invidual pins of Pico
from time import sleep

led1 = Pin(14, Pin.OUT) #special assignment for LED on Pico #pin set up as output
led2 = Pin(15, Pin.OUT)
led1.value(0)
led2.value(1)

while True:
    #when value is 1 it turns on; when off it turns off
    led1.toggle()
    led2.toggle()
    sleep(1)
 