mala = "aeiouáéěíóúůyý"
velka = "AEIOUÁÉĚÍÓÚŮYÝ"

def pocet_samohlasek(slovo):
    pocet = 0
    for i in slovo:
        if i in mala or i in velka:
            pocet += 1
    return pocet

print(pocet_samohlasek('Ahoj světe'))    # → 4
print(pocet_samohlasek('Python'))         # → 2
print(pocet_samohlasek('Programování'))   # → 5