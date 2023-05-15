from machine import Pin #allows us to work with invidual pins of Pico
from time import sleep

led = Pin("LED", Pin.OUT) #special assignment for LED on Pico #pin set up as output
led.value(0)

#defining a function for the led to blink for 3 counts
def blinkthree():
    i=0;
    while i<3:
        led.toggle()
        sleep(.3)
        print("doing it again"+str(i))
        i=i+1

while True:
    blinkthree()
   
    #when value is 1 it turns on; when off it turns off
    #led.on()
    #sleep(1)
    #led.off()
    #sleep(1)
 