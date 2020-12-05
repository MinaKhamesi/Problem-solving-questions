def threeNumberSort(array, order):
	idx = 0
    for num in order:
		idx = moveToStart(array,num,idx)
	return array

def moveToStart(array,num,idx):
	splitIdx = idx
	for i in range(idx,len(array)):
		if array[i] == num:
			swap(splitIdx, i, array)
			splitIdx += 1
	return splitIdx

def swap(i, j , array):
	array[i] , array[j] = array[j] , array[i]

## having three splitting index like firstIdx, secondIdx and thirdIdx is also a good idea. in one loop all be sorted. The Thing is order is always length 3.