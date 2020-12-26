#SOLUTION 1
#O(bns) time | O(n) space
def multiStringSearch(bigString, smallStrings):
    return [isInBig(bigString,smallString) for smallString in smallStrings]

def isInBig(big, small):
    for i in range(len(big)):
        if i + len(small) > len(big):break
        if isInBigHelper(big,small,i): return True
    return False

def isInBigHelper(big,small,start):
    leftSmall, rightSmall = 0, len(small) - 1
    leftBig, rightBig = start, start + len(small) - 1
    while leftSmall <= rightSmall:
        if small[leftSmall] != big[leftBig] or small[rightSmall] != big[rightBig]:
            return False
        leftSmall += 1
        rightSmall -= 1
        leftBig += 1
        rightBig -= 1
    return True

