def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(array, 0, endIdx)
        siftDown(array, 0, endIdx - 1)
    return array

def buildMaxHeap(array):
    for i in reversed(range(len(array))):
        siftDown(array, i, len(array) - 1)

def siftDown(array, startIdx, endIdx):
    leftChildIdx = startIdx * 2 + 1
    currentIdx = startIdx
    while leftChildIdx <= endIdx:
        rightChildIdx = leftChildIdx + 1
        if rightChildIdx > endIdx or array[leftChildIdx] > array[rightChildIdx]:
            idxToSwap = leftChildIdx
        else:
            idxToSwap = rightChildIdx
        if array[currentIdx] < array[idxToSwap]:
            swap(array, currentIdx, idxToSwap)
            currentIdx = idxToSwap
            leftChildIdx = currentIdx * 2 + 1
        else:
            return
def swap(arr , i , j):
    arr[i] , arr[j] = arr[j] , arr[i]