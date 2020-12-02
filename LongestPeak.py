def longest_peak(array):
    i=1
    longest_peak_length = 0
    while i<len(array)-1:
        is_peak = array[i]>array[i-1] and array[i]>array[i+1]
        if not is_peak:
            i += 1
            continue
			
        leftIdx = i-2
        while leftIdx>=0 and array[leftIdx]<array[leftIdx+1]:
            leftIdx -= 1
			
        rightIdx = i + 2
        while rightIdx<len(array) and array[rightIdx]<array[rightIdx-1]:
            rightIdx += 1
			
        current_peak_length = rightIdx - leftIdx - 1
        longest_peak_length = max(longest_peak_length,current_peak_length)
        i = rightIdx
    return longest_peak_length