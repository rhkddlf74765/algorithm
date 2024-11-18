from week10_task01 import Binarytree, Node, MorseCodes

from week10_task02 import MinHeap, Huffman
def test_Huffman():
    txt = "sfgsghecbnaewqsxcvbaws"
    hm = Huffman(txt)
    hm.makeCodes()
    print(hm.getEncodedText())
    hm.printCodes()
    
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
    
    test_Huffman()
    tstmorsecode()

if __name__ == "__main__":
    main()
