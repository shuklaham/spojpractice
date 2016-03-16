class Vertex:
	def __init__(self,key):
		self.id = key
		self.color = 'white'
		self.distance = float('inf')
		self.connectedTo = {}
		self.predecessor = None
		self.discoveryTime = 0
		self.finishTime = 0

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

t = 0
flag = True
def dfs(g,start):
	global t
	global flag
	startVert = g.getVertex(start)
	startVert.predecessor = None
	_dfs(g,startVert)

def _dfs(g,startVert):
	global t
	global flag
	t = t + 1
	startVert.discoveryTime = t
	startVert.color = 'gray'
	for nbrString in startVert.getConnections():
		nbr = g.getVertex(nbrString)
		if nbr.color in ['gray','black'] and nbr == startVert.predecessor:
			flag = False
		if nbr.color == 'white':
			nbr.predecessor = startVert
			_dfs(g,nbr)
	t = t + 1
	startVert.finishTime = t
	startVert.color = 'black'

nodes,edges = raw_input().split(' ')
nodes = int(nodes)
edges = int(edges)
g = Graph()
for i in xrange(edges):
	n1key,n2key = raw_input().split(' ')
	g.addEdge(n1key,n2key)
	g.addEdge(n2key,n1key)

dfs(g,n1key)

for v in g.getVertices():
	actualVert = g.getVertex(v)
	if actualVert.color == 'white':
		flag = False
if nodes -1 != edges:
	flag = False

if flag:
	print 'YES'
else:
	print 'NO'