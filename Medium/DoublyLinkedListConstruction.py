# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
			return
        self.insertBefore(self.head, node)

    def setTail(self, node):
		if self.tail is None:
			self.setHead(node)
			return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail: return
        current = self.head
		while current is not None:
			if current == nodeToInsert:
				self.remove(nodeToInsert)
				break
			else:
				current = current.next
		if node == self.head:
			nodeToInsert.next = node
			node.prev = nodeToInsert
			self.head = nodeToInsert
		else:
			nodeToInsert.next = node
			nodeToInsert.prev = node.prev
			node.prev.next = nodeToInsert
			node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert== self.tail: return
        current = self.head
		while current is not None:
			if current == nodeToInsert:
				self.remove(current)
				break
			else:
				current = current.next
		if node == self.tail:
			self.tail.next = nodeToInsert
			nodeToInsert.prev = self.tail
			self.tail = nodeToInsert
		else:
			nodeToInsert.prev = node
			nodeToInsert.next = node.next
			node.next.prev = nodeToInsert
			node.next = nodeToInsert
				

    def insertAtPosition(self, position, nodeToInsert):
		if position == 1:
			self.setHead(nodeToInsert)
			return
        currentPosition = 1
		current = self.head
		while currentPosition < position:
			current = current.next
			currentPosition += 1
		if current is None:
			self.setTail(nodeToInsert)
		else:
			self.insertBefore(current, nodeToInsert)

    def removeNodesWithValue(self, value):
        current = self.head
		while current is not None:
			if current.value == value:
				nextNode = current.next
				self.remove(current)
				current = nextNode
			else:
				current = current.next

    def remove(self, node):
		if node == self.head :
			self.head = node.next
		if node == self.tail:
			self.tail = node.prev
			
		if node.prev is not None:
        	node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		
		node.next, node.prev = None, None

    def containsNodeWithValue(self, value):
        current = self.head
		while current is not None:
			if current.value == value:
				return True
			current = current.next
		return False
