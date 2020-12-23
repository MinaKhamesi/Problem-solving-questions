def shiftedBinarySearch(array, target):
    return helper(array, target, 0, len(array) - 1)

def helper(array, target, startIdx, endIdx):
    while startIdx <= endIdx:
        middle = (startIdx + endIdx) // 2
        if array[middle] == target:
            return middle
        elif array[startIdx] <= array[middle]:
            if target >= array[startIdx] and target < array[middle]:
                endIdx = middle - 1
            else:
                startIdx = middle + 1
        else:
            if target > array[middle] and target <= array[endIdx]:
                startIdx = middle + 1
            else:
                endIdx = middle - 1
    return -1
