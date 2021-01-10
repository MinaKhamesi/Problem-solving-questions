def airportConnections( airports , routes , startingAirport):
    graph = createGraph(airports , routes)
    unreachableNodes = getUnreachableNodes(graph , startingAirport, airports)
    rankUnreachableNodes(unreachableNodes , graph)
    return getMinNewConnections(unreachableNodes , graph)

def createGraph(airports , routes):
    graph = {}
    for airport in airports:
        graph[airport] = AirportNode(airport)
    for airport , connection in routes:
        graph[airport].connections.append(connection)
    return graph

def getUnreachableNodes(graph , startingAirport , airports):
    visited = {}
    depthFirstTraverse(startingAirport , graph , visited)
    
    unreachableNodes = []
    for airport in airports:
        if airport not in visited:
            graph[airport].isReachable = False
            unreachableNodes.append( graph[airport])
    
    return unreachableNodes

def depthFirstTraverse(airport , graph, visited):
    if airport in visited: return
    visited[airport] = True
    connections = graph[airport].connections
    for connection in connections:
        depthFirstTraverse(connection , graph , visited)

def rankUnreachableNodes(unreachableNodes , graph):
    for airportNode in unreachableNodes:
        unreachablesReachableFromHere = []
        visited = {}
        depthFirstAddUnreachable(airportNode.airport , unreachablesReachableFromHere , visited , graph)
        airportNode.unreachables = unreachablesReachableFromHere

def depthFirstAddUnreachable(airport , unreachables , visited , graph):
    if airport in visited: return
    if graph[airport].isReachable: return
    visited[airport] = True
    unreachables.append(graph[airport])
    connections = graph[airport].connections
    for connection in connections:
        depthFirstAddUnreachable(connection , unreachables , visited , graph)

def getMinNewConnections(unreachableNodes , graph):
    unreachableNodes.sort(key  = lambda node: len(node.unreachables) , reverse = True)
    minNumberOfNewConnections = 0
    for node in unreachableNodes:
        if node.isReachable: continue
        minNumberOfNewConnections += 1
        reachables = node.unreachables
        for nextNode in reachables:
            nextNode.isReachable = True
    return minNumberOfNewConnections

class AirportNode:
    def __init__(self,airport):
        self.airport = airport
        self.connections = []
        self.unreachables = []
        self.isReachable = True
