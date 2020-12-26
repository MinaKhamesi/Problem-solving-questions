def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid < array[mid]:
            right = mid - 1
        elif mid > array[mid]:
            left = mid + 1
        else:
            if mid == 0 or array[mid - 1] != mid - 1:
                return mid
            else:
                right = mid - 1 
    return -1