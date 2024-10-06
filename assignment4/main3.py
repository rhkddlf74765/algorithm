from week04 import CircularQueue, CircularDeque, Max_Size
from simulation import TicketCounterSimulation
from maze import Maze
    
    
def mazetest():
    m = Maze()
    m.BFS1()
    print(m.getmap()[1][0])
    
def TCS():
    tc = TicketCounterSimulation(2,100,1,3)
    tc.run()
def main():
        # a = CircularDeque()
    # for i in range(6):
    #     a.enqueue((i+1)*2)
    # print(a)
    # a.addFront(5)
    # print(a)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    # a.addRear(12)
    # print(a)
    # a.deleteFront()
    # print(a)
    # a.deleteRear()
    # print(a)
    # print(a.getRear())
    
    TCS()
    # mazetest()

    return 0

if __name__ == '__main__' :
    main()
    
