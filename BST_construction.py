class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while currentNode:
            if value >= currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

        return self

    def contains(self, value):
        currentNode = self
        while currentNode:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                return True
        return False

    def remove(self, value):
        currentNode = self
        if not currentNode.left and not currentNode.right: return self
        parent = None
        while currentNode is not None:
            if value > currentNode.value:
                parent = currentNode
                currentNode = currentNode.right
            elif value < currentNode.value:
                parent = currentNode
                currentNode = currentNode.left
            else:
                if currentNode.left  and currentNode.right :
                    nodeToReplace = self.findMostLeftOfRightBranchAndRemoveItsConnection(currentNode)
                    currentNode.value = nodeToReplace.value
                # if node to remove is Root and it has only one child
                elif parent is None:
                    if currentNode.left:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    else:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                # if node to remove has one child or no child and it has a parent
                else:
                    if parent.left == currentNode:
                        parent.left = currentNode.left if currentNode.left else currentNode.right
                    else:
                        parent.right = currentNode.right if currentNode.right else currentNode.left
                    break
                    
                    
        return self

    def findMostLeftOfRightBranchAndRemoveItsConnection(self,Node):
        currentNode = Node.right
        parent = Node

        if currentNode.left is None:
            parent.right = None
            return currentNode

        while currentNode.left is not None:
            parent = currentNode
            currentNode = currentNode.left
            
        parent.left = None
        return currentNode

node1 = BST(5)
node1.insert(10)
node1.insert(3)
node1.insert(2)
node1.insert(4)
node1.insert(15)
node1.insert(11)
node1.insert(13)
node1.insert(8)
node1.insert(9)
print(node1.contains(3))
node1.remove(5)
node1.remove(13)
node1.remove(10)

