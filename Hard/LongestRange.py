def largestRange(array):
    longestRange = [float('inf'),float('-inf')]
	numTable = {}
	for num in array:
		numTable[num] = False
	for num in array:
		if numTable[num] : continue
		startNum = num
		while startNum  in numTable:
			numTable[startNum ] = True
			startNum -= 1
			
		endNum = num
		while endNum  in numTable:
			numTable[endNum] = True
			endNum += 1
			
		longestRange = max(longestRange, [startNum+1, endNum-1], key=lambda x:x[1] - x[0])
	return longestRange
		