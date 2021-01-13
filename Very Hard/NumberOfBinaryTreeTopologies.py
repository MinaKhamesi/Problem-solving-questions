def numberOfBinaryTreeTopologies( n , cache={0:1}):
    if n in cache: return cache[n]
    numberOfTopologies = 0
    for leftSubtreeSize in range(n):
        rightSubtreeSize = n - 1 - leftSubtreeSize
        numberOfLeftTopologies = numberOfBinaryTreeTopologies(leftSubtreeSize , cache)
        numberOfRightTopologies = numberOfBinaryTreeTopologies(rightSubtreeSize , cache)
        numberOfTopologies += (numberOfLeftTopologies * numberOfRightTopologies)
    cache[n] = numberOfTopologies
    return cache[n]

def numberOfBinaryTreeTopologies2(n):
    cache = [1]
    for size in range(1 ,n + 1):
        numberOfTopologies = 0
        for leftSubtreeSize in range(size):
            rightSubtreeSize = size - 1 - leftSubtreeSize
            leftNum = cache[leftSubtreeSize]
            rightNum = cache[rightSubtreeSize]
            numberOfTopologies += (leftNum * rightNum)
        cache.append(numberOfTopologies)
    return cache[n]
    