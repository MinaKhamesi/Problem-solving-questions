def numbersInPi(pi, numbers):
    numTable = {number:True for number in numbers}
	minSpaces = getMinSpaces(pi, numTable, {}, 0)
	return minSpaces if minSpaces != float('inf') else -1

def getMinSpaces(pi, numTable, cache, idx):
	if idx == len(pi): return -1
	if idx in cache : return cache[idx]
	minSpaces = float('inf')
	for i in range(idx, len(pi)):
		prefix = pi[idx : i+1]
		if prefix in numTable:
			minSpacesInSuffix = getMinSpaces(pi, numTable, cache, i + 1)
			minSpaces = min(minSpaces, minSpacesInSuffix + 1)
	cache[idx] = minSpaces
	return minSpaces