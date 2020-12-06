class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        for i in reversed(range(len(array))):
            self.siftDown(array,i)
        return array

    def siftDown(self, array, idx):
        currentIdx = idx
        leftChildIdx = (idx * 2) + 1
        rightChildIdx = (idx * 2) + 2
        while leftChildIdx < len(array) :
            rightChildIdx = rightChildIdx if rightChildIdx < len(array) else -1
            if rightChildIdx == -1 or array[leftChildIdx] < array[rightChildIdx]:
                childToSwapIdx = leftChildIdx
            else:
                childToSwapIdx = rightChildIdx
            if array[currentIdx] > array[childToSwapIdx] :
                array[ currentIdx] , array[childToSwapIdx] = array[childToSwapIdx], array[ currentIdx]
                currentIdx = childToSwapIdx
                leftChildIdx = (currentIdx * 2) + 1
                rightChildIdx = ( currentIdx * 2) + 2
            else:
                break

    def siftUp(self, array, idx):
		currentIdx = idx
        parentIdx = (idx-1) // 2
		while parentIdx >= 0 and array[ parentIdx] > array[currentIdx] :
			array[parentIdx] , array[currentIdx] = array[ currentIdx], array[ parentIdx ]
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		valueToReturn = self.heap.pop()
		self.siftDown(self.heap, 0)
		return valueToReturn

    def insert(self, value):
        self.heap.append(value)
		self.siftUp( self.heap, len(self.heap)-1 )
