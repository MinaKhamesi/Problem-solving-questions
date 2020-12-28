def subarraySort(array):
    minUnsorted = float('inf')
    maxUnsorted = float('-inf')
    for i in range(len(array)):
        if i - 1 >= 0 and array[i] < array[i-1]:
            minUnsorted = min(minUnsorted, array[i] )
            maxUnsorted = max(maxUnsorted, array[i])
        if i + 1 < len(array) and array[i + 1] < array[i]:
            minUnsorted = min(minUnsorted , array[i] )
            maxUnsorted = max(maxUnsorted , array[i])

    if minUnsorted == float('inf'): return [-1 , -1]
    firstIdx=0
    while firstIdx < len(array) and array[firstIdx] <= minUnsorted:
        firstIdx += 1

    lastIdx = len(array) - 1
    while lastIdx >= 0 and array[lastIdx] >= maxUnsorted:
        lastIdx -= 1

    return [firstIdx , lastIdx]