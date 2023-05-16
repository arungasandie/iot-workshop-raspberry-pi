import network
import socket
from time import sleep
import machine
from umqtt.simple import MQTTClient
import random
import ahtx0
from machine import Pin, I2C

import wificonnect
#will only print after wificonnect works
print("Connected to Wifi.")

wlan = network.WLAN(network.STA_IF)
mqtt_server = 'io.adafruit.com'
mqtt_port = 1883 # non-SSL port
mqtt_user = 'arungasandie' #Adafruit ID
mqtt_password = 'aio_caWq92ETlBSemfFjQNBkQ2LrV4LI' # Under Keys
mqtt_topic = 'arungasandie/feeds/temperature' # Under "Feed info"
#adafruit needs different clients using their own unique names
mqtt_client_id = str(random.randint(10000,999999)) #must have a unique ID - good enough for now

i2c=I2C(1, scl=Pin(15), sda=Pin(14))
sensor=ahtx0.AHT10(i2c)

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
        temp=str(round(sensor.temperature,1))
        client.publish(mqtt_topic, temp)
        print("Sent temp is "+ temp)
    else:
        reconnect()
    sleep(20)#send after 20 seconds to reduce data being collected