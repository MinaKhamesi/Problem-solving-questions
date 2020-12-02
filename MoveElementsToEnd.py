def move_elements_to_end(array,num):
    pivotIdx = len(array) - 1
    for i in reversed(range(len(array))):
        if array[i] == num:
            swap(i,pivotIdx,array)
            pivotIdx -= 1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]
