def waterFallStreams( array , source ):
    finalBuckets = [0 for bucket in array[0]]
    exploreWater(array , 1 , source , 100 , finalBuckets)
    return finalBuckets

def exploreWater( array , row, col , amount , finalBuckets, goRight = None):
    if col < 0 or col >= len(array[row]): return
    if array[row - 1][col] == 1 :return
    if row == len(array) - 1:
        finalBuckets[col] += amount
        return
    if array[row][col] == 0:
        exploreWater( array , row + 1, col, amount , finalBuckets)

    else:
        if goRight is None:
            exploreWater( array , row , col + 1 , amount / 2 , finalBuckets , True)
            exploreWater( array , row , col - 1 , amount / 2 , finalBuckets , False)
        elif goRight:
            exploreWater( array , row , col + 1 , amount , finalBuckets , True)
        else:
            exploreWater( array , row , col - 1 , amount, finalBuckets , False)


###SOLUTION 2
### O(w^2 * h) time | O(w) space w -->width , h --> height
def waterFallStreams2( array ,source ):
    rowAbove = array[0][:]
    rowAbove[source] = - 100
    for i in range( 1 , len(array)):
        current = array[i][:]

        for col in range(len(current)):

            hasWater = rowAbove[col] < 0
            isBlocked = current[col] == 1
            
            if not hasWater: continue
            if not isBlocked:
                current[col] += rowAbove[col]
                continue

            waterSplit = rowAbove[col] / 2

            left = col
            while left - 1 >= 0:
                left -= 1
                if rowAbove[left] == 1:
                    break
                if current[left] != 1:
                    current[left] += waterSplit
                    break
                
            right = col
            while right + 1 < len(current):
                right += 1
                if rowAbove[right] == 1:
                    break
                if current[right] != 1:
                    current[right] += waterSplit
                    break
                
        rowAbove = current
    return [amount * -1 for amount in rowAbove]

