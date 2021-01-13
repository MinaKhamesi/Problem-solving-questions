def rearrangeLinkedList( head , k ):
    smallerListHead = None
    smallerListTail = None
    equalListHead = None
    equalListTail = None
    largerListHead = None
    largerListTail = None
    
    node = head
    while node is not None:
        if node.value < k:
            smallerListHead , smallerListTail = growLinkedList(node , smallerListHead , smallerListTail)
        if node.value == k :
            equalListHead , equalListTail = growLinkedList(node , equalListHead , equalListTail)
        if node.value > k :
            largerListHead , largerListTail = growLinkedList(node , largerListHead , largerListTail)
        nextToGo = node.next
        node.next = None
        node = nextToGo

    newHead , newTail = mergeLists(smallerListHead , smallerListTail , equalListHead , equalListTail)
    finalHead , _ = mergeLists(newHead , newTail , largerListHead , largerListTail)
    return finalHead

def growLinkedList( node , head , tail):
    if head is None:
        newHead = node
        newTail = node
    elif head == tail:
        head.next = node
        newTail = node
        newHead = head
    else:
        tail.next = node
        newTail = node
        newHead = head
    return newHead , newTail

def mergeLists(smallerHead , smallerTail , largerHead , largerTail):
    newHead = largerHead if smallerHead is None else smallerHead
    newTail = smallerTail if largerTail is None else largerTail
    if smallerTail is not None:
        smallerTail.next = largerHead
    return newHead , newTail