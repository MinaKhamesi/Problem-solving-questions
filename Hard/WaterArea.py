def waterArea(heights):
	if len(heights) < 2 : return 0
	maxFromLeft = [height for height in heights]
	maxFromRight = [height for height in heights]
	for i in range(1,len(heights)):
		maxFromLeft[i] = max(maxFromLeft[ i - 1], heights[i])
	for i in reversed(range(len(heights) - 1)):
		maxFromRight[i] = max(maxFromRight[i + 1], heights[i])
	heightOfWater = [min(maxFromLeft[i], maxFromRight[i]) for i in range(len(heights))]
	waterTrapped = [heightOfWater[i] - heights[i] for i in range(len(heights))]	
	return sum(waterTrapped)  