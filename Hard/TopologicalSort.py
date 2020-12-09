def topologicalSort(jobs, deps):
    graph = Graph(jobs)
    graph.addDependencies(deps)
    order = []
    for node in graph.nodes.values():
        hasCycle = do_the_job(node, order)
        if hasCycle : return []
    return order


def do_the_job(node, order):
	if node.completed : return False
	if node.visiting: return True
	node.visiting = True
	for preRequisiteNode in node.dependencies:
		hasCycle = do_the_job(preRequisiteNode,order)
		if hasCycle: return True
	order.append(node.value)
	node.completed = True
	node.visiting = False
	
class Graph:
	def __init__(self,jobs):
		self.nodes = self.addNodesToGraph(jobs)
		
	def addNodesToGraph(self, jobs):
		nodes = {}
		for job in jobs:
			node = Node(job)
			nodes[job] = node
		return nodes
	
	def addDependencies(self, deps):
		for job1, job2 in deps:
			node2 = self.nodes[job2]
			node1 = self.nodes[job1]
			node2.addDep(node1)
		
	
class Node:
	def __init__(self,value):
		self.value = value
		self.completed = False
		self.visiting = False
		self.dependencies = []
		
	def addDep(self,node):
		self.dependencies.append(node)