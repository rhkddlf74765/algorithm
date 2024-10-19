class Doubly_Linked_list:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        s = ""
        while temp:
            s = s + str(temp) + ""
            temp = temp.next
        return s

    def isEmpty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def findNode(self, d):
        temp = self.head
        pos = 0
        if temp.next == temp.prev:
            print("List is Empty")
            return False
        while temp.next is not None:
            temp = temp.next
            pos += 1
            if temp.getData() == d:
                print("{0} is in index {1}".format(d, pos))
                return True
        print("There are not {}".format(d))
        return False

    def combine(self, other: "Doubly_Linked_list"):  # list 1 + list 2
        if self.isEmpty():
            self.head = other.head
            return self
        if other.head is None:
            return self
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = other.head
        other.head.prev = temp
        return self

    def replaceDataAt(self, pos, d):
        node = self.getNodeAt(pos)
        if node is not None:
            node.data = d

    def getsize(self):
        node = self.head
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def getNodeAt(self, pos):
        if pos < 0 or pos > self.getsize():
            print("Invalid position")
            return
        temp = self.head
        while temp is not None and pos > 0:
            temp = temp.next
            pos -= 1
        return temp

    def insertAt(self, pos, d):
        if pos == self.getsize():
            self.insertAtRear(d)
            return
        if pos == 0:
            self.insertAtFront()
            return
        new_node = Node2(None, d, None)
        before = self.getNodeAt(pos - 1)
        if before is None:
            print("Invalid node")
            return
        new_node.next = before.next
        new_node.prev = before
        before.next.prev = new_node
        before.next = new_node
        if new_node.next is None:
            new_node.next.prev = new_node

    def insertAtRear(self, d):
        new_node = Node2(None, d, None)
        if self.isEmpty():
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        # temp.next.prev = new_node
        new_node.prev = temp

    def insertAtFront(self, d):
        new_node = Node2(None, d, None)
        if self.head is None:  # list doesn't have any node
            self.head = new_node
        else:
            new_node.next = self.head
            if not self.isEmpty():
                self.head.prev = new_node
            self.head = new_node

    def deleteAtFront(self):
        if self.isEmpty():
            print("List is Empty")
            return
        temp = self.head
        if temp.next == temp.prev:  # list is having only one node
            self.head = None
            return
        else:
            self.head = temp.next
            self.head.prev = None

            return temp

    def deleteAtRear(self):
        if self.isEmpty():
            print("List is Empty")
            return
        temp = self.head
        if temp.next == temp.prev:  # list has only one node
            self.head = None
            return temp
        else:
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None
            return temp

    def deleteAt(self, pos):
        temp = Node2()
        if pos == self.getsize():
            temp = self.deleteAtRear()
        elif pos == 0:
            temp = self.deleteAtFront()
        else:
            before = self.getNodeAt(pos - 1)
            if before is None:
                print("Invalid node")
                return None
            temp = before.next
            before.next = temp.next
            temp.next.prev = before
            temp.next = None
            temp.prev = None


class Node2:
    def __init__(self, prev=None, data=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data) + ""

    def getData(self):
        return self.data

    def getPrev(self):
        return self.prev

    def getnext(self):
        return self.next

    def setData(self, p):
        self.data = p

    def setprev(self, p):
        self.prev = p

    def setnext(self, p):
        self.next = p


class sparse_poly(Doubly_Linked_list):
    def __init__(self):
        super().__init__()

    def display(self, msg):
        print("\t", msg, end=" ")
        node = self.head
        while node is not None:
            print(node, end=" ")
            node = node.next
        print()

    def read(self):
        self.clear()
        while True:
            token = input("Insert Term (coeff, expon) : ").split(" ")
            if token[0] == "q":  # sgn = q : over
                self.display("Polynomial")
                return
            self.insertAt(self.getsize(), Term(token[0], token[1]))

    def getdegree(self):
        if self.isEmpty():
            return None
        term = self.head
        maxdegree = 0
        while term:
            if term.getData().getexpon() > maxdegree:
                maxdegree = term.getData().getexpon()
            term = term.next
        return maxdegree

    def __add__(self, other: Doubly_Linked_list):
        result = sparse_poly()
        resultlist = []
        selftemp = self.head
        while selftemp:
            resultlist.append(Term(selftemp.getData().getcoeff(), selftemp.getData().getexpon()))
            selftemp = selftemp.next
        othertemp = other.head
        while othertemp:
            found = False  
            for i in range(len(resultlist)):
                if resultlist[i].getexpon() == othertemp.getData().getexpon():
              
                    new_coeff = resultlist[i].getcoeff() + othertemp.getData().getcoeff()
                    resultlist[i].setcoeff(new_coeff)
                    found = True
                    break
            if not found:
                resultlist.append(Term(othertemp.getData().getcoeff(), othertemp.getData().getexpon()))
            othertemp = othertemp.next
        for term in resultlist:
            result.insertAt(result.getsize(), Term(term.getcoeff(), term.getexpon()))
        return result

    

    def __sub__(self, other):
        result = sparse_poly()
        resultlist = []
        selftemp = self.head
        while selftemp:
            resultlist.append(Term(selftemp.getData().getcoeff(), selftemp.getData().getexpon()))
            selftemp = selftemp.next
        othertemp = other.head
        while othertemp:
            found = False  
            for i in range(len(resultlist)):
                if resultlist[i].getexpon() == othertemp.getData().getexpon():
                    new_coeff = resultlist[i].getcoeff() - othertemp.getData().getcoeff()
                    resultlist[i].setcoeff(new_coeff)
                    found = True
                    break
            if not found:
                resultlist.append(Term(-othertemp.getData().getcoeff(), othertemp.getData().getexpon()))
            othertemp = othertemp.next
        for term in resultlist:
            result.insertAt(result.getsize(), Term(term.getcoeff(), term.getexpon()))
        return result



class Term:
    def __init__(self, coeff=None, expon=None):
        self.coeff = coeff
        self.expon = expon

    def __str__(self):
        return str(self.coeff) + "x*" + str(self.expon)

    def getcoeff(self):
        return int(self.coeff)

    def getexpon(self):
        return int(self.expon)

    def setcoeff(self, d):
        self.coeff = d

    def setexpon(self, d):
        self.expon = d
