def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx1 = 0
    idx2 = 0
    leastDifference = float('inf')
    closest_nums = None
    while idx1<len(arrayOne) and idx2<len(arrayTwo):
        num1, num2 = arrayOne[idx1], arrayTwo[idx2]
        if abs(num1-num2) < leastDifference:
            leastDifference = abs(num1-num2)
            closest_nums = [num1,num2]
        if num1 < num2 :
            idx1 += 1
        elif num2 < num1:
            idx2 += 1
        else:
            return [num1,num2]
    return closest_nums
