class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    heightOne = calculateHeight(topAncestor, descendantOne)
    heightTwo = calculateHeight(topAncestor, descendantTwo)
    NodeOne = descendantOne
    NodeTwo = descendantTwo
    while heightTwo > heightOne :
        NodeTwo = NodeTwo.ancestor
        heightTwo -= 1
    while heightOne > heightTwo :
        NodeOne = NodeOne.ancestor
        heightOne -= 1
    while NodeOne is not None and NodeTwo is not None:
        if NodeOne == NodeTwo:
            return NodeOne
        else:
            NodeOne = NodeOne.ancestor
            NodeTwo = NodeTwo.ancestor
    return topAncestor

def calculateHeight(top, node):
	size = 1
	while node!= top:
		size += 1
		node = node.ancestor
	return size