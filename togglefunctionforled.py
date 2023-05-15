from machine import Pin #allows us to work with invidual pins of Pico
from time import sleep

led = Pin("LED", Pin.OUT) #special assignment for LED on Pico #pin set up as output
led.value(0)

while True:
    #when value is 1 it turns on; when off it turns off
    led.toggle()
    sleep(1)