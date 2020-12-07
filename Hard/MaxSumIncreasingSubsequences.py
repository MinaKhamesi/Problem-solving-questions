def maxSumIncreasingSubsequence(array):
    maxSumTillNow = [num for num in array]
    idxs = [None for _ in array]
    maxSum = float('-inf')
    startingIdx = -1
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i]:
                if maxSumTillNow[j] + array[i] > maxSumTillNow[i]:
                    maxSumTillNow[i]  = maxSumTillNow[j] + array[i]
                    idxs[i] = j
                
        if maxSumTillNow[i] > maxSum:
            maxSum = maxSumTillNow[i]
            startingIdx = i
            
    numsContributed = []
    currentIdx = startingIdx
    while currentIdx is not None:
        numsContributed.append(array[currentIdx])
        currentIdx = idxs[currentIdx]
    return [maxSum, list(reversed(numsContributed))]

print(maxSumIncreasingSubsequence([10,70,20,30,50,11,30]))