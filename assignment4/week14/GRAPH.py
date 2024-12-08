from collections import OrderedDict
class Vertex:
    def __init__(self, key = None):
        self.key = key 
        
    def __str__(self): return str(self.key)
    def __repr__(self): return str(self.key)
    def __hash__(self): return hash(self.key)
    def __eq__(self, other): return self.key == other.key
    def __ne__(self, other): return self.key != other.key
    def __lt__(self, other): return self.key < other.key
    def __le__(self,other): return self.key <= other.key
    def __gt__(self, other): return self.key > other.key
    def __ge__(self,other): return self.key >= other.key
    
    
    
    
class Edge: ## u->v(w) u에서 v로 (가중치 = w)
    def __init__(self, u = None, v = None, w = None): ## u, v = vertex
        self.u = u
        self.v = v
        self.w = w
        
    def __str__(self):
        return str(self.u) + "->" + str(self.v) + '(' + str(self.w) + ')'
    def __repr__(self):
        return str(self.u) + "->" + str(self.v) + '(' + str(self.w) + ')'        
    def __hash__(self): return hash(self.w)
    def __eq__(self, other): return self.w == other.w
    def __ne__(self, other): return self.w != other.w
    def __lt__(self, other): return self.w < other.w
    def __le__(self,other): return self.w <= other.w    
    def __gt__(self, other): return self.w > other.w
    def __ge__(self,other): return self.w >= other.w
    def getU(self):
        return self.u
    def getV(self):
        return self.v
    def getW(self):
        return self.w



class Graph :
    def __init__(self, d = False, gdict = None):
        if gdict is None :
            gdict = {} ## by using dictionary // gdict = {vertex : [edge]}
        self.gdict = gdict
        self.directed = d
        self.keyIndex = {} ##containing vertex's index ## key = vertex, iem = vertex sequence
    
    def __len__(self):
        return len(self.gdict)
    
    def __str__(self):
        gs = ""
        for  vtx in self.gdict:
            gs += "{} : {}".format(vtx, self.gdict[vtx])
        return gs
        
    def getorder(self):
        return len(self.gdict.keys())
        
    def addVertex(self, vtx):
        if vtx in self.gdict.keys():
            print("Vertex is already in grahp")
        else :
            self.gdict[vtx] = [] ## A list containing edges
            self.keyIndex[vtx] = len(self.keyIndex) + 1 
    def addEdge(self, e : Edge):
        if e.getU() in self.gdict:
            self.gdict[e.getU()].append(e)
            
        if not self.directed:
            e2 = Edge(e.getV(), e.getU(), e.getW())
            if e.getV() in self.gdict:  # e.getV()가 그래프에 존재하는지 확인
                self.gdict[e.getV()].append(e2)
            else:
                print(f"Vertex {e.getV()} does not exist in the graph.")
            
            
    def isDirected(self):
        return self.directed
    
    def getADJlist(self):
        adjlist = {}
        for vtx in self.gdict:
            adjlist[vtx] = set(self.getNeighborsVertices(vtx))
        return adjlist
    
    def printADJlist(self):
        alist = self.getADJlist()
        print("ADJacency List")
        for vtx in alist :
            print("{} : {}".format(vtx, alist[vtx]))
            
        
    def getADJmatrix(self):
        adjMatrix = [[0 for x in range(self.getorder())] for y in range(self.getorder())]
        for e in self.getEdgeList():
            adjMatrix[self.keyIndex[e.getU()]-1][self.keyIndex[e.getV()]-1] = e.getW()
        return adjMatrix            
    
    def printADJMatrix(self):
        M = self.getADJmatrix()
        print("ADJacency Matrix \n")
        for i in range(0, self.getorder):
            print()
            for j in range(0,self.getorder()):
                print("{0:>2d}".format(M[i][j]), end = "")
            
        
    def getEdgeList(self):
        elist = []
        for vtx in self.gdict:
            for e in self.gdict[vtx]:
                elist.append(e)
        return elist
        
        
    def getVertixList(self):
        dict1 = OrderedDict(sorted(self.keyIndex.items()))
        return list(dict1)
    
    def getNeighborsVertices(self, vtx) -> list: 
        elist = self.gdict[vtx]
        vlist = []
        for e in elist :
            vlist.append(e.getV())
        return vlist
    
    def GetShortestPath(self, vertex) :
        if len(self.gdict[vertex]) == 0:
            return False
        elist = self.gdict[vertex]
        minpath = self.gdict[vertex][0]
        for edge in elist:
            temp = edge
            if temp < minpath :
                minpath = temp
        return minpath
    
    def getDegree(self):
        pass
    def getOutDegree(self):
        pass
    def getInDegree(self):
        pass
    def getSize(self):
        pass
    def getWeihgt(self):
        pass
    def isCyclic(self):
        pass
    def RemoveEdge(self, edge : Edge):
        U = edge.getU()
        if self.isDirected() :
            self.gdict[U].remove(edge)
            return
        V = edge.getV()
        self.gdict[U].remove(edge)
        for e in self.gdict[V]:
            if e.getV() == U :
                self.gdict[V].remove(e)
        return 
    
        
    def RemoveVertex(self, vertex : Vertex):
        if vertex not in self.gdict:
            print("Vertex not found in the graph")
            return
        neighbor_vertex = self.getNeighborsVertices(vertex)
        for neighbor in neighbor_vertex:
            for edge in self.gdict[neighbor]:
                if edge.getV() == vertex :
                    self.gdict[neighbor].remove(edge)
        del self.gdict[vertex]
        return
    
        
    
            
            
            
        
        
    
    