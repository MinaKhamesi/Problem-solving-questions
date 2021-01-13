def mergeSort( array ):
    if len(array) <= 1: return array
    middle = len(array) // 2
    leftHalf = mergeSort(array[:middle])
    rightHalf = mergeSort(array[middle:])
    return sort(leftHalf , rightHalf)

def sort(array1 , array2):
    result = []
    idx1 = idx2 = 0
    while idx1 < len(array1) and idx2 < len(array2):
        if array1[idx1] <= array2[idx2]:
            result.append(array1[idx1])
            idx1 += 1
        else:
            result.append(array2[idx2])
            idx2 += 1
    while idx1 < len(array1):
        result.append(array1[idx1])
        idx1 += 1
    while idx2 < len(array2):
        result.append(array2[idx2])
        idx2 += 1
    return result

def mergeSort2( array ):
    if len(array) <= 1 : return array
    helperArray = array[:]
    splitAndSortInPlace(array , 0 , len(array) - 1 , helperArray)
    return array

def splitAndSortInPlace(mainArray , startIdx , endIdx, helperArray):
    if startIdx == endIdx: return
    middleIdx = (startIdx + endIdx) // 2
    splitAndSortInPlace(helperArray , startIdx , middleIdx , mainArray)
    splitAndSortInPlace(helperArray , middleIdx + 1 , endIdx , mainArray)
    mergeAndSort(mainArray , startIdx , middleIdx , endIdx , helperArray)

def mergeAndSort(mainArray , startIdx , middleIdx , endIdx , helperArray):
    idx = startIdx
    idx1 = startIdx
    idx2 = middleIdx + 1
    while idx1 <= middleIdx and idx2 <= endIdx:
        if helperArray[idx1] < helperArray[idx2]:
            mainArray[idx] = helperArray[idx1]
            idx1 += 1
        else:
            mainArray[idx] = helperArray[idx2]
            idx2 += 1
        idx += 1
    
    while idx1 <= middleIdx:
        mainArray[idx] = helperArray[idx1]
        idx1 += 1
        idx += 1
    
    while idx2 <= endIdx:
        mainArray[idx] = helperArray[idx2]
        idx2 += 1
        idx += 1
