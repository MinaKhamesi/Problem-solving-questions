
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    position = 0
	first = head
	secondNodeToSeeEnd = head
	while position < k :
		secondNodeToSeeEnd = secondNodeToSeeEnd.next
		position += 1
	if secondNodeToSeeEnd is None:
		head.value = head.next.value
		head.next = head.next.next
	else:
		while secondNodeToSeeEnd.next is not None:
			first = first.next
			secondNodeToSeeEnd = secondNodeToSeeEnd.next
		first.next = first.next.next
