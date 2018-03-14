MODE_JUMP = 0
MODE_PTP = 2

EE_BIAS_X = 59.7
EE_BIAS_Y = 0.
EE_BIAS_Z = 0.

ON = 1
OFF = 0

dType.SetEndEffectorParamsEx(api, EE_BIAS_X, EE_BIAS_Y, EE_BIAS_Z, 1)


#JUMP
x, y, z = (206.7603, 145.3136, 13.8382)
dType.SetPTPCmdEx(api, MODE_JUMP, x, y, z, 0, 1)
dType.SetEndEffectorSuctionCupEx(api, 1, ON)

#P2P
x, y, z = (230.4929, 49.8467, 105.0460)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, MODE_PTP, x, y, z, current_pose[3], 1)
dType.SetEndEffectorSuctionCupEx(api, 1, OFF)
