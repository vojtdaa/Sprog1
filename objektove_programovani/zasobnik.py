class Zasobnik:

    def __init__(self, seznam = []):
        self.seznam = seznam
        pass

    def IsEmpty(self):
        if self.seznam:
            return False
        else: return True

    def Push(self, new):
        self.seznam.append(new)

    def Pop(self):
        if self.IsEmpty():
            return
        
        return self.seznam.pop()
    
    
    def Peek(self):
        if self.IsEmpty():
            return
        return self.seznam[-1]
    
    def Clear(self):
        self.seznam = []

    def __str__(self):
        return str(self.seznam)
            

zasoba = Zasobnik()
zasoba.Push(1)
zasoba.Push(2)
zasoba.Push(2)
zasoba.Push(2)
print(zasoba.Pop())

print(zasoba.IsEmpty())
print(zasoba.Peek())
print(str(zasoba))