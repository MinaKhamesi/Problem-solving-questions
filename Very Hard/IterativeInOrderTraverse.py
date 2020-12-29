def iterativeInOrderTraversal(tree, callback):
    prev = None
    while tree is not None:
        if prev == tree.parent :
            if tree.left:
                nextNode = tree.left
            else:
                callback(tree)
                nextNode = tree.right if tree.right else tree.parent
        elif prev == tree.left:
            callback(tree)
            nextNode = tree.right if tree.right else tree.parent
        else:
            nextNode = tree.parent
        prev = tree
        tree = nextNode
        
