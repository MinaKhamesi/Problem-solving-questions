def zigzagTraverse(array):
    result = []
	row, col = 0, 0
	goingDown = True
	while row < len(array) and col < len(array[0]):
		result.append(array[row][col])
		
		if goingDown:
			if row == len(array) - 1:
				col += 1
				goingDown = False
			elif col == 0:
				row += 1
				goingDown = False
			
			else:
				row += 1
				col -= 1
		else:
			if col == len(array[0]) - 1:
				row += 1
				goingDown = True
			elif row == 0:
				col += 1
				goingDown = True
			
			else:
				row -= 1
				col += 1
	return result
	