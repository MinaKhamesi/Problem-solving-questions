def ThreeNumberSum(array,targetSum):
    array.sort()
    allTripletsEqualToTarget = []
    for firstIdx in range(len(array)-2):
        leftIdx = firstIdx + 1
        rightIdx = len(array)-1
        firstNum = array[firstIdx]
        while leftIdx<rightIdx:
            leftNum = array[leftIdx]
            rightNum = array[rightIdx]
            currentSum = firstNum + leftNum + rightNum
            if currentSum == targetSum:
                allTripletsEqualToTarget.append([firstNum,leftNum,rightNum])
                leftIdx += 1
            elif currentSum > targetSum:
                rightIdx -= 1
            else:
                leftIdx += 1
    return allTripletsEqualToTarget

print(ThreeNumberSum([12,3,1,2,-6,5,-8,6], 0)==[[-8,2,6],[-8,3,5],[-6,1,5]])
