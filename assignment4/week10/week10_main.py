from week10_task01 import Binarytree, Node, MorseCodes

from week10_task02 import MinHeap, Huffman
def test_Huffman():
    txt = "sfgsghecbnaewqsxcvbaws"
    hm = Huffman(txt)
    hm.makeCodes()
    print(hm.getEncodedText())
    hm.printCodes()
    


def test_minheap():
    h1 = MinHeap()
    h1.insert(45)
    h1.insert(5)
    h1.insert(12)
    h1.insert(47)
    h1.insert(222)
    h1.insert(3)
    h1.printHeap()
    print(h1.heap)
    h1.delete()
    h1.printHeap()
    print(h1.heap)
    
def tstmorsecode():
    code= "... --- ..."
    a = MorseCodes()
    a.MakeMorseTree()
    sentence = a.Decode(code)
    print("decode : ")
    print(sentence)   
    print("encode : ")
    print(a.Encode(sentence))
     
def main():
    # t1 = test_minheap()
    test_Huffman()
    # tstmorsecode()

main()