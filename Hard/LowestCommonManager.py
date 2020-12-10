def getLowestCommonManager(topManager, reportOne, reportTwo):
	info = {'LCM': None}
	exploreTree(topManager, reportOne, reportTwo, info)
	return info['LCM']

def exploreTree(node, one, two, info):
	if node is None: return
	count = 0
	for reportNode in node.directReports:
		newCount = exploreTree(reportNode, one, two, info)
		if info['LCM']: return 
		count += newCount
	if node == one or node == two:
		count += 1
	if count == 2:
		info['LCM'] = node
	return count
	
### SOLUTION 2(its basically the same in a new format)
def getLowestCommonManager2(topManager, reportOne, reportTwo):
	return getInfo(topManager, reportOne, reportTwo).lowestManager

def getInfo(manager, one, two):
	numVisited = 0
	for reporter in manager.directReports:
		info = getInfo(reporter, one, two)
		if info.lowestManager is not None:
			return info
		else:
			numVisited += info.numVisited
	if manager == one or manager == two:
		numVisited += 1
	lowestManager = manager if numVisited == 2 else None
	return Info(lowestManager, numVisited)

class Info:
	def __init__(self, lowestManager, numVisited):
		self.lowestManager = lowestManager
		self.numVisited = numVisited