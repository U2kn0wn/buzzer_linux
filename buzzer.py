#!/usr/bin/python3

import pyudev
import playsound


context = pyudev.Context()
x=0
for device in context.list_devices(subsystem='block', DEVTYPE='partition'):

     x+=1

while True:
    a=0
    for device in context.list_devices(subsystem='block', DEVTYPE='partition'):

         a+=1


    if x != a:
        playsound.playsound("sound.mp3")
        x=a
