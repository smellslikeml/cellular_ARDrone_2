#!/usr/bin/env python
import sys
import time
import ardrone
from Hologram.HologramCloud imoprt HologramCloud
from config import DEVICEKEY

print('Connecting to Cellular Network')
creds = {'devicekey': DEVICEKEY}
hologram = HologramCloud(creds, network='cellular',
                         authentication_type='csrpsk')
hologram.openReceiveSocket()

def popReceiveMessage():
    recv = hologram.popReceiveMessage()
    if recv:
        return str(recv)

def handle_polling(drone, fx, delay_interval=0):
    while True:
        res = fx()
        if res == 'land':
            drone.land()
            time.sleep(2)
            drone.halt()
            time.sleep(2)
            hologram.closeReceiveSocket()
            break
        time.sleep(delay_interval)

drone = ardrone.ARDrone()
time.sleep(2)
drone.reset()
time.sleep(2)
print('Drone Ready')
drone.takeoff()
print('Drone Taking Off')
time.sleep(2)
drone.hover()
print('Drone Flight Program')
time.sleep(2)
popReceivedMessage(drone)
