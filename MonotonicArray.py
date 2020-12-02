def Monotonic(array):
    is_non_decreasing = True
    is_non_increasing = True
    for i in range(1,len(array)):
        if array[i] > array[i-1]:
            is_non_increasing = False
        elif array[i] < array[i-1]:
            is_non_decreasing = False
    return is_non_increasing or is_non_decreasing
        