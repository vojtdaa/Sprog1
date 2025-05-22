import random

def Prohazet(slovo):
    cislo = len(slovo)
    zapis = []
    nahodny_zapis = []
    random_az = 0

    for x in range(0, cislo):
        zapis.append(x)
        random_az += 1

    for x in range(cislo):
        nahodne_cislo = random.randint(0, random_az - 1)
        nahodny_zapis.append(zapis[nahodne_cislo])
        zapis.pop(nahodne_cislo)
        random_az -= 1
        
    vysledek = ""
    for x in nahodny_zapis:
        vysledek += slovo[x]

    return vysledek

print(Prohazet(str(input("Zadej slovo na zamíchání: "))))