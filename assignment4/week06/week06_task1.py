class LineEditor:
    def __init__ (self):
        self.list = SinglyLinkedList()
    def runEditor(self):
        command = input("i = insert, d = delete, r = replace,"
                        "p = print, s = write, l = load, q = quite")
        if command == 'i' : self.addLine()
        if command == 'd' : self.deleteLine()
        if command == 'r' : self.replaceLine()
        if command == 'p' : self.printByLine()
        if command == 's' : self.writeToFile()
        if command == 'l' : self.loadFromFile("example.txt")
        if command == 'q' : return 

    def addLine(self):
        pos = int(input("Enter the number  :  "))
        str = input("Enter string  :  ")
        self.list.insertAt(pos, str)
        
    def deleteLine(self):
        pos = int(input("Enter the number  :  "))
        self.list.deleteAt()  
              
    def replaceLine(self):
        pos = int(input("Enter the number  :  "))
        str = input("Enter string  :  ")
        self.list.replaceData(pos, str)
            
    def printByLine(self):
        temp = self.list.head
        while temp :
            print(temp.getData())
            temp = temp.next
    def loadFromFile(self,fname):
        with open(fname,'r') as f:
            content = f.read()
            print(content)
    def writeToFile(self):
        with open('example.txt','w') as f:
            temp = self.list.head
            while temp :    
                f.write(temp.getData() + "\n")
                temp = temp.next
                

class SinglyLinkedList:
    def __init__ (self):
        self.head = None
    def __str__ (self):
        temp = self.head
        s ="" + str(temp) + "->"
        while temp.next:
            temp = temp.next
            s = s + str(temp) + "->"
            
        return s
    
    def getSize(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next            
            count += 1
        return count
    
    def FindLast(self):
        temp = self.head
        while temp.next :
            temp = temp.next
        return temp
    def replaceData(self, pos, d):
        pos = pos - 1
        if pos > self.getSize():
            last = self.FindLast()
            last.setData(d)
        elif pos < 0 :
            self.head.setData(d)
        else :
            temp = self.getNodeAt(pos)
            temp.setData(d)
            
    def reverseList(self):
        pass
    def getData(self, pos):
        pass
    def findData(self,d):
        pass
    def __iter__(self):
        pass
     
    def isEmpty(self):
        return self.head == None
    def clear(self):
        return self.head != None
    def InsertAtFront(self, d):
        new_node = Node(d)
        if self.head :
            new_node.next = self.head
        self.head = new_node
        
    def InsertAtRear(self, d):
        if self.head is None:
            self.InsertAtFront(d)
        else :
            new_node = Node(d)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def getNodeAt(self,pos):
        if pos < 0 or pos > self.getSize(): 
            print("Invalid position")
            return None
        else :
            node = self.head
            while pos > 0 and node is not None:
                node = node.next
                pos -= 1
            return node
    
    def insertAt(self, pos, elem):
        if pos == 0:
            self.InsertAtFront(elem)
            return
        if pos >= self.getSize():
            self.InsertAtRear(elem)
            return
        before = self.getNodeAt(pos - 1)
        if before == None :
            self.head = Node(elem, self.head)
        else :
            node = Node(elem, before.next)
            before.next = node
    
    def deleteAtFront(self):
        if self.head :
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return
        print("list is empty")
            
    def deleteAtRear(self):
        tmp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else : 
                while tmp.next.next:
                    tmp = tmp.next
            second_last = tmp
            last = second_last.next
            second_last.next = None
        return last
    
    def deleteAt(self, pos):

        if pos > self.getSize() or self.isEmpty():
            print("Invalid position access")
            return
        elif pos == 0:
            self.deleteAtFront()
            return 
        elif pos == self.getSize() - 1:
            self.deleteAtRear()
            return
        else :
            before = self.getNodeAt(pos - 1)
            temp = before.next
            before.next = temp.next
            temp.next = None
            return temp
    

class Node:
    def __init__ (self, d = None, nxt = None):
        self.data = d
        self.next = nxt
        
    def __str__ (self):
        return str(self.data)
    def getNext(self):
        return self.next
    def getData(self):
        return self.data
    def setData(self,d):
        self.data = d
    def setNext(self,n):
        self.next = n