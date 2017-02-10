# Graphs
# vertex - node
# Edges - directed or undirected
# Edges may be weighted or unweighted
# Graph Representation : G = (V,E)
# Vertices Representation : V = {v1,v2,v3,v4}
# Edges Representation : E = {(V1,V2,4),(v2,V3,6)}
# Path : Sequences of Edges
# Cycle : Same starting and ending point. No cycles => Acyclic graph
# DAG : Directed Acyclic Graph.
# Adjacency Matrix : Easiest way to represent a graph (uses 2D array)
# AM is good when number of edges is large |V|^2(number of edges needed to fill AM)
# AM is good when every vertex is connected to every other vertex.
# Adjacency List : More space-efficient way to implement a sparsely connected graph.



# Class vertex

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnection(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):

        return str(self.id)+' connected to:'+ str([x.id for x in self.connectedTo])


class Graph:

    def __init__(self):
        self.vertexList = {}
        self.numberVertices = 0

    def addVertex(self,key):
        self.numberVertices += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def addEdge(self,fro,too,cost=0):
        if fro not in self.vertexList:
            nv = self.addVertex(fro)
        if too not in self.vertexList:
            nv = self.addVertex(too)

        self.vertexList[fro].addNeighbor(self.vertexList[too],cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())

    def __contains__(self,n):
        return n in self.vertexList

graph = Graph()
for i in range(6):
    graph.addVertex(i)

graph.vertexList
graph.addEdge(0,1,2)
for vertex in graph:
    print vertex
    print vertex.getConnection()
    print '\n'


