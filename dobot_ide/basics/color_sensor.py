ON = 1
OFF = 0

PORT_GP1 = 0
PORT_GP2 = 1
PORT_GP4 = 2
PORT_GP5 = 3

COLOR_RED = 0
COLOR_GREEN = 1
COLOR_BLUE = 2


dType.SetColorSensor(api, ON, PORT_GP5)

while True:
	print(dType.GetColorSensorEx(api, COLOR_RED))
	print()
