def powerset(array, idx=None):
	powerSets = [[]]
	for i in range(len(array)):
		newLists = []
		for arr in powerSets:
			newLists.append(arr+[array[i]])
		powerSets += newLists
	return powerSets

#solution2
def powerset2(array,idx = None):
	powersets = []
	if idx is None: 
		idx = len(array) - 1
	if idx<0:
		return [[]]
	powersets = powerset(array,idx-1) 
	for i in range(len(powersets)):
		new_powerset = powersets[i] + [array[idx]]
		powersets.append(new_powerset)
	return powersets