def rightSiblingTree( root ):
    buildRights(root , None, None)
    return root

def buildRights(node , parent, isLeftChild):
    if node is None: return
    left , right = node.left , node.right

    buildRights(node.left , node , True)

    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right:
            node.right = parent.right.left
        else:
            node.right = None
    
    buildRights(right , node , False)

