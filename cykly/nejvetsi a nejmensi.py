cislo = 1362

cifra1 = 0
cifra2 = 0
cifra3 = 0
cifra4 = 0

odecitani = 1000

pocet = 0

while cislo > 1000:
    cislo -= 1000
    pocet += 1

cifra1 = pocet
pocet = 0

while cislo > 100:
    cislo -= 100
    pocet += 1

cifra2 = pocet
pocet = 0

while cislo > 10:
    cislo -= 10
    pocet += 1

cifra3 = pocet
pocet = 0

while cislo > 0:
    cislo -= 1
    pocet += 1

cifra4 = pocet
pocet = 0

print(cifra1, cifra2, cifra3, cifra4)