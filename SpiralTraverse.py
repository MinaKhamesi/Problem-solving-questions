def spiral_traverse(array):
    firstRow, lastRow = 0, len(array)-1
    firstCol, lastCol = 0, len(array[0])-1

    traversed = []

    while firstRow<lastRow and firstCol<lastCol:
        for col in range(firstCol,lastCol+1):
            traversed.append(array[firstRow][col])
        for row in range(firstRow+1, lastRow+1):
            traversed.append(array[row][lastCol])
        for col in reversed(range(firstCol,lastCol)):
            traversed.append(array[lastRow][col])
        for row in reversed(range(firstRow+1,lastRow)):
            traversed.append(array[row][firstCol])

        firstRow+= 1
        firstCol += 1
        lastRow -= 1
        lastCol -= 1

    if firstRow == lastRow:
        for col in range(firstCol,lastCol+1):
            traversed.append(array[firstRow][col])
    if firstCol == lastCol :
        for row in range(firstRow,lastRow+1):
            traversed.append(array[row][firstCol])

    return traversed