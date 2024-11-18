class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__ (self):
        return str(self.data)
    def getright(self):
        return self.right
    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def setright(self, n):
        self.right = n
    def setleft(self, n):
        self.left = n
    def setdata(self, n):
        self.data = n
    
        
class Binarytree:
    def __init__ (self, root = None):
        self.root = root
        
    def insert(self, value):
        new_node = Node(value)
        if self.isempty() :
            self.root = new_node
            return
        else :
            self.recursive_insert(self.root, value)
            
    def recursive_insert(self, current : Node, value): 
        if value < current.data:
            if current.left is None:
                current.left = Node(value)
                return 
            else : self.recursive_insert(current.left, value)
        elif value > current.data:
            if current.right is None:
                current.right = Node(value)
                return
            else :
                self.recursive_insert(current.right, value)
        else :
            print("value is exist")
            return 
                        
    def isempty(self) -> bool: 
        if self.root is None:
            print("tree is empty")
            return False
        return True
    def getroot(self):
        return self.root
    def setroot(self, key):
        self.root = key
    def getcount(self):
        pass
    def getheight(self, n):
        if n is None:
            return -1 
        hleft = self.getheight(n.getleft())
        hright = self.getheight(n.getright())
        if (hleft > hright):
            return hleft + 1
        else :
            return hright + 1
    def getleafcount(self):
        result = []
        self.getleaf(self.root, result)
        return len(result)
    
    def getleaf(self, n : Node, result = list) -> None: 
        if n is not None:
            if n.left is not None and n.right is not None:
                result.append(n)
            self.getleaf(n.left, result)
            self.getleaf(n.right, result)
    
    def getleaf_list(self):
        result = []
        self.getleaf(self.root, result)
        return result
    
    def clear(self):
        self.root = None
        
    def PrintInorder(self):
        print("Inorder : ",end = " ")
        result = self.getInorder()
        print(result)
               
    def Inorder(self, node, result=None):
        if result is None:
            result = []
        if node is not None:
            self.Inorder(node.left, result)  # node.getleft() 호출
            result.append(node.data)
            self.Inorder(node.right, result)  # node.getright() 호출
        return result

    def getInorder(self):
        result = []
        self.Inorder(self.root, result)
        return result
            
    def PrintPreorder(self):
        print("Inorder : ",end = " ")
        self.Preorder(self.root)
        print(" ")           
        
    def Preorder(self, n : Node):
        if n is not None:
            print(n, end = "->" )
            self.Preorder(n.getleft())
            self.Preorder(n.getright())
             
    def PrintPostorder(self):
        print("Inorder : ",end = " ")
        self.Postorder(self.root)
        print(" ")  
                 
    def Postorder(self, n : Node):
        if n is not None:
            self.Postorder(n.getleft())
            self.Postorder(n.getright())
            print(n, end = "->" )
            
class MorseCodes(Binarytree) :
    def __init__(self, root = None):
        self.root = root
      
    def MakeMorseTree(self):
        morse_code = { ## By using dictionary 
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
            'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
            'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
        }
        self.root = Node()
        for word, code in morse_code.items():
            current_node = self.root
            for symbol in code :
                if symbol == '.':
                    if not current_node.left:
                        current_node.left = Node()
                    current_node = current_node.left
                elif symbol == '-':
                    if not current_node.right :
                        current_node.right = Node()
                    current_node = current_node.right 
            current_node.data = word       
    
    def CharToCode(self, node = Node, target = str, path = str):
        if node is None:
            return None
        if node.data == target:
            return path
        left_path = self.CharToCode(node.left, target, path + ".")
        if left_path:
            return left_path
        return self.CharToCode(node.right, target, path + "-")
    
    def CodeToChar(self, code = str) -> str:
        for char in code:
            current = self.root
            if char == '.':
                current = current.left
            elif char == '.' :
                current = current.right
            return current.data
        
    def PrintMorseTree(self):
        self.PrintInorder()
    def Decode(self, code): ## morse codes -> sentence
        words = code.split('/')
        decoded_message = ''
        for word in words:
            for symbol in word.split(' '):  # 문자별로 구분
                current_node = self.root
                for s in symbol:
                    if s == '.':
                        current_node = current_node.left
                    elif s == '-':
                        current_node = current_node.right
                decoded_message += current_node.data
            decoded_message += ' '
        return decoded_message.strip()
    def Encode(self, sentence = str) -> list: ##sentence -> morsecodes
        result = []
        for char in sentence.upper():
            if char == " ":
                result.append('/')
            else :
                result.append(self.CharToCode(self.root, char, ""))
        return result
    