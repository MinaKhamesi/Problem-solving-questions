def quickSelect(array, k):
    position = k - 1
    return quickSelectHelper(array, 0, len(array) - 1, position)

def quickSelectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception('Algorithm should never reach here')
        splitIdx = startIdx
        idx = startIdx
        while idx < endIdx:
            if array[idx] < array[endIdx]:
                swap(array, idx, splitIdx)
                splitIdx += 1
            idx += 1
        swap(array, endIdx, splitIdx)
        if splitIdx == position:
            return array[splitIdx]
        elif position > splitIdx:
            startIdx = splitIdx + 1
        else:
            endIdx = splitIdx - 1
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
