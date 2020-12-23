def searchForRange(array, target):
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange

def alteredBinarySearch(array, target, startIdx, endIdx, finalRange, goLeft):
    while startIdx <= endIdx:
        mid = (startIdx + endIdx) // 2
        if target < array[mid]:
            endIdx = mid - 1
        elif target > array[mid]:
            startIdx = mid + 1
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return
                else:
                    endIdx = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                else:
                    startIdx = mid + 1