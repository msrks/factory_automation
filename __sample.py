import time
from glob import glob
import platform

from pydobot import Dobot

def load():
    if platform.system() == "Darwin" :
        available_ports = glob('/dev/cu*usb*')  # mask for OSX Dobot port
    else:
        pass

available_ports = glob('/dev/cu*usb*')  # mask for Raspi Dobot port

if len(available_ports) == 0:
    print('no port found for Dobot Magician')
    exit(1)

device = Dobot(port=available_ports[0])

time.sleep(0.5)

device.set_infrared_sensor()
device.set_color_sensor()
# device.get_io()

time.sleep(1)

# device.move_conveyor_belt(1, direction=1)

# device.speed(50)
# device.go(250.0, 0.0, 25.0)
# device.speed(50)
# device.go(250.0, 0.0, 0.0)

# time.sleep(2)

# device.stop_conveyor_belt()
# time.sleep(2)

for i in range(5):
    ret = device.get_color_sensor()
    print(ret)
    ret = device.get_infrared_sensor()
    print(ret)

device.close()
