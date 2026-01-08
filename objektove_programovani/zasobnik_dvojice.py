class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
uzel_1 = Node(1)

uzel_2 = Node(2)
uzel_2.next = uzel_1

uzel_3 = Node(3)
uzel_3.next = uzel_2

class Stack:
    def __init__(self):
        self.top = None
    
    def IsEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def Push(self, cislo):
        if self.IsEmpty():
            novy_top = Node(cislo)
            self.top = novy_top
        else:
            novy_top = Node(cislo)
            self.next = self.top
            self.top = novy_top

    def Pop(self):
        if self.IsEmpty() == True:
            return
        elif self.top.next == None:
            value = self.top.value
            self.top = None
            return value


    def Show(self):
        return self.top.value

zasoba = Stack()
zasoba.Push(2)
zasoba.Push(5)
zasoba.Push(3)
zasoba.Pop()
zasoba.Pop()

print(zasoba.Show())

        