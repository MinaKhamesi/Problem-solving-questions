def rectangleMania(coords):
    coordTable = {coordToString(coord):True for coord in coords}
    rectangleCount = 0
    for x1,y1 in coords:
        for x2,y2 in coords:
            if isInUpperRight([x2,y2] , [x1,y1]):
                if coordToString([x1,y2]) in coordTable and coordToString([x2,y1]) in coordTable:
                    rectangleCount += 1
    return rectangleCount

def isInUpperRight(coord2 , coord1):
    x2 , y2 = coord2
    x1 , y1 = coord1
    return x2 > x1 and y2 > y1

def coordToString(coord):
    x , y = coord
    return str(x) + '-' + str(y)

#########Solution 2
def rectangleMania2(coords):
    xTable = {}
    yTable = {}
    for x, y in coords:
        if x not in xTable:
            xTable[x] = []
        xTable[x].append([x, y])
        if y not in yTable:
            yTable[y] = []
        yTable[y].append([x , y])

    rectangleCount = 0
    for upperRightAngle in coords:
        rectangleCount += countRectangles(upperRightAngle , 'Right' , upperRightAngle , xTable , yTable)
    return rectangleCount

def countRectangles(current , direction , origin , xTable, yTable):
    if direction == 'FinishingPoint':
        return 1 if current == origin else 0
    
    nextPossiblePoints = getPoints(current , direction , xTable, yTable)
    nextDirection = getNextDirection(direction)

    rectangleCount = 0
    for point in nextPossiblePoints:
        rectangleCount += countRectangles(point , nextDirection, origin , xTable , yTable)
    
    return rectangleCount

def getPoints(current , direction, xTable, yTable):
    x , y = current
    nextPoints = []
    if direction == 'Right':
        possibles = yTable[y]
        for x1,y1 in possibles:
            if x1 > x:
                nextPoints.append([x1,y1])
    if direction == 'Down':
        possibles = xTable[x]
        for x1, y1 in possibles:
            if y1 < y:
                nextPoints.append([x1 , y1])

    if direction == 'Left':
        possibles = yTable[y]
        for x1, y1 in possibles:
            if x1 < x:
                nextPoints.append([x1 , y1])
    
    if direction == 'Up':
        possibles = xTable[x]
        for x1 , y1 in possibles:
            if y1 > y:
                nextPoints.append([x1 , y1])
    return nextPoints

def getNextDirection(direction):
    if direction == 'Right': return 'Down'
    if direction == 'Down': return 'Left'
    if direction == 'Left': return 'Up'
    if direction == 'Up': return 'FinishingPoint'

