def allKindsOfNodeDepths( root ):
    return getTreeInfo( root ).sumOfAllDepths

def getTreeInfo( node ):
    if node is None:
        return TreeInfo(0 , 0 , 0)
    leftInfo = getTreeInfo(node.left)
    rightInfo = getTreeInfo(node.right)
    sumOfDepths = leftInfo.sumOfDepths + leftInfo.subtreeSize + rightInfo.sumOfDepths + rightInfo.subtreeSize
    subtreeSize = leftInfo.subtreeSize + rightInfo.subtreeSize + 1
    sumOfAllDepths = leftInfo.sumOfAllDepths + rightInfo.sumOfAllDepths + sumOfDepths
    return TreeInfo(subtreeSize , sumOfDepths , sumOfAllDepths)

class TreeInfo:
    def __init__(self, subtreeSize , sumOfDepths , sumOfAllDepths):
        self.subtreeSize = subtreeSize
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths

#######EXACT SAME SOLUTION WITHOUT CLASS
def allKindsOfNodeDepths2(root):
	depthOfThisNode , sizeOfSubtree, sumOfDepths = calculateDepth(root , 0)
	return sumOfDepths

def calculateDepth(node , runningSum):
	if node is None:
		return [0 , 0 , runningSum]
	leftDepth , leftSize, runningSum = calculateDepth(node.left , runningSum)
	rightDepth , rightSize, runningSum = calculateDepth(node.right , runningSum)
	currentNodeSum = leftDepth + rightDepth
	runningSum += currentNodeSum
	nextLevelDepth = leftDepth + leftSize + rightDepth + rightSize + 1
	nextLevelSubtreeSize = leftSize + rightSize + 1
	return [nextLevelDepth , nextLevelSubtreeSize , runningSum]
######## SAME SOLUTION BUT SAVING INFO IN A DICTIONARY 
def allKindsOfNodeDepths3( root ):
    subtreeSizes = {}
    calculateSizes(root , subtreeSizes)
    nodeDepths = {}
    calculateSumDepths( root , nodeDepths, subtreeSizes)
    return calculateSumOfAllDepths(root , nodeDepths)

def calculateSizes(root , subtreeSizes):
    if root is None: return 0
    subtreeSizes[root] = calculateSizes(root.left, subtreeSizes) + calculateSizes(root.right, subtreeSizes) + 1
    return subtreeSizes[root] 

def calculateSumDepths( root , nodeDepths , subtreeSizes):
    if root is None: return 0
    currentDepths = 0
    if root.left:
        calculateSumDepths( root.left , nodeDepths , subtreeSizes)
        currentDepths += nodeDepths[root.left] + subtreeSizes[root.left]
    if root.right:
        calculateSumDepths(root.right , nodeDepths , subtreeSizes)
        currentDepths += nodeDepths[root.right] + subtreeSizes[root.right]
    nodeDepths[root] = currentDepths

def calculateSumOfAllDepths(node , nodeDepths):
    if node is None: return 0
    return calculateSumOfAllDepths(node.left , nodeDepths ) + calculateSumOfAllDepths(node.right , nodeDepths) + nodeDepths[node]


##########################
def allKindOfNodeDepths3( root ):
    runningSum = 0
    stack = [ root ]
    while len(stack):
        node = stack.pop()
        if node is None: continue
        runningSum += nodeDepth( node )
        stack.append(node.left)
        stack.append(node.right)
    return runningSum


####### SAME SOLUTION RECURSIVE 
def allKindsOfNodeDepths4( root ):
    return allKindsOfNodeDepths4(root.left) + allKindsOfNodeDepths4(root.right) + nodeDepth(root)
###
def nodeDepth( node, depth=0 ):
    if node is None: return 0
    return nodeDepth(node.left , depth + 1) + nodeDepth(node.right, depth + 1) + depth

##########################SOLUTION 5 & 6
def allKindsOfNodeDepths5( root , depthsSum = 0 , depth= 0):
    if root is None: return 0
    depthsSum += depth
    return depthsSum + allKindsOfNodeDepths5(root.left , depthsSum , depth + 1) + allKindsOfNodeDepths5(root.right , depthsSum , depth + 1)

def allKindsOfNodeDepths6( root , depth =0):
    if root is None: return 0
    depthSum = (depth *(depth + 1)) / 2
    return depthSum + allKindsOfNodeDepths6( root.left , depth + 1) + allKindsOfNodeDepths6(root.right , depth + 1)

