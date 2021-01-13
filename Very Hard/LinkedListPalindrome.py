class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def linkedListPalindrome( head ):
    slowNode = head
    fastNode = head
    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    secondPartHead = invertLinkedList(slowNode)
    firstPartNode = head
    secondPartNode = secondPartHead
    while secondPartNode is not None :
        if firstPartNode.value != secondPartNode.value:
            return False
        firstPartNode = firstPartNode.next
        secondPartNode = secondPartNode.next
    return True

def invertLinkedList( node ):
    prev = None
    current = node
    while current is not None:
        nextToGo = current.next
        current.next = prev
        prev = current
        current = nextToGo
    return prev

######################
def linkedListPalindrome2( head ):
    isPalindromeResult , _ = isPalindrome(head , head)
    return isPalindromeResult

def isPalindrome(leftNode , rightNode):
    if rightNode is None:
        return True,leftNode
    isPalindromeResult , newLeft = isPalindrome(leftNode , rightNode.next)
    palindromeToThisPoint = isPalindromeResult and newLeft.value == rightNode.value
    return palindromeToThisPoint , newLeft.next

#########################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome3(head):
    length = calculateLength(head)
	secondPartPosition = length // 2
	secondPartNode = head
	i = 0
	while i < secondPartPosition:
		secondPartNode = secondPartNode.next
		i += 1
	
	palindromeLength = 2 if (length / 2) % 1 == 0 else 3
	while palindromeLength <= length:
		current = head
		i = 1
		while i < length - secondPartPosition :
			current = current.next
			i += 1
		if current.value != secondPartNode.value: return False
		secondPartNode = secondPartNode.next
		secondPartPosition += 1
		palindromeLength += 2
	return True

def calculateLength(head):
	length = 0
	node = head
	while node is not None:
		node = node.next
		length += 1
	return length
