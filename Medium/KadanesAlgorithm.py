def kadanesAlgorithm(array):
    runningMaxSum = 0
    maxTillNow = float('-inf')
    for num in array:
        runningMaxSum = max(num, runningMaxSum + num)
        maxTillNow = max(maxTillNow, runningMaxSum)
    return maxTillNow

# a tiny diffrence in writing the code
def kadanesAlgorithm2(array):
    runningSum = 0
    maxTillNow = float('-inf')
    for num in array:
        runningSum += num
        maxTillNow = max(maxTillNow, runningSum)
        if runningSum < 0:
            runningSum = 0
    return maxTillNow