EE_BIAS_X = 59.7
EE_BIAS_Y = 0.
EE_BIAS_Z = 0.

ON = 1
OFF = 0

dType.SetEndEffectorParamsEx(api, EE_BIAS_X, EE_BIAS_Y, EE_BIAS_Z, 1)
dType.SetEndEffectorSuctionCupEx(api, 1, ON)
# dType.SetEndEffectorSuctionCupEx(api, 1, OFF)
