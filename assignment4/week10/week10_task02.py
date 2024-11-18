class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)
    def insert(self, n):
        pass
    def delete(self):
        pass

class MinHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0) #first element is 0
        
    def insert(self, n):
        self.heap.append(n)
        i = self.getSize()
        print(i)
        while i != 1 and n < self.getParent(i):
            self.heap[i] = self.getParent(i)
            i = i // 2
        self.heap[i] = n
        
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.getSize()]
            while child <= self.getSize():
                if child < self.getSize() and self.getLeft(parent) > self.getRight(parent):
                    child += 1
                if last <= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child = child * 2
            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot
        
            
    def printHeap(self):
        level = 1
        for i in range(1, self.getSize() + 1):
            if i == level :
                print('')
                level = level * 2
            print(str(self.heap[i]), end=" ")
        print("\n -----------------------------------")
    def isEmpty(self):
        return len(self.heap) == 1
    def getSize(self):
        return len(self.heap) - 1
    def getParent(self, i):
        return self.heap[i//2]
    def getLeft(self, i):
        return self.heap[2*i]
    def getRight(self, i):
        return self.heap[2*i + 1]
    
class HNode:
    def __init__(self, char = None, freq = None, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.char) + ":" + str(self.freq)
    def __eq__(self, n):
        return self.freq == n.freq
    def __ne__(self, other):
        return self.freq != other.freq
    
    def __lt__(self, other):
        return self.freq < other.freq
    def __ge__(self, other):
        return self.freq >= other.freq
    def __le__(self, other):
        return self.freq <= other.freq

class Huffman:
    def __init__(self, txt = ""):
        self.text = txt
        self.mh = MinHeap()
        self.codes = {}
        self.decode = {}
    def makeFrequencies(self):
        frequencies = {}
        for c in self.text:
            if not c in frequencies:
                frequencies[c] = 0
            frequencies[c] += 1
        return frequencies
    def makeHeap(self):
        frequencies = self.makeFrequencies()
        for key in frequencies:
            node = HNode(key, frequencies[key])
            self.mh.insert(node)
    def makeHuffmanTree(self):
        self.makeHeap()
        while (len(self.mh.heap) > 2 ):
            p = self.mh.delete()
            q = self.mh.delete()
            r = HNode(None, p.freq + q.freq, p, q)
            self.mh.insert(r)
        return self.mh.delete()
    def makeCodes(self):
        root = self.makeHuffmanTree()
        code = ""   
        self.makeCodesRec(root, code) 
    def makeCodesRec(self, root, code):
        if root is None:
            return 
        if root.char != None:
            self.codes[root.char] = code
            self.decode[root.char] = root.char
            return 
        self.makeCodesRec(root.left, code + "0")
        self.makeCodesRec(root.right, code + "1")
    def getEncodedText(self):
        encodedText = ""
        for c in self.text:
            encodedText += self.codes[c]
        return encodedText
    def printCodes(self):
        print("Huffman Codes:")
        for char, code in self.codes.items():
            if char == ' ':
                print("'Space':", code)  # 공백 문자 표시
            else:
                print(f"'{char}': {code}")
    
    
    