MODE_JUMP = 0
MODE_PTP = 2

#JUMP
x, y, z = (206.7603, 145.3136, 13.8382)
dType.SetPTPCmdEx(api, MODE_JUMP, x, y, z, 0, 1)

#P2P
x, y, z = (230.4929, 49.8467, 105.0460)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, MODE_PTP, x, y, z, current_pose[3], 1)
