"""
Factory Automation Demo

2018-03-14 msrks
"""
STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
MM_PER_CRICLE = 3.1415926535898 * 36.0
vel = float(50) * STEP_PER_CRICLE / MM_PER_CRICLE

PORT_GP1 = 0
PORT_GP2 = 1
PORT_GP4 = 2
PORT_GP5 = 3

COLOR_RED = 0
COLOR_GREEN = 1
COLOR_BLUE = 2

MODE_JUMP = 0
MODE_PTP = 2

EE_BIAS_X = 59.7
EE_BIAS_Y = 0.
EE_BIAS_Z = 0.

ON = 1
OFF = 0


# configure settings
dType.SetEMotorEx(api, 0, 1, int(vel), 1)
dType.SetWAITCmd(api, 3000, 1)
dType.SetInfraredSensor(api, 1, 1)
dType.SetColorSensor(api, ON, PORT_GP5)
dType.SetEndEffectorParamsEx(api, EE_BIAS_X, EE_BIAS_Y, EE_BIAS_Z, 1)

while True:
    is_exist = dType.GetInfraredSensor(api, 1)[0]
    print(is_exist)
    if is_exist:
        # 1. stop belt-conveyer
        dType.SetEMotorEx(api, 0, 1, 0, 1)

        # 2. move to conveyered object and suck
        x, y, z = (212.6265, 189.3846, 15.6877)
        dType.SetPTPCmdEx(api, MODE_JUMP, x, y, z, 0, 1)
        dType.SetEndEffectorSuctionCupEx(api, 1, ON)

        # 3. move to garbage box and discard
        x, y, z = (3.6929, 275.6171, 25.)
        dType.SetPTPCmdEx(api, MODE_JUMP, x, y, z, 0, 1)
        dType.SetEndEffectorSuctionCupEx(api, 1, OFF)

        # 4. restart belt-conveyer
        dType.SetEMotorEx(api, 0, 1, int(vel), 1)

        #is_red = dType.GetColorSensorEx(api, COLOR_RED)

        dType.SetWAITCmd(api, 30, isQueued=0)
