
class Stack:
    def __init__(self, size):
        self.itemSize = size
        self.items = [None]*self.itemSize
        self.top =  -1
        
    def __contains__(self, items):
        for i in self.items:
            if i == items : 
                return True
        return False
    def __str__(self) -> str:
        out = ''

        for i in range(self.size()):
            out = out + str(self.items[i]) + ' '
        return out
    def __iter__(self):
        self.Iter_count = self.size()
        return self
    def __next__(self):
        if self.Iter_count > 0 :
            self.Iter_count -= 1
            return self.items[self.Iter_count]
        else : 
            raise StopIteration
    def size(self):
        return self.top + 1
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top + 1 == self.itemSize
            
    def push(self, item):
        if not self.isFull():
            self.top = self.top + 1
            self.items[self.top] = item
        else : 
            print("stack is full")
    def pop(self):
        if not self.isEmpty():
            item = self.items[self.top]
            self.top = self.top - 1
            return item
        else : 
            print("stack is already empty")
    def clear(self):
        self.items = [None] * self.itemSize
    def display(self):
        for i in self.items:
            print("{} ", format(i))
    def peek(self):
        return self.items[self.top]
    def find(self, item):
        for i in self.items:
            if i == item :
                return True
        return False

class stackApplications:
    def precedence (self, op):
        if (op == '(' or op ==')'):
            return 0;
        elif (op == '+' or op == '-'):
            return 1;
        elif (op == '*' or op == '/'):
            return 2;
        else :
            return -1
        
    def checkBrackets(self, statement):
        stack = Stack(10)
        for ch in statement:
            if ch in ('{', '[', '('):
                stack.push(ch)
            elif ch in ('}', ']', ')'):
                if stack.isEmpty():
                    return False
                else : 
                    left = stack.pop()
                    if (ch == "}" and left != "{") or \
                        (ch =="]" and left != "[") or\
                            (ch == ")" and left != "(") :
                                return False
        return stack.isEmpty()
    def convertBase(self, num):
        stack = Stack(10)
        while num > 0 :
            decimal_num = num % 2
            num = num // 2
            stack.push(decimal_num)
        out = []
        for i in stack:
            out.append(i)
        return out
    
    def Infix2Postfix(self, expr):
        s = Stack(10)
        output = []
        for term in expr :
            if term in '(':
                s.push('(')
            elif term in ')':
                while not s.isEmpty():
                    op = s.pop()
                    if op == '(':
                        break
                    else :
                        output.append(op)
            elif term in "+-*/" : 
                while not s.isEmpty():
                    op = s.peek()
                    if (self.precedence(term) <= self.precedence(op)):
                        output.append(op)
                        s.pop()
                    else : break
                s.push(term)
            else :
                output.append(term)
        while not s.isEmpty():
            output.append(s.pop())
        return output
    
    def EvalPostfix(self, expr):
        stack = Stack(10)
        for i in expr:
            op = self.precedence(i)
            if op == -1:
                stack.push(int(i))
            elif op == 1 or op == 2:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    tempt = b + a
                    stack.push(tempt)
                elif i == '-':
                    tempt = b - a
                    stack.push(tempt)
                elif i == '*':
                    tempt = b * a
                    stack.push(tempt)
                elif i == '/':
                    tempt = b / a
                    stack.push(tempt)
        return stack.pop()               
                
              