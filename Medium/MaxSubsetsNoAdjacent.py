def maxSubsetSumNoAdjacent(array):
    if not len(array): return 0
    if len(array)<3: return max(array)
    max_non_adjacent = array[0]
    max_adjacent = max( array[0], array[1] )
    for i in range(2,len(array)):
        current_max = max(max_non_adjacent + array[i], max_adjacent)
        max_non_adjacent = max_adjacent
        max_adjacent = current_max
    return current_max

def maxSubsetSumAdjacent2(array):
    if not len(array): return 0
    if len(array)<3: return max(array)
    maxSums = array[:]
    maxSums[1] = max(maxSums[0], maxSums[1])
    for i in range(2,len(array)):
        maxSums[i] = max(maxSums[ i - 1 ], maxSums[ i - 2 ] + array[i])
    return maxSums[-1]