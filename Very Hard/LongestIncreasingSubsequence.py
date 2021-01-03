def longestIncreasingSubsequence( array ):
    longests = [1 for num in array]
    idxs = [None for idx in array]
    maxLengthIdx = 0
    for i in range(1 , len(array)):
        for j in range(i):
            if array[j] < array[i] and longests[j] + 1 > longests[i]:
                longests[i] = longests[j] + 1
                idxs[i] = j
        if longests[i] > longests[maxLengthIdx]:
            maxLengthIdx = i
    return buildSequence( idxs , maxLengthIdx  , array)

def buildSequence(idxs , firstIdx , array):
    result = []
    current = firstIdx
    while current is not None:
        result.append(array[current])
        current = idxs[current]
    return list(reversed(result))

##SOLUTION 2
def longestIncreasingSubsequence2( array ):
    idxsInLengths = [None for length in range(len(array) + 1)]
    idxsToBacktrack = [None for idx in array]
    idxsInLengths[1] = 0
    maxLength = 1
    for i, num in enumerate(array):
        maxLengthAchivable = binarySearch( 1 , maxLength , idxsInLengths , array , num)
        if maxLengthAchivable > maxLength:
            idxsInLengths[maxLengthAchivable] = i
            maxLength = maxLengthAchivable
            idxsToBacktrack[i] = idxsInLengths[maxLengthAchivable - 1]
        else:
            currentNumInLength = array[idxsInLengths[maxLengthAchivable]]
            if num < currentNumInLength:
                idxsInLengths[maxLengthAchivable] = i
                idxsToBacktrack[i] = idxsInLengths[maxLengthAchivable - 1]
    return buildSequence2(idxsToBacktrack , idxsInLengths[maxLength] , array)

def binarySearch(minLength , maxLength , lengths , array , num):
    if minLength > maxLength:
        return minLength
    middleLength = (minLength + maxLength) // 2
    idxInMiddleLength = lengths[middleLength]
    numInMiddleLength = array[idxInMiddleLength]
    if num > numInMiddleLength :
        minLength = middleLength + 1
    else:
        maxLength = middleLength - 1
    return binarySearch(minLength , maxLength , lengths, array , num)

def buildSequence2(idxs , firstIdx , array):
    result = []
    current = firstIdx
    while current is not None:
        result.append(array[current])
        current = idxs[current]
    return list(reversed(result))