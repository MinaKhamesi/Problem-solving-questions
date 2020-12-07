def minNumberOfJumps(array):
    if len(array) < 2: return 0
    jump = 1
    maxReach = array[0]
    steps = array[0] - 1
    for i in range(1, len(array)):
        maxReach = max(maxReach, i + array[i])
        if steps == 0 and i != len(array) - 1:
            jump += 1
            steps = maxReach - i
        steps -= 1
    return jump

def minNumberOfJumps2(array):
    if len(array) < 2 : return 0
    minJumps = [float('inf') for _ in array]
    minJumps[0] = 0
    for i in range(1,len(array)):
        for j in range(i):
            isReachable = array[j] + j >= i
            if isReachable:
                minJumps[i] = min(minJumps[i], minJumps[j] + 1)
    return minJumps[-1]