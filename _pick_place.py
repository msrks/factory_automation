import time
from glob import glob
import platform

from pydobot import Dobot

x,y,z = 27.1, 258.2, -4.8
a,b,c = 242, -10, 15

def load():
    if platform.system() == "Darwin" :
        available_ports = glob('/dev/cu*usb*')  # mask for OSX Dobot port
    else:
        pass

available_ports = glob('/dev/ttyUSB0')  # mask for Raspi Dobot port
if len(available_ports) == 0:
    print('no port found for Dobot Magician')
    exit(1)

device = Dobot(port=available_ports[0])
device.stop_conveyor_belt()
time.sleep(.5)

device.speed(50)
device.go(x,y,z+20)
device.speed(50)
device.go(x,y,z)
time.sleep(.5)

device.suck(True)
time.sleep(.5)

device.speed(30)
device.go(x,y,z+20)
device.speed(30)
device.go(a,b,c+20)
device.speed(30)
device.go(a,b,c-10)
time.sleep(.5)

device.suck(False)

device.move_conveyor_belt(.3, direction=1)
time.sleep(.1)
	
device.close()