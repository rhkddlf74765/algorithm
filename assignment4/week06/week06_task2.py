from week06_task1 import Node

class JosephusProblem:
    def __init__(self, n1 = 10, m1 = 3):
        self.list = CircularlyLinkedList()
        self.n = n1
        self.m = m1
        for i in range(1, n1+1):
            self.list.InsertAtFront(i)
            
    def RunJosephusProblem(self):
        print(self.list)
        temp = self.list.head.next
        count = 0
        while True:
            temp = temp.next
            count += 1
            if count == self.m:
                temp2 = temp.next
                pos = self.list.findPosition(temp)
                print("Eleminated ->",self.list.deleteAt(pos))
                temp = temp2
                print(self.list)
                count = 0
                if temp == temp.next :
                    print("Selected ->",temp)
                    break
        


class CircularlyLinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        pass
    
    def reverseList(self):
        pass
    
    def findNode(self, data):
        pass
    
    def findPosition(self, node):
        temp = self.head.next
        pos = 0
        while True:
            temp = temp.next
            pos += 1
            if temp.data == node.data or pos > self.getSize() + 1:
                break
        return pos % self.getSize()
    
        
    def __str__ (self):
        temp = self.head
        s = ""
        while self.head is not None:
            s = s+str(temp)+ "->"
            temp = temp.next
            if temp == self.head:
                break
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def getSize(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next            
            count += 1
            if node == self.head:
                break
        return count
    
    def getNodeAt(self,pos):
        if pos < 0 or pos > self.getSize() : return None
        node = self.head
        if self.head is not None :
            while True:
                node = node.next
                pos -= 1
                if pos < 0 :
                    break
            return node
        
        

    def InsertAtFront(self, d):
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.head.next = self.head
        else :
            new_node.next = self.head.next
            self.head.next = new_node
            
    def InsertAtRear(self, d):
            new_node = Node(d)
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
                self.head.next = self.head
            else :
                new_node.next = self.head.next
                self.head.next = new_node
                self.head = new_node
                
    def InsertAt(self, d, pos):
        if pos == self.getSize():
            self.InsertAtRear(d)
            return 
        if pos == 0:
            self.InsertAtFront(d)
            return 
        
        new_node = Node(d)
        before = self.getNodeAt(pos - 1)
        if before is None:
            print("This node does not exit...")
            return 
        new_node.next = before.next
        before.next  = new_node
        
    def deleteAtFront(self):
        if self.isEmpty():
            print("List is Empty....")
            return
        temp = self.head
        if(temp == temp.next) :
            self.head = None
            return temp
        else :
            temp = self.head.next
            self.head.next = temp.next
            temp.next = None
            return temp
        
    def deleteAtRear(self):
        temp = self.head
        if self.isEmpty():
            print("List is Empty....")
            return
        if(temp == temp.next) :
            self.head = None
            return temp
        else :
            before = self.getNodeAt(self.getSize()-2)
            self.head = before
            self.head.next = temp.next
            temp.next = None
            return temp
        
    def deleteAt(self, pos):
        if pos == self.getSize() - 1 :
            return self.deleteAtRear()
        elif pos == 0 :
            return self.deleteAtFront()
        else :
            before = self.getNodeAt(pos - 1)
            if before is None:
                print("This node does not exist...")
                return
            temp = before.next
            before.next = temp.next
            temp.next = None
            return temp
                    
        
        