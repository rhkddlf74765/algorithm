Max_Size = 10
class CircularQueue:
    def __init__(self) :
        self.front = 0
        self.rear = 0
        self.items = [None]*Max_Size
        
    def __str__(self) :
        out = []
        outstr = ''
        a = (self.front + 1 + Max_Size) % Max_Size
        b = (self.rear + 1 + Max_Size) % Max_Size
        if self.front < self.rear:
            out = self.items[a : b]
        for i in out:
            outstr = outstr + str(i) + ", "
        
        
        return outstr
    def isEmpty(self):
        return self.rear == self.front
    def isFull(self) :
        return self.front == (self.rear + 1) % Max_Size   
    def clar(self):
        self.front = self.rear
    def __len__(self) : 
        return (self.rear - self.front)
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear +  1) % Max_Size
            self.items[self.rear] = item
        else :
            print("Queue is full\n")
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % Max_Size
            item = self.items[self.front]
            return item
        else : 
            print("Queue is empty\n ")
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % Max_Size] 
        else : "Queue is empty\n" 
    def printQueue(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1 : self.rear + 1]
            print(out)
                  
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addFront(self,item):
        if not self.isFull():
            self.front = (self.front - 1 + Max_Size) % Max_Size
            self.items[self.front] = item
        else : 
            "Deque is full\n"
    def addRear(self,item):
        self.enqueue(item)
    def deleteFront(self):
        self.dequeue()
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            return item
        else : 
            print("Deque is empty\n")
    def getRear(self):
        return self.items[self.rear]
    def getFront(self):
        return self.items[self.front]
    
