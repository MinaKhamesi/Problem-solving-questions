def minHeightBst(array):
    midIdx = (len(array)-1)//2
    root = BST(array[midIdx])
    insertMiddleNum(array,0,midIdx-1,root)
    insertMiddleNum(array,midIdx+1, len(array)-1,root)
    return root

def insertMiddleNum(array,startIdx,endIdx,node):
	if endIdx < startIdx: return
	midIdx = (startIdx + endIdx)//2
	node.insert(array[midIdx])
	insertMiddleNum(array,startIdx,midIdx-1,node)
	insertMiddleNum(array,midIdx+1,endIdx,node)
	
	
## solution2 without using .insert method, so that time complexity become O(N) instead of O(NlogN)
def minHeightBst2(array):
    midIdx = (len(array)-1)//2
    root = BST(array[midIdx])
    addMiddleNum(array,0,midIdx-1,root)
    addMiddleNum(array,midIdx+1, len(array)-1,root)
    return root

def addMiddleNum(array,startIdx,endIdx,node):
    if endIdx < startIdx : return
    midIdx = ( startIdx + endIdx ) // 2
    newNode = BST(array[midIdx])
    if array[midIdx] >= node.value:
        node.right = newNode
    else:
        node.left = newNode
    addMiddleNum(array,startIdx, midIdx -1 , newNode)
    addMiddleNum(array, midIdx + 1, endIdx, newNode)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
