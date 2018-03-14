import math

dType.SetJOGJointParams(api, 150, 150, 150, 150, 150, 150, 150, 150)

while(True):
    dType.SetJOGCmd(api, 1, 1, 1)
    dType.SetWAITCmd(api, 0.5, 1)
    dType.SetJOGCmd(api, 1, 0, 1)
    dType.SetWAITCmd(api, 0.2, 1)

    dType.SetJOGCmd(api, 1, 2, 1)
    dType.SetWAITCmd(api, 0.5, 1)
    dType.SetJOGCmd(api, 1, 0, 1)
    dType.SetWAITCmd(api, 0.2, 1)
