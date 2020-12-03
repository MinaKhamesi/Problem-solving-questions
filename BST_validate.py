class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree,lowerBound=float('-inf'),upperBound=float('inf')):
    if tree is None:
        return True
    isValid = tree.value >= lowerBound and tree.value < upperBound
    if isValid:
        return validateBst(tree.right, tree.value, upperBound) and validateBst(tree.left, lowerBound, tree.value)
    else:
        return False