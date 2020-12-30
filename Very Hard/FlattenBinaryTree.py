def flattenBinaryTree( root):
    nodesInOrder = []
    traverseInOrder(root , nodesInOrder)
    for i in range(len(nodesInOrder)):
        node = nodesInOrder[i]
        node.left = nodesInOrder[ i - 1] if i-1 >= 0 else None
        node.right = nodesInOrder[ i + 1] if i + 1 < len(nodesInOrder) else None
    return nodesInOrder[0]
def traverseInOrder(node , nodes):
    if node is None: return
    traverseInOrder(node.left, nodes)
    nodes.append(node)
    traverseInOrder(node.right , nodes)
        
#SOLUTION2 my solution
def flattenBinaryTree2( root ):
    leftMost = {}
    traverse(root , None, leftMost)
    return leftMost['leftMost']

def traverse(node, prev, leftMost):
    if node is None: return
    if node.left is None and node.right is None:
        node.left = prev
        if prev is not None:
            prev.right = node
        else:
            leftMost['leftMost'] = node
        return node
    newPrev = traverse(node.left , prev, leftMost)
    node.left = newPrev
    newPrev.right = node
    nodeToReturn = traverse(node.right, node, leftMost)
    return nodeToReturn if nodeToReturn is not None else node

#SOLUTION3 same idea, different coding
def flattenBinaryTree3( root ):
    leftMost, _ = flattenTree(root)
    return leftMost

def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftLeftMost, leftRightMost = flattenTree(node.left)
        connect(leftRightMost , node)
        leftMost = leftLeftMost
    if node.right is None:
        rightMost = node
    else:
        rightLeftMost , rightRightMost = flattenTree(node.right)
        connect(node , rightLeftMost)
        rightMost = rightRightMost
    return [leftMost , rightMost]

def connect(left, right):
    left.right = right
    right.left = left