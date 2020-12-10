# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    main = headOne
	prev = None
	two = headTwo
	while main is not None and two is not None:
		if main.value <= two.value:
			prev = main
			main = main.next
		else:
			if prev is not None:
				prev.next = two
			prev = two
			two = two.next
			prev.next = main
	if main is None:
		prev.next = two
	return headOne if headOne.value <= headTwo.value else headTwo


###SOLUTION  2 recursive
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
	recursiveMerge(headOne, headTwo, None)
	return min(headOne, headTwo, key= lambda x: x.value)

def recursiveMerge(main, two, prev):
	if main is None:
		prev.next = two
		return
	if two is None: return
	if main.value <= two.value:
		recursiveMerge(main.next, two, main)
	else:
		if prev is not None:
			prev.next = two
		newTwo = two.next
		two.next = main
		recursiveMerge(main, newTwo, two)