import math

def kvadraticka_rovnice(a, b, c):
    diskriminant = b**2 - 4*a*c
    dvojnasobny_koren = False
    if a == 0:
        return None

    if diskriminant < 0:
        return None
    elif diskriminant == 0:
        dvojnasobny_koren = True
        vysledek1 = (-b)/(2*a)
        vysledek2 = vysledek1
    else:
        vysledek1 = (-b + math.sqrt(diskriminant))/(2*a)
        vysledek2 = (-b - math.sqrt(diskriminant))/(2*a)

    return vysledek1, vysledek2


print(kvadraticka_rovnice(1, 5, 3))
print(kvadraticka_rovnice(1, -20, 3))