# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
		self.lowers = Heap('max')
        self.greaters = Heap('min')
        self.median = None

    def insert(self, number):
		if len(self.lowers.heap) == 0:
			self.lowers.insert(number)
		elif len(self.greaters.heap) == 0:
			self.greaters.insert(number)
		else:
			if number <= self.lowers.peak():
				self.lowers.insert(number)
			else:
				self.greaters.insert(number)
		#To Balance the Two heaps		
		if abs(self.lowers.size - self.greaters.size) > 1:
			larger = max(self.lowers, self.greaters, key = lambda x:x.size)
			smaller = min(self.lowers, self.greaters, key= lambda x: x.size)
			numToAdd = larger.remove()
			smaller.insert(numToAdd)
		#To Update median
		if abs(self.lowers.size - self.greaters.size) == 1 :
			larger = max(self.lowers, self.greaters, key=lambda x: x.size)
			self.median = larger.peak()
		else:
			num1 = self.lowers.peak()
			num2 = self.greaters.peak()
			self.median = (num1 + num2) / 2
			
				

    def getMedian(self):
        return self.median
	
	
class Heap:
	def __init__(self, type):
		self.type = type
		self.heap = []
		self.size = 0
		
	def insert(self, number):
		self.heap.append(number)
		self.siftUp(self.heap , self.size)
		self.size += 1
		
	def remove(self):
		self.heap[0], self.heap[-1] = self.heap[-1] , self.heap[0]
		numToReturn = self.heap.pop()
		self.siftDown(self.heap, 0)
		self.size -= 1
		return numToReturn
		
	def peak(self):
		return self.heap[0]
	
	def siftUp(self, heap, idx):
		currentIdx = idx
		parentIdx = (idx - 1) // 2
		while parentIdx >= 0 and needToSwapUp(heap, currentIdx, parentIdx, self.type):
			heap[currentIdx] , heap[parentIdx] = heap[parentIdx], heap[currentIdx]
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
			
	def siftDown(self, heap, idx):
		currentIdx = idx
		leftChildIdx = (idx * 2) + 1
		rightChildIdx = (idx * 2) + 2
		while leftChildIdx < len(heap) :
			if rightChildIdx < len(heap) and rightIsBetterForSwap(heap, rightChildIdx, leftChildIdx, self.type):
				idxToSwap = rightChildIdx
			else:
				idxToSwap = leftChildIdx
			if needToSwapDown( heap , idxToSwap, currentIdx, self.type):
				heap[idxToSwap] , heap[currentIdx] = heap[currentIdx] , heap[idxToSwap]
				currentIdx = idxToSwap
				leftChildIdx = (currentIdx * 2) + 1
				rightChildIdx = (currentIdx * 2) + 2
			else:
				break
 			
def needToSwapUp(heap, current, parent, typ):
	if typ == 'min':
		return heap[current] < heap[parent]
	if typ == 'max':
		return heap[current] > heap[parent]
	
def rightIsBetterForSwap(heap, right, left, typ):
	if typ == 'min':
		return heap[right] < heap[left]
	else:
		return heap[right] > heap[left]
		
def needToSwapDown(heap, child, current, typ):
	if typ == 'min':
		return heap[child] < heap[current]
	else:
		return heap[child] > heap[current]
		
