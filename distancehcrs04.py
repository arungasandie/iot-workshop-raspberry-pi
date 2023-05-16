# This requires the hcrs04 MicroPython library to be installed:
from hcsr04 import HCSR04
from machine import Pin
from time import sleep
import network
import socket
from time import sleep
import machine
from umqtt.simple import MQTTClient
import random

import wificonnect
#will only print after wificonnect works
print("Connected to Wifi.")

wlan = network.WLAN(network.STA_IF)
mqtt_server = 'io.adafruit.com'
mqtt_port = 1883 # non-SSL port
mqtt_user = 'arungasandie' #Adafruit ID
mqtt_password = 'aio_uoTJ24nKus6o1klH7hxkbBv2igcd' # Under Keys
mqtt_topic = 'arungasandie/feeds/position' # Under "Feed info"
#adafruit needs different clients using their own unique names
mqtt_client_id = str(random.randint(10000,999999)) #must have a unique ID - good enough for now

# Assuming the sensor's trigger is on GPIO15 and echo is on GPIO14:
sensor2 = HCSR04(trigger_pin=15, echo_pin=14)
led1 = Pin(10, Pin.OUT) #special assignment for LED on Pico #pin set up as output
led2 = Pin(11, Pin.OUT)
led1.value(0)
led2.value(0)

def mqtt_connect():
    client = MQTTClient(client_id=mqtt_client_id, server=mqtt_server, port=mqtt_port, user=mqtt_user, password=mqtt_password, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    reset()
try:
     client = mqtt_connect()
except OSError as e:
    reconnect()
    
while True:
    if wlan.isconnected():
        dist = sensor2.distance_cm()
        client.publish(mqtt_topic, str(dist))
        # print('Distance:', distance, 'cm')
        if dist < 20:
            print("Parking not available")
            led1.value(1)
            led2.value(0)
        else:
            print("Parking available")
            led2.value(1)
            led1.value(0)
        
        print("Sent distance is "+ str(dist))
    else:
        reconnect()
    sleep(10)#send after 20 seconds to reduce data being collected
  
