'''
hint: https://www.quora.com/How-does-following-algorithm-for-finding-longest-path-in-tree-work
'''

import math

class Queue():
	def __init__(self):
		self.items = []

	def enqueue(self,n):
		self.items.insert(0,n)

	def dequeue(self):
		if len(self.items) == 0:
			return False
		return self.items.pop()

	def peek(self):
		if len(self.items) == 0:
			return False
		return self.items[len(self.items)-1]

	def is_empty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

	def show(self):
		print self.items


class Vertex:
	def __init__(self,key):
		self.id = key
		self.color = 'white'
		self.distance = float('inf')
		self.connectedTo = {}
		self.predecessor = None

	def addNbr(self,nbr,cost=0):
		self.connectedTo[nbr] = cost

	def __str__(self):
		d = self.connectedTo.keys()
		a = ''
		for x in d:
			a = a + str(x) + ' '
		return str(self.id) + ' is at a distance ' + str(self.distance) +' from source'

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]


class Graph:
	def __init__(self):
		self.vertList = {}
		self.size = 0

	def addVertex(self,key):
		self.size = self.size + 1
		v = Vertex(key)
		self.vertList[key] = v
		return v

	def getVertex(self,key):
		if key in self.vertList:
			return self.vertList[key]
		else:
			return None

	def __contain__(self,key):
		if key in self.vertList:
			return self.vertList[n]
		else:
			return None

	def addEdge(self,fromVertex,toVertex,cost=0):
		if fromVertex not in self.vertList:
			f = self.addVertex(fromVertex)
		if toVertex not in self.vertList:
			t = self.addVertex(toVertex)
		self.vertList[fromVertex].addNbr(toVertex)

	def getVertices(self):
		return self.vertList.keys()


def bfs(g,start):
    max_d = 0
    farthest_nbr_id = 0
    q = Queue()
    startVertex = g.getVertex(start)
    startVertex.distance = 0
    startVertex.predecessor = None
    q.enqueue(start)
    while q.size()!=0:
        vertex_id = q.dequeue()
        vertex = g.getVertex(vertex_id)
        vertex.color = 'gray'
        for nbr_id in vertex.getConnections():
            nbr = g.getVertex(nbr_id)
            if nbr.color == 'white':
                nbr.predecessor = vertex
                nbr.distance = vertex.distance + 1
                if nbr.distance > max_d:
                    max_d = nbr.distance
                    farthest_nbr_id = nbr_id
                q.enqueue(nbr_id)
        vertex.color = 'black'
    return (farthest_nbr_id,max_d)

g = Graph()
num_nodes = int(raw_input())
for i in range(num_nodes-1):
    v1,v2 = raw_input().split(' ')
    v1 = int(v1)
    v2 = int(v2)
    g.addEdge(v1,v2)
    g.addEdge(v2,v1)

vertex_in_mid,distance_till_there = bfs(g,v2)

for v_id in g.getVertices():
    v = g.getVertex(v_id)
    v.color = 'white'
    v.distance = float('inf')
    v.predecessor = None


final_nbr_id,final_max_dist = bfs(g,vertex_in_mid)
print final_max_dist

'''
for v_id in g.getVertices():
    v = g.getVertex(v_id)
    print v.distance
'''
