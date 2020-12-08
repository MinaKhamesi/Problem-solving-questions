def diskStacking(disks):
	disks.sort(key = lambda x: x[2])
	maxHeights = [disk[2] for disk in disks]
	idxs = [None for disk in disks]
	maxHeight = disks[0][2]
	startingIdx = 0
	for i in range(1 , len(disks)):
		for j in range(i):
			if disks[i][0] > disks[j][0] and disks[i][1] > disks[j][1] and disks[i][2] > disks[j][2]:
				currentHeight = maxHeights[j] + disks[i][2]
				if currentHeight > maxHeights[i]:
					maxHeights[i] = currentHeight
					idxs[i] = j
		if maxHeights[i] > maxHeight:
			maxHeight = maxHeights[i]
			startingIdx = i
	return backTrackDisks(idxs, startingIdx, disks)

def backTrackDisks(idxs, startingIdx, disks):
	result = []
	currentIdx = startingIdx
	while currentIdx is not None:
		result.append(disks[currentIdx])
		currentIdx = idxs[currentIdx]
	return list(reversed(result))
	
