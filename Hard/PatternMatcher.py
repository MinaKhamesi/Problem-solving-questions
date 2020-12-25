def patternMatcher(pattern, string):
    startsWithX = pattern[0] == 'x'
    if startsWithX:
        newPattern = list(pattern)
    else:
        newPattern = list(map(lambda char: 'x' if char == 'y' else 'y', list(pattern)))
    numX, numY, xBeforeY = getInfo(newPattern)
    if numY == 0:
        lenX = len(string) / numX
        if lenX % 1 != 0 :
            return []
        lenX = int(lenX)
        x = string[:lenX]
        possibleMatch = numX*x
        if possibleMatch == string:
            return [x,''] if startsWithX else ['', x]
    else:
        for lenX in range(1, len(string)):
            lenY = (len(string) - lenX*numX) / numY
            if lenY % 1 != 0: continue
            lenY = int(lenY)
            x = string[:lenX]
            yStartIdx = xBeforeY*lenX
            y = string[yStartIdx : yStartIdx + lenY]
            possibleMatch = list(map(lambda char: x if char == 'x' else y, newPattern))
            if ''.join(possibleMatch) == string:
                return [x,y] if startsWithX else [y,x]
    return []

def getInfo(newPattern):
    numX, numY, xBeforeY = 0, 0, None
    for char in newPattern:
        if char == 'x':
            numX += 1
        if char == 'y':
            numY += 1
            if xBeforeY == None:
                xBeforeY = numX
    return numX, numY, xBeforeY
