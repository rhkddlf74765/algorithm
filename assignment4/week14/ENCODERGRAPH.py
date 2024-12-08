from GRAPH import Graph, Vertex, Edge
class EncodeGraph:
    def getGraph01(self):
        g = Graph(False)
        v1 = Vertex("A")
        v2 = Vertex("B")
        v3 = Vertex("C")
        v4 = Vertex("D")
        v5 = Vertex("E")
        v6 = Vertex("F")
        v7 = Vertex("G")
        v8 = Vertex("H")
        
        g.addVertex(v1)
        g.addVertex(v2)
        g.addVertex(v3)
        g.addVertex(v4)
        g.addVertex(v5)
        g.addVertex(v6)
        g.addVertex(v7)
        g.addVertex(v8)
        
        e1 = Edge(v1, v2, 1)
        e2 = Edge(v1, v3, 1)
        e3 = Edge(v2, v4, 1)
        e4 = Edge(v3, v4, 1)
        e5 = Edge(v3, v5, 1)
        e6 = Edge(v5, v7, 1)
        e7 = Edge(v5, v8, 1)
        e8 = Edge(v7, v8, 1)
        e9 = Edge(v4, v6, 1)                

        g.addEdge(e1)
        g.addEdge(e2)
        g.addEdge(e3)        
        g.addEdge(e4)
        g.addEdge(e5)
        g.addEdge(e6)
        g.addEdge(e7)
        g.addEdge(e8)
        g.addEdge(e9) 
        g.RemoveEdge(e1)
        
        return g 
    def getGraph02(self):
        graph = Graph(True)
    
    def getGraph03(self):
        graph = Graph(True)
    
EncodeGraph().getGraph01()
        
        