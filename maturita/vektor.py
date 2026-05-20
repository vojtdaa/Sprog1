import math

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vektor({self.x}, {self.y})"
    
    def __add__(self, jiny):

        if not isinstance(jiny, Vektor):
            raise TypeError("Scitat lze pouze zlomky")
        
        return Vektor(self.x + jiny.x, self.y + jiny.y)
    
    def __sub__(self, jiny):

        if not isinstance(jiny, Vektor): # validace zda pracujeme pouze s objekty
            raise TypeError("Odecitat lze pouze zlomky") # pokud nepracuje s objekty, Python vyhodi error v tomto zneni

        return Vektor(self.x + jiny.x, self.y + jiny.y)
    
    def skalarni(self, jiny):
        return self.x*jiny.x + self.y*jiny.y
    
    def nasobek(self, k):
        return Vektor(self.x * k, self.y * k)
    
    def delka(self):
        return math.sqrt(self.x**2 + self.y**2)
    
u = Vektor(1, 2)
v = Vektor(3, 4)
print(u + v)            # → Vektor(4, 6)
print(u - v)            # → Vektor(-2, -2)
print(u.skalarni(v))    # → 11
print(u.nasobek(3))     # → Vektor(3, 6)
print(v.delka())        # → 5.0