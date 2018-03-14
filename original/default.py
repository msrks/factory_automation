posX = dType.GetPoseEx(api, 1)
for i in range(1, 6):
    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, (200+i*20), 0, 0, current_pose[3], 1)
    dType.SetWAITCmdEx(api, 1, 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, posX,  0,  0, current_pose[3], 1)
for i in range(1, 6):
    dType.SetPTPCmdEx(api, 0, posX, 0, 0, 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
