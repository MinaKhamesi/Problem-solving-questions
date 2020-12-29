def rightSmallerThan(array):
    rightSmallers = [0 for num in array]
    for i in range(len(array)):
        currentNum = array[i]
        count = 0
        for j in range(i + 1 , len(array)):
            if array[j] < currentNum:
                count += 1
        rightSmallers[i] = count
    return rightSmallers

##SOLUTION2

def rightSmallerThan2( array ):
    rightSmallers = [0 for num in array]
    if not len(array): return []
    bst = BST(array[-1])
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i] , i, rightSmallers)

    return rightSmallers

class BST:
    def __init__(self, value):
        self.value = value
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, rightSmallers, numElementsSmaller = 0):
        if value < self.value:
            self.leftSubtreeSize += 1
            if self.left:
                self.left.insert(value, idx, rightSmallers, numElementsSmaller)
            else:
                self.left = BST(value)
                rightSmallers[idx] = numElementsSmaller
        else:
            numElementsSmaller += self.leftSubtreeSize
            if value > self.value:
                numElementsSmaller += 1
            if self.right:
                self.right.insert(value, idx, rightSmallers, numElementsSmaller)
            else:
                self.right = BST(value)
                rightSmallers[idx] = numElementsSmaller