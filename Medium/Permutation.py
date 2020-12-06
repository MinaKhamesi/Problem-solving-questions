def traverseArray(array, i , perms):
	if i>=len(array) -1:
		perms.append(array[:])
	else:
		for j in range(i,len(array)):
			array[i] , array[j] = array[j], array[i]
			traverseArray(array, i + 1, perms)
			array[i] , array[j] = array[j], array[i]
