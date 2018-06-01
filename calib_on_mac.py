"""
get arm position of picking object using verbose mode.

2018-06-01 msrks
"""
import time
from glob import glob
from pydobot import Dobot

available_ports = glob('/dev/cu*usb*')
device = Dobot(port=available_ports[0], verbose=True)
time.sleep(0.5)
device.close()
