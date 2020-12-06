def minRewards(scores):
    minRewards = [1 for students in scores]
	for i in range(len(scores)-1):
		if scores[i+1]>scores[i]:
			minRewards[i+1] = minRewards[i] + 1
	for j in reversed(range(len(scores)-1)):
		if scores[j] > scores[j+1]:
			minRewards[j] = max(minRewards[j],minRewards[j+1] + 1)
	return sum(minRewards)





def minRewards(scores):
	if len(scores) == 1 : return 1
	minRewards = [1 for student in scores]
	weakestStudentsIndices = findWeakestStudentsIndices(scores)
	
	for i in weakestStudentsIndices:
		expandFromIdx(i, scores, minRewards)
		
	return sum(minRewards)

def findWeakestStudentsIndices(scores):
	weakestStudentsIndices = []
	for i in range(len(scores)):
		if i == 0 and scores[0] < scores[1]:
			weakestStudentsIndices.append(0)
		elif i== len(scores) - 1 and scores[i] < scores[i - 1]:
			weakestStudentsIndices.append(i)
		elif i != 0 and i!= len(scores) - 1:
			if scores[i] < scores[i -1 ] and scores[i] < scores[i+1]:
				weakestStudentsIndices.append(i)
	return weakestStudentsIndices

def expandFromIdx(i, scores, minRewards):
	leftIdx = i - 1
	while leftIdx >=0 and scores[leftIdx] > scores[leftIdx + 1]:
		minRewards[leftIdx] = max(minRewards[leftIdx + 1] + 1 , minRewards[leftIdx])
		leftIdx -= 1
	rightIdx = i + 1
	while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
		minRewards[rightIdx] = minRewards[rightIdx - 1] + 1
		rightIdx += 1
	
