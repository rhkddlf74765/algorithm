from task1 import Doubly_Linked_list, sparse_poly, Term

def tstdll():
    dll = Doubly_Linked_list()
    dll.insertAtRear(11)
    dll.insertAtFront(22)
    dll.insertAtFront(33)
    dll.insertAtFront(44)
    dll.insertAtFront(55)
    dll.insertAtRear(66)
    dll.insertAtRear(77)
    dll.insertAtRear(88)
    print(dll)
    dll.insertAt(3,99)
    dll.insertAt(6,123)
    print(dll)
    dll.deleteAtFront()
    print(dll)
    dll.deleteAtFront()
    print(dll)
    dll.deleteAtRear()
    print(dll)
    dll.deleteAt(4)
    print(dll)
    dll.findNode(22)
    dll.replaceDataAt(3,11111)
    print(dll)
    dll2 = Doubly_Linked_list()
    dll2.insertAtFront(4)
    dll2.insertAtFront(5)
    dll2.insertAtFront(6)
    dll2.insertAtFront(7)
    print(dll2)
    print(dll.combine(dll2))
    dll3 = Doubly_Linked_list()
    print(dll3.combine(dll2))
   
def tstpoly():
    p1 = sparse_poly()
    p1.read()
    p2 = sparse_poly()
    p2.read()
    # p3 = p1 + p2
    p4 = p1 - p2
    # p3.display("add = ")
    p1.display("p1 = ")
    p2.display("p2 = ")
    p4.display("sub = ")
    
def main(): 
    # tstdll()
    tstpoly()
    
if __name__ == "__main__":
    main()