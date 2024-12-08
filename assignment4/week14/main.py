from encodegraph import EncodeGraph
eg = EncodeGraph()
def test_graph01():
    g = eg.getGraph01()
    print(g.getorder())
    print(g)
    print(g.gdict)
    g.printADJlist()
    g.RemoveVertex(g.gdict.keys()[0])
    g.printADJlist()
    m = g.getADJmatrix()
    for row in m:
        print(row)
    a=g.getVertixList()
    print()
    print(a)
    
    
def main():
    test_graph01()
    
if __name__ == "__main__":
    main()