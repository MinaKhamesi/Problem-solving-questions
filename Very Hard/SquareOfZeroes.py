def squareOfZeros(matrix):
    infoMatrix = getZeroCounts(matrix)
    n = len(matrix)
    for topRow in range(n):
        for leftCol in range(n):
            length = 2
            while leftCol + length <= n and topRow + length <= n:
                bottomRow = topRow + length - 1
                rightCol = leftCol + length - 1
                if isSquareOfZeros(topRow , bottomRow , leftCol , rightCol , infoMatrix):
                    return True
                length += 1
    return False

def isSquareOfZeros(r1, r2 , c1 , c2 , info):
    length = c2 - c1 + 1 
    hasTopBorder = info[r1][c1]['numZerosRight'] >= length
    hasBottomBorder = info[r2][c1]['numZerosRight'] >= length
    hasLeftBorder = info[r1][c1]['numZerosBelow'] >= length
    hasRightBorder = info[r1][c2]['numZerosBelow'] >= length
    return hasTopBorder and hasBottomBorder and hasLeftBorder and hasRightBorder

def getZeroCounts(matrix):
    info = [[x for x in row] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            numZero = 1 if matrix[row][col] == 0 else 0
            info[row][col] = {'numZerosRight' : numZero , 'numZerosBelow' : numZero}
    lastIdx = len(matrix) - 1
    for row in reversed(range(len(matrix))):
        for col in reversed(range(len(matrix[0]))):
            if matrix[row][col] == 1: continue
            if row < lastIdx:
                info[row][col]['numZerosBelow'] += info[row+1][col]['numZerosBelow']
            if col < lastIdx:
                info[row][col]['numZerosRight'] += info[row][col + 1]['numZerosRight']
    return info

    ###########SOLUTION 2
def squareOfZeros2(matrix):
    n = len(matrix)
    for topRow in range(n):
        for leftCol in range(n):
            length = 2
            while topRow + length <= n and leftCol + length <= n:
                bottomRow = topRow + length - 1
                rightCol = leftCol + length - 1
                if isSquareOfZeros2(topRow , bottomRow, leftCol , rightCol , matrix):
                    return True
                length += 1
    return False
def isSquareOfZeros2(r1, r2 , c1 , c2 , matrix):
    for row in range(r1 , r2 + 1):
        if matrix[row][c1] != 0 or matrix[row][c2] != 0:
            return False
    for col in range(c1 , c2 + 1):
        if matrix[r1][col] != 0 or matrix[r2][col] != 0 :
            return False
    return True
############SOLUTION 3
def squareOfZeros3(matrix):
    lastIdx = len(matrix) - 1
    return containSquareOfZeros(matrix , 0 , 0 ,lastIdx , lastIdx , {})

def containSquareOfZeros(matrix , r1 , c1, r2 , c2, cache):
    if r1 >= r2 or c1 >= c2:
        return False
    key = coordToString(r1,c1,r2,c2)
    if key in cache :
        return cache[key]
    cache[key] = (
        isSquareOfZeros2(r1,r2,c1,c2 , matrix)
        or containSquareOfZeros(matrix , r1 + 1 ,c1,r2,c2 - 1, cache)
        or containSquareOfZeros(matrix , r1 + 1 , c1 + 1 , r2, c2, cache)
        or containSquareOfZeros(matrix , r1 , c1 + 1, r2 - 1, c2,cache)
        or containSquareOfZeros(matrix , r1 , c1 , r2 + 1, c2 - 1 , cache)
        or containSquareOfZeros(matrix , r1 + 1 , c1 + 1, r2 - 1 , c2 - 1 , cache)
    )
    return cache[key]

def coordToString(r1,c1 , r2 , c2):
    return str(r1) + '-' + str(c1) + '-' + str(r2) + '-' + str(c1)

######## SOLUTION 4
def squareOfZeros4(matrix):
    lastIdx = len(matrix) - 1
    info = getZeroCounts(matrix)
    return containSquareOfZeros2(info , 0 , 0 , lastIdx , lastIdx, {})

def containSquareOfZeros2(info , r1 , c1 , r2 , c2 , cache):
    if r1 >= r2 or c1 >= c2:
        return False
    key = coordToString(r1,r2,c1,c2)
    if key in cache:
        return cache[key]
    cache[key] = (
        isSquareOfZeros(r1 , r2 , c1, c2 , info)
        or containSquareOfZeros2(info , r1 + 1 , c1 +1 , r2 , c2, cache)
        or containSquareOfZeros2(info , r1 + 1 , c1 , r2 , c2 - 1 , cache)
        or containSquareOfZeros2(info , r1 , c1 , r2 - 1 , c2 -1 , cache)
        or containSquareOfZeros2(info , r1 , c1 + 1 , r2 - 1 , c2 , cache)
        or containSquareOfZeros2(info , r1 + 1 , c1 + 1 , r2 -1 , c2 - 1, cache)
    )
    return cache[key]
