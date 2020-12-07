def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo) : return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0: return True

    if arrayOne[0] != arrayTwo[0] : return False

    leftOne = getSmallerNums(arrayOne)
    leftTwo = getSmallerNums(arrayTwo)

    rightOne = getBiggerOrEqualNums(arrayOne)
    rightTwo = getBiggerOrEqualNums(arrayTwo)

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getSmallerNums(array):
    smallers = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smallers.append(array[i])
    return smallers

def getBiggerOrEqualNums(array):
    biggerOrEquals = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEquals.append(array[i])
    return biggerOrEquals


###SOLUTION 2

def sameBsts2(arrayOne, arrayTwo):
    return areSame(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))

def areSame(arrayOne, arrayTwo,idxOne, idxTwo, lowerBound, upperBound):

    if idxOne == -1 or idxTwo == -1:
        return idxOne == idxTwo
    
    if arrayOne[idxOne] != arrayTwo[idxTwo]: return False

    leftChildIdxOne = getLeftChildIdx(arrayOne, idxOne, lowerBound)
    leftChildIdxTwo = getLeftChildIdx(arrayTwo, idxTwo, lowerBound)
    rightChildIdxOne = getRightChildIdx(arrayOne, idxOne, upperBound)
    rightChildIdxTwo = getRightChildIdx(arrayTwo, idxTwo, upperBound)

    currentValue = arrayOne[idxOne]

    isLeftTheSame = areSame(arrayOne, arrayTwo , leftChildIdxOne, leftChildIdxTwo, lowerBound, currentValue) 

    isRightTheSame = areSame(arrayOne, arrayTwo, rightChildIdxOne, rightChildIdxTwo, currentValue, upperBound)

    return  isLeftTheSame  and  isRightTheSame   

def getLeftChildIdx(array, idx, lowerBound):
    for i in range(idx + 1, len(array)):
        if array[i] < array[idx] and array[i] >= lowerBound:
            return i
    return -1

def getRightChildIdx(array, idx, upperBound):
    for i in range(idx + 1, len(array)):
        if array[i] >= array[idx] and array[i] < upperBound:
            return i
    return -1

