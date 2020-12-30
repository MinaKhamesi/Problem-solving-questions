def apartmentHunting( blocks , reqs ):
    distances = [float('-inf') for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closest = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closest = min(closest , abs( j - i))
            distances[i] = max(distances[i] , closest)
    return getMinIdx(distances)

def getMinIdx(dists):
    minVal = dists[0]
    minIdx = 0
    for i, val in enumerate(dists):
        if val < minVal:
            minVal = val
            minIdx = i
    return minIdx

#SOLUTION 2
def apartmentHunting2( blocks , reqs ):
    distances = list(map( lambda req: getFarthests(blocks , req) , reqs))
    return getMinIdx2( distances )

def getFarthests(blocks , req):
    farthest = [float('-inf') for block in blocks]
    closest = float('-inf')
    for i in range(len(blocks)):
        if blocks[i][req]:
            closest = i
        farthest[i] = i - closest
    closest = float('inf')
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closest = i
        farthest[i] = min(farthest[i] , closest - i)
    return farthest

def getMinIdx2( distances ):
    minVal = float('inf')
    minIdx = -1
    for blockIdx in range(len(distances[0])):
        maxInBlock = float('-inf')
        for reqIdx in range(len(distances)):
            maxInBlock = max(maxInBlock , distances[reqIdx][blockIdx])
        if maxInBlock < minVal:
            minVal = maxInBlock
            minIdx = blockIdx
    return minIdx