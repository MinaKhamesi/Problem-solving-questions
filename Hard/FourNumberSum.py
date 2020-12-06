def fourNumberSum(array, targetSum):
	result = []
	sumsTable = {}
	for i in range(len(array)):
		for j in range(i + 1, len(array)):
			currentSum = array[i] + array[j]
			neededSum = targetSum - currentSum
			if neededSum in sumsTable:
				for num1,num2 in sumsTable[neededSum]:
					result.append([num1, num2, array[i], array[j]])
			
		for k in range(i):
			currentSum = array[i] + array[k]
			if currentSum not in sumsTable:
				sumsTable[currentSum] = []
			sumsTable[currentSum].append([array[i], array[k]])
	return result