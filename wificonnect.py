import network
import socket
from time import sleep
import machine

ssid = 'GEARBOX MEMBERS'
password = 'Members@Gearbox'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True) #set wifi chip to active
    wlan.connect(ssid, password)
    while wlan.isconnected() == False: #incase wifi isn't connected
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    
#try the connect function else 
try:
    connect()
except KeyboardInterrupt:
    machine.reset()