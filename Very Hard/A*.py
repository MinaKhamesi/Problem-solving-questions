def aStar(startRow , startCol , endRow , endCol , graph):
    nodes = initializeNodes(graph)

    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode , endNode)
    startNode.totalDistance = startNode.estimatedDistanceToEnd 

    nodesToVisit = MinHeap([startNode])
    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.pop()
        if currentMinDistanceNode == endNode: break
        tentativeDistance = currentMinDistanceNode.distanceFromStart + 1
        neighbors = getNeighbors(currentMinDistanceNode , nodes)
        for neighbor in neighbors:
            if neighbor.value == 1: continue
            if neighbor.distanceFromStart <= tentativeDistance: continue
            neighbor.distanceFromStart = tentativeDistance
            neighbor.cameFrom = currentMinDistanceNode
            neighbor.estimatedDistanceToEnd = calculateManhattanDistance(neighbor , endNode)
            neighbor.totalDistance = neighbor.distanceFromStart + neighbor.estimatedDistanceToEnd
            if not nodesToVisit.contains(neighbor):
                nodesToVisit.insert(neighbor)
            else:
                nodesToVisit.update(neighbor)
    return reconstructPath(endNode)

def initializeNodes(graph):
    nodes = []
    for i,row in enumerate(graph):
        rowToAdd = []
        for j, value in enumerate(row):
            rowToAdd.append(Node(i,j,value))
        nodes.append(rowToAdd)
    return nodes

def calculateManhattanDistance(node1 , node2):
    r1  = node1.row
    r2 = node2.row
    c1 = node1.col
    c2 = node2.col
    return abs(r2 - r1) + abs(c2 - c1)

def getNeighbors(neighbor , nodes):
    neighbors = []
    lastIdx = len(nodes) - 1
    r = neighbor.row
    c = neighbor.col
    possibles = [[r+1 , c],[r - 1, c],[r , c+1] , [r , c-1]]
    for row,col in possibles:
        if row < 0 or row > lastIdx or col < 0 or col > lastIdx:
            continue
        neighbors.append(nodes[row][col])
    return neighbors

def reconstructPath(endNode):
    if endNode.cameFrom is None: return []
    current = endNode
    path = []
    while current is not None:
        path.append([current.row , current.col])
        current = current.cameFrom
    return path[::-1]


class Node:
    def __init__(self , row , col , value):
        self.id = str(row) + '-' + str(col)
        self.row = row
        self.col = col
        self.value = value
        self.cameFrom = None
        self.distanceFromStart = float('inf')
        self.estimatedDistanceToEnd = float('inf')
        self.totalDistance = float('inf')

class MinHeap:
    def __init__(self,array):
        self.heap = array
        self.positionsInHeap = {node.id:idx for idx, node in enumerate(self.heap)}


    def isEmpty(self):
        return len(self.heap) == 0


    def contains(self, node):
        return node.id in self.positionsInHeap

        
    def insert(self , node):
        self.positionsInHeap[node.id] = len(self.heap) - 1
        self.heap.append(node)
        self.siftUp(len(self.heap) - 1 , self.heap)

    def update(self, node):
        startIdx = self.positionsInHeap[node.id]
        self.siftUp(startIdx, self.heap)


    def pop(self):
        self.swap(0 , len(self.heap) - 1 , self.heap)
        nodeToReturn = self.heap.pop()
        del self.positionsInHeap[nodeToReturn.id]
        self.siftDown(0 , self.heap)
        return nodeToReturn


    def siftUp(self,currentIdx, array):
        parentIdx = (currentIdx - 1) // 2
        while parentIdx >= 0 and array[parentIdx].totalDistance > array[currentIdx].totalDistance:
            self.swap(currentIdx , parentIdx , array)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1 )// 2


    def siftDown(self, currentIdx , array):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx < len(array):
            childTwoIdx = childOneIdx + 1
            if childTwoIdx >= len(array) or array[childOneIdx].totalDistance < array[childTwoIdx].totalDistance:
                idxToSwap = childOneIdx
            else:
                idxToSwap = childTwoIdx
            if array[currentIdx].totalDistance <= array[idxToSwap].totalDistance:
                return
            self.swap(idxToSwap , currentIdx, array)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1




    def swap(self, i , j , array):
        self.positionsInHeap[array[i].id] = j
        self.positionsInHeap[array[j].id] = i 

        array[i] , array[j] = array[j] , array[i]
    