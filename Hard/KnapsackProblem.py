def knapsackProblem(items, capacity):
    maxValTable = [[0 for c in range(capacity + 1)] for i in range(len(items) + 1)]
	for i in range(1 , len(items) + 1):
		[currentVal, currentWeight] = items[i - 1]
		for c in range(capacity + 1):
			if c >= currentWeight :
				
				maxValWithoutUsingItem = maxValTable[i - 1][c]
				maxValWithItem = currentVal + maxValTable[ i - 1][c - currentWeight]
				
				maxValTable[i][c] = max(maxValWithoutUsingItem, maxValWithItem)
		    else:
				maxValTable[i][c] = maxValTable[i - 1][c]
				
	return [maxValTable[-1][-1], computeIdxs(maxValTable, items)]
			
def computeIdxs(table, items):
	idxs = []
	row = len(table) - 1
	col = len(table[0]) - 1
	while table[row][col] != 0:
		if table[row][col] != table[row - 1][col]:
			idxs.append(row-1)
			row -= 1
			col -= items[row][1]
		else:
			row -= 1
	return list(reversed(idxs))
				
