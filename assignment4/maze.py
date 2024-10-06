from week04 import CircularQueue, CircularDeque
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from assignment2 import week03
class Cell:
    def __init__ (self, r = 0, c = 0):
        self.row = r
        self.col = c
    def __str__(self) -> str:
        return "(" + str(self.row) + ", " + str(self.col) + ")"

class Maze:
    MAZE_SIZE = 6
    def getmap(self):
        map = [['1,','1','1','1','1','1'],
               ['e','0','1','0','0','1'],
               ['1','0','0','0','1','1'],
               ['1','0','1','0','1','1'],
               ['1','0','1','0','0','x'],
               ['1','0','0','0','1','1']]
 
    
        return map
    
    def isValidPos(self, x, y ,map):
        if(x < 0 or y<0 or x >= self.MAZE_SIZE or y >= self.MAZE_SIZE):
            return False
        else :
            return map[x][y] == '0' or map[x][y] =='x'
    
    def BFS1(self): # use circulardeque
        map = self.getmap()
        que = CircularDeque()
        entry = Cell(1,0)
        que.enqueue(entry)
        print("\n BFS1 : using queue data structure : ")

        while not que.isEmpty():
            here = que.dequeue()
            print(here, end ='->')
            x = here.row
            y = here.col
            
            if (map[x][y] == 'x'):
                print("\n goal is found")
                return True
            else : 
                map[x][y] = '.'
                if self.isValidPos(x, y-1, map) : 
                    que.enqueue(Cell(x,y-1))
                if self.isValidPos(x, y+1, map) : 
                    que.enqueue(Cell(x,y+1))
                if self.isValidPos(x+1, y, map) : 
                    que.enqueue(Cell(x+1,y))
                if self.isValidPos(x-1, y, map) : 
                    que.enqueue(Cell(x-1,y))     
    def BFS2(self): # use circularqueue
        map = self.getmap()
        que = CircularQueue()
        entry = Cell(1,0)
        que.enqueue(entry)
        print("\n BFS2 : using queue data structure : ")
        
        while not que.isEmpty():
            here = que.dequeue()
            print(here, end ='->')
            x = here.row
            y = here.col
            
            if (map[x][y] == 'x'):
                print("\n goal is found")
                return True
            else : 
                map[x][y] = '.'
                if self.isValidPos(x, y-1, map) : 
                    que.enqueue(Cell(x,y-1))
                if self.isValidPos(x, y+1, map) : 
                    que.enqueue(Cell(x,y+1))
                if self.isValidPos(x+1, y, map) : 
                    que.enqueue(Cell(x+1,y))
                if self.isValidPos(x-1, y, map) : 
                    que.enqueue(Cell(x-1,y))
    def DFS1(self): # using stack from circulardeque(font operation)
        map = self.getmap()
        stack = CircularDeque()
        entry = Cell(1,0)
        stack.addFront(entry)
        print("\n DFS1 : using queue data structure : ")
        
        while not stack.isEmpty():
            here = stack.getFront()
            stack.deleteFront()
            print(here, end ='->')
            x = here.row
            y = here.col
            
            if (map[x][y] == 'x'):
                print("\n goal is found")
                return True
            else : 
                map[x][y] = '.'
                if self.isValidPos(x, y-1, map) : 
                    stack.addFront(Cell(x,y-1))
                if self.isValidPos(x, y+1, map) : 
                    stack.addFront(Cell(x,y+1))
                if self.isValidPos(x+1, y, map) : 
                    stack.addFront(Cell(x+1,y))
                if self.isValidPos(x-1, y, map) : 
                    stack.addFront(Cell(x-1,y))
        
    def DFS2(self): #using stack
        map = self.getmap()
        stack = week03.Stack(10)
        entry = Cell(1,0)
        stack.push(entry)
        print("\n DFS2 : using stack data structure : ")
        
        while not stack.isEmpty():
            here = stack.pop()
            print(here, end ='->')
            x = here.row
            y = here.col
            
            if (map[x][y] == 'x'):
                print("\n goal is found")
                return True
            else : 
                map[x][y] = '.'
                if self.isValidPos(x, y-1, map) : 
                    stack.push(Cell(x,y-1))
                if self.isValidPos(x, y+1, map) : 
                    stack.push(Cell(x,y+1))
                if self.isValidPos(x+1, y, map) : 
                    stack.push(Cell(x+1,y))
                if self.isValidPos(x-1, y, map) : 
                    stack.push(Cell(x-1,y))
    def DFS3(self): #stack from circulardeque(rear operation)
        map = self.getmap()
        stack = CircularDeque()
        entry = Cell(1,0)
        stack.addRear(entry)
        print("\n DFS1 : using queue data structure : ")
        
        while not stack.isEmpty():
            here = stack.getRear()
            stack.deleteRear()
            print(here, end ='->')
            x = here.row
            y = here.col
            
            if (map[x][y] == 'x'):
                print("\n goal is found")
                return True
            else : 
                map[x][y] = '.'
                if self.isValidPos(x, y-1, map) : 
                    stack.addRear(Cell(x,y-1))
                if self.isValidPos(x, y+1, map) : 
                    stack.addRear(Cell(x,y+1))
                if self.isValidPos(x+1, y, map) : 
                    stack.addRear(Cell(x+1,y))
                if self.isValidPos(x-1, y, map) : 
                    stack.addRear(Cell(x-1,y))

m = Maze()
m.BFS1()
m.BFS2()
m.DFS1()
m.DFS2()
m.DFS3()