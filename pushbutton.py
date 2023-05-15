from machine import Pin #allows us to work with invidual pins of Pico
from time import sleep

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN) #set default at 0V
#£led.value(0)

while True:
    if button.value():
        led.toggle()
        sleep(1)
        
      