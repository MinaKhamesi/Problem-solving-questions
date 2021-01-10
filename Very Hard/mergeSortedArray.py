def mergeSortedArrays( arrays ):
    idxs = [0 for array in arrays]
    result = []
    while True:
        smallestNum = float('inf')
        smallestNumIdx = None
        for i in range(len(arrays)):
            currentArray = arrays[i]
            currentArrayIdx = idxs[i]
            if currentArrayIdx >= len(currentArray): continue
            if currentArray[currentArrayIdx] < smallestNum:
                smallestNum = currentArray[currentArrayIdx]
                smallestNumIdx = i
        if smallestNum == float('inf'): break
        result.append(smallestNum)
        idxs[smallestNumIdx] += 1
    return result

############SOLUTION2
def mergeSortedArrays2( arrays ):
    minHeap = MinHeap()
    for i in range(len(arrays)):
        minHeap.insert({'value':arrays[i][0] , 'arrayIdx': i , 'elementIdx' : 0})
    result = []
    while not minHeap.isEmpty():
        nextMin = minHeap.pop()
        val = nextMin['value']
        arrayIdx = nextMin['arrayIdx']
        elementIdx = nextMin['elementIdx']
        result.append(val)
        if elementIdx + 1 < len(arrays[arrayIdx]):
            minHeap.insert({'value': arrays[arrayIdx][elementIdx + 1] , 'arrayIdx': arrayIdx , 'elementIdx': elementIdx + 1})
    return result

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self , node):
        self.heap.append(node)
        self.siftUp(len(self.heap) - 1 , self.heap)

    def pop(self):
        self.swap(0 , len(self.heap) - 1 , self.heap)
        nodeToReturn = self.heap.pop()
        self.siftDown(0 , self.heap)
        return nodeToReturn

    def isEmpty(self):
        return len(self.heap) == 0

    def siftUp(self, currentIdx , array):
        parentIdx = (currentIdx - 1) // 2
        while parentIdx >= 0 and array[currentIdx]['value'] < array[parentIdx]['value']:
            self.swap(currentIdx , parentIdx , array)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def siftDown(self , currentIdx , array):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx < len(array):
            childTwoIdx = childOneIdx + 1
            if childTwoIdx >= len(array) or array[childOneIdx]['value'] < array[childTwoIdx]['value']:
                idxToSwap = childOneIdx
            else:
                idxToSwap = childTwoIdx
            
            if array[idxToSwap]['value'] < array[currentIdx]['value']:
                self.swap(idxToSwap , currentIdx , array)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def swap(self, i , j , array):
        array[i] , array[j] = array[j] , array[i]

