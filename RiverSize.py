## solution1 .DFS
def riverSizes(matrix):
    visited = [[False for _ in matrix[0]] for _ in matrix]
    sizes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    currentSize = calculateSize(row,col,matrix,visited)
                    sizes.append(currentSize)
                visited[row][col] = True
    return sizes

def calculateSize(row, col, matrix, visited):
    outOfBound = row<0 or row>=len(matrix) or col<0 or col>=len(matrix[0])
    if outOfBound or visited[row][col]: return 0
    visited[row][col] = True
    if matrix[row][col] == 0: return 0
    upSize = calculateSize(row - 1, col, matrix, visited)
    bottomSize = calculateSize(row + 1, col, matrix, visited)
    leftSize = calculateSize(row , col - 1 , matrix, visited)
    rightSize = calculateSize(row , col + 1 , matrix, visited)
    return 1 + upSize + bottomSize + leftSize + rightSize


##solution2 BFS
def riverSizes2(matrix):
    visited = [[False for _ in matrix[0]] for _ in matrix]
    sizes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if visited[row][col]: continue
            visited[row][col] = True
            traverse(matrix, row, col, visited, sizes)
    return sizes


def traverse(matrix, row, col, visited, sizes):
    queue = [[row,col]]
    size = 0
    while len(queue):
        currentRow, currentCol = queue.pop(0)
        if matrix[currentRow][currentCol] == 0:
            visited[currentRow][currentCol] = True
        else:
            size += 1
            neighbors = findNeighbors(matrix, currentRow, currentCol, visited)
            for [Row,Col] in neighbors:
                queue.append([Row, Col])
                visited[Row][Col] = True
    if size>0:
        sizes.append(size)

def findNeighbors(matrix, row, col, visited):
    neighbors = []
    for Row,Col in [[row + 1, col], [row - 1, col ], [ row, col -1 ], [row, col + 1]]:
        if  Row>=0 and Row<len(matrix) and Col>=0 and Col<len(matrix[0]) and not visited[Row][Col]:
            neighbors.append([Row, Col])
    return neighbors