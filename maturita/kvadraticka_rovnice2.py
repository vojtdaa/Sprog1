import math

def kvadraticka_rovnice(a=0, b=0, c=0):
    diskriminant = b**2 - 4*a*c
    vysledek = None
    vysledek2 = None
    if diskriminant < 0:
        return "Zadne reseni v realnych cislech."
    
    if diskriminant == 0:
        vysledek = (b*(-1)) / (2*a)
        return f"({vysledek}, {vysledek})"
    
    if diskriminant > 0:
        vysledek = (b*(-1)+math.sqrt(diskriminant)) / (2*a)
        vysledek2 = (b*(-1)-math.sqrt(diskriminant)) / (2*a)
        return f"({vysledek}, {vysledek2})"
    

print(kvadraticka_rovnice(1, -5, 6))
print(kvadraticka_rovnice(1, -4, 4))
print(kvadraticka_rovnice(1, 2, 5))