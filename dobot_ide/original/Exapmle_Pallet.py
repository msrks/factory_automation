pallet = Pallet()
test = pallet.pallet()
#pallet data
for i in range(0, test.row):
	for j in range(0, test.col):
		pos = test.pos(i,j)
		print(pos.x, pos.y, pos.z)
		dType.SetPTPCmd(api, 0, pos.x, pos.y, pos.z, 0, isQueued=1)