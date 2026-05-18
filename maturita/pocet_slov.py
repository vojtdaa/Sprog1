def pocet_slov(n):
    mezera = True
    vysledek = 0

    for i in n:
        if i == " ":
            mezera = True

        elif mezera == True:
            vysledek += 1
            mezera = False
            
    return vysledek

print(pocet_slov('Ahoj světe'))   # → 2
print(pocet_slov('Python'))        # → 1
print(pocet_slov(''))              # → 0
print(pocet_slov('  ahoj  '))      # → 1
