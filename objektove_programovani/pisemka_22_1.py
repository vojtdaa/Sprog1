import math

class Bod:
    def __init__(self, x_bod, y_bod):
        self.x = x_bod
        self.y = y_bod
    
    def vypis(self):
        return f"[{self.x}; {self.y}]"

    
class Obdelnik:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        pass

    def Obsah(self):
        obsah = (self.c.x - self.a.x) * (self.c.y - self.b.y)
        return obsah

    def Move(self, kam_x, kam_y):
        self.a.x += kam_x
        self.a.y += kam_y

        self.b.x += kam_x
        self.b.y += kam_y

        self.c.x += kam_x
        self.c.y += kam_y

        self.d.x += kam_x
        self.d.y += kam_y
        return

    def Scale(self, value):
        self.value = value
        if value < 1:
            self.b.x -= (self.b.x - self.a.x) * value 
            self.d.y -= (self.d.y - self.a.y) * value
        else:
            self.b.x = (self.b.x - self.a.x) * value + self.a.x
            self.d.y = (self.d.y - self.a.y) * value + self.a.y
            
        self.d.y += (self.d.y - self.a.y) * value

        self.c.x = self.b.x
        self.c.y = self.d.y
        return

new_rect = Obdelnik(Bod(-1, -1), Bod(1, -1), Bod(1, 1), Bod(-1, 1))
print(new_rect.Obsah())

new_rect.Move(10, 10)
print(new_rect.a.vypis())
print(new_rect.b.vypis())
print(new_rect.c.vypis())
print(new_rect.d.vypis())

print(new_rect.Obsah())

new_rect.Scale(5)
print(new_rect.Obsah())

new_rect.Scale(2)
print(new_rect.Obsah())