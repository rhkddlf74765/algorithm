from GRAPH import Graph , Edge
from ENCODERGRAPH import EncodeGraph
import queue
class MST:
    def kluskar(self):
        pass
    def prims(self, g : Graph):

        graph = g ## graph imitation
        Vlist = graph.getVertixList()
        q = queue.Queue(maxsize=len(Vlist))
        current = Vlist[0]
        new_graph = Graph() ##empty graph
        new_graph.addVertex(current)
        q.put(current)
        
        e = Edge(0,0,10000)
        for p in range(len(graph)):
            minedge = e
            for i in range(q.qsize()):
                current = q.get()
                temp = graph.GetShortestPath(current)
                print("yes")
                if temp is False :
                    continue
                print(temp)
                if temp < minedge:
                    minedge = temp
                print("minedge = {}".format(minedge))
            graph.RemoveEdge(minedge)
            new_graph.addVertex(minedge.getV())
            new_graph.addEdge(minedge)
            print("new_graph : ")
            print(new_graph)
            print("graph : ")
            print(graph)
            for v in new_graph.getVertixList():
                q.put(v)
        return new_graph
            
            
                
            
graph = EncodeGraph().getGraph01()
a = MST().prims(graph)
print("complete")
print(a)