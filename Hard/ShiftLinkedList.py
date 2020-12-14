def shiftLinkedList(head, k):
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1

    offset = abs(k) % length

    if offset == 0: return head

    newTailPosition = length - offset if k > 0 else offset

    newTail = head
    for i in range(1, newTailPosition):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    tail.next = head
    return newHead
