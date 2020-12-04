def searchInSortedMatrix(matrix, target):
    row = 0
	col = len(matrix[0]) - 1
	while col >= 0 and row < len(matrix):
		if matrix[row][col] < target :
			row += 1
		elif matrix[row][col] > target :
			col -= 1
		else:
			return [row, col]	
	return [-1,-1]