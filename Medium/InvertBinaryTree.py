def invertBinaryTree(tree):
    if tree is None: return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

#solution2 
def invertBinaryTree2(tree):
    stack = [tree]
    while len(stack):
        current = stack.pop()
        if current is None: continue
        current.left, current.right = current.right, current.left
        stack.append(current.left)
        stack.append(current.right)
    





