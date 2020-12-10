def reverseLinkedList(head):
    if head.next is None: return head
	current = head.next
	previous = head
	head.next = None
	while current is not None:
		nextNode = current.next
		current.next = previous
		previous = current
		current = nextNode
	return previous