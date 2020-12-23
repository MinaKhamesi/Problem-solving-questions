def quickSort(array):
    sortHelper(array, 0, len(array) - 1)
	return array

def sortHelper(arr, startIdx, endIdx):
	if startIdx >= endIdx: return
	pivotIdx = startIdx
	idx = startIdx
	while idx < endIdx:
		if arr[idx] < arr[endIdx]:
			swap(arr, idx, pivotIdx)
			pivotIdx += 1
		idx += 1
	swap(arr, endIdx, pivotIdx)
	leftIsSmaller = (pivotIdx - startIdx) < (endIdx - pivotIdx)
	
	if leftIsSmaller:
		sortHelper(arr, startIdx, pivotIdx - 1)
		sortHelper(arr, pivotIdx + 1, endIdx)
	else:
		sortHelper(arr, pivotIdx + 1, endIdx)
		sortHelper(arr, startIdx, pivotIdx - 1)
		
def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]
			
