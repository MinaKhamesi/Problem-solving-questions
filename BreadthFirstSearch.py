class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    ## Since the question state that nodes are tree-like and there is no cycle so we don't need a visited list
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue):
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            queue = queue + currentNode.children
        return array