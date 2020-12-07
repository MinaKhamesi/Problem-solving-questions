def maxPathSum(tree):
	if tree is None: return 0
    info = {'maxSum':float('-inf')}
	calculateSums(tree, info)
	return info['maxSum']

def calculateSums(node, info):
	if node is None: return 0
	
	leftSum = calculateSums(node.left, info)
	rightSum = calculateSums(node.right, info)
	
	currentPathMaxSum = max((leftSum + rightSum + node.value), (leftSum + node.value), (rightSum + node.value), node.value)
	
	info['maxSum'] = max(info['maxSum'], currentPathMaxSum)
	
	maxBranchSum = max(max(leftSum, rightSum) + node.value , node.value)
	
	return maxBranchSum
