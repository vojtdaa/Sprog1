class Prvek:
    def __init__(self, hodnota, predchozi):
        self.hodnota = hodnota
        self.predchozi = predchozi
    
    def __str__(self):
        return str(self.hodnota)

class Zasobnik:
    def __init__(self):
        self.top = None

    def novy_prvek(self, hodnota):
        self.top = Prvek(hodnota, self.top)
        return self.top
    
    def peak(self):
        return self.top
    
    def pop(self):
        if self.top != None:
            self.top = self.top.predchozi
        return self.top
    
    def isEmpty(self):
        if self.top == None:
            is_empty = True
        else: is_empty = False

        return is_empty

z = Zasobnik()

z.novy_prvek(26)
z.novy_prvek(15)
print(z.peak())
z.pop()
print(z.peak())
print(z.isEmpty())
z.pop()
z.pop()
print(z.isEmpty())